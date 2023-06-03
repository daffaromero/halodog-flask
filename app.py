from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
from keras.models import load_model
import tensorflow_hub as hub
from io import BytesIO
import requests  # move requests to the end of the imports

app = Flask(__name__)

model = load_model('models/dafrom_model.h5', custom_objects={
                   'KerasLayer': hub.KerasLayer})
print('Loaded model: ', model)


def preprocess_image_from_url(url):
    """
    Takes an image URL and turns the image into a tensor
    """
    # Read the image
    res = requests.get(url).content
    img = Image.open(BytesIO(res)).convert('RGB')

    # Resize the image to our desired size: 224, 224
    img = img.resize((224, 224))

    # Convert the image into a numpy array and normalize pixel values
    img_array = np.array(img) / 255.0

    # Expand dimensions so the image is compatible with the model's input shape
    img_tensor = np.expand_dims(img_array, axis=0)

    return img_tensor  # Return only the tensor


types = ['Bird', 'Dog', 'Rabbit', 'Fish', 'Cat', 'Guinea pig / mouse', 'Other']


def get_predicted_label(pred_probabilities):
    """
    Turns an array of predictions probabilities into a label
    """
    return types[pred_probabilities.argmax()]


@app.route("/", methods=['GET'])
def home():
    return ('<div>Welcome to the Tulations Flask ML runner!</div>'
            '<div>Use the /predict endpoint to make predictions</div>')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'url' not in request.json:
        return jsonify({'error': 'No image URL in the request'}), 400
    url = request.json['url']
    if url == '':
        return jsonify({'error': 'No image URL provided'}), 400
    else:
        # Only one value is returned now
        image = preprocess_image_from_url(url)
        pred = model.predict(image)
        pred_class = get_predicted_label(
            pred[0])  # Assuming categorical output
        return jsonify({'predicted_class': pred_class}), 200


if __name__ == '__main__':
    app.run(debug=True)
