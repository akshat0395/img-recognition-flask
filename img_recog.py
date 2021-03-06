from keras.models import load_model
from PIL import Image
import numpy as np
from flasgger import Swagger

from flask import Flask, request
app = Flask(__name__)
swagger = Swagger(app)

model = load_model('./model.hdf5')


@app.route('/predict_digit', methods=['POST'])
def predict_digit():
    """API endpoint for returning prediction
    ---
    parameters:
        - name: image
          in: formData
          type: file
          required: true
    """
    im = Image.open(request.files['image'])
    im2arr = np.array(im).reshape((1,1,500000,500000))
    return str(np.argmax(model.predict(im2arr)))

if __name__ == '__main__':
    app.run()
