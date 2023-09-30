from app.photo import photo
from flask import request
import requests
from flask import current_app as app, make_response, jsonify
from flask_cors import cross_origin
import base64
import io
import numpy as np
from PIL import Image
from app.screen_detecting.test import get_sreenshot
from app.get_number_of_faces.numbers import get_numbers
# from app.get_number_of_faces.numbers import get_number


@cross_origin()
@photo.post("/api/photo")
def make_correction():
    data_list = request.json  # Теперь ожидаем список JSON объектов
    responses = []

    for data in data_list:
        image_bytes = base64.b64decode(data["photo"])
        image_io = io.BytesIO(image_bytes)
        image = Image.open(image_io)
        numpy_array = np.array(image)
        if get_numbers(image_io) == 0:
            resp = {'log': 'No face' , "photo": data["photo"]}
        else:
            resp = {'log': 'Real', "photo": data["photo"]} if get_sreenshot(numpy_array) == 1 else {'log': 'Fake', "photo":  data["photo"]}
        responses.append(resp)

    return make_response(responses)
