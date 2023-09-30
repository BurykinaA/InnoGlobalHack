from app.photo import photo 
from flask import request
import requests
from flask import current_app as app, make_response, jsonify
from flask_cors import cross_origin
import base64
import io
import numpy as np
from PIL import Image
from ..get_number_of_faces.numbers import get_numbers
from ..screen_detecting.test import get_sreenshot



@cross_origin()
@photo.post('/api/photo')
def make_correction():
    data = request.json
    image_bytes = base64.b64decode(data['photo'][23:])
    image_io = io.BytesIO(image_bytes)
    image = Image.open(image_io)
    numpy_array = np.array(image)
<<<<<<< HEAD
    if get_numbers(image_io) != 1:
        resp = {'photo': 'No face'}
    else:
        resp = {'photo': 'Real'} if get_sreenshot(numpy_array) else {'photo': 'Fake'}

    # resp = {'photo': 'Real'} if get_sreenshot(numpy_array) == 1 else {'photo': 'Fake'}
=======
    # if get_numbers(image_io) != 1:
    #     resp = {'photo': 'No face'}
    # else:
    #     resp = {'photo': 'Real'} if get_sreenshot(numpy_array) else {'photo': 'Fake'}

    resp = {'photo': 'Real'} if get_sreenshot(numpy_array) == 1 else {'photo': 'Fake'}
>>>>>>> 5b6ca6f6f03a8bd50c22449ca291b16842183d83

    return make_response(resp)