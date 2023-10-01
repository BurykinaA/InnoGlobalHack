from app.photo import photo
from flask import request
import requests
from flask import current_app as app, make_response, jsonify, send_file
from flask_cors import cross_origin
import base64
import csv
import io
import os
import numpy as np
from PIL import Image
from app.screen_detecting.test import get_sreenshot
from app.get_number_of_faces.numbers import get_numbers

# from app.get_number_of_faces.numbers import get_number
from app.get_number_of_faces.grad import check_gradient
from app.main_model.test1 import get_score


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
        cnt, tmp = get_numbers(image_io)
        if cnt == 0:
            resp = {"log": "empty", "photo": data["photo"], "name": data["name"]}
        else:
            print(tmp)
            ans1 = get_score(numpy_array)
            ans2 = get_sreenshot(numpy_array)
            if check_gradient(numpy_array, 1000):
                resp = {"log": "fake", "photo": data["photo"], "name": data["name"]}
            else:

                if tmp >= 95:
                    resp = {"log": "real", "photo": data["photo"], "name": data["name"]}
                else:
                    if ans2 == 1:
                        resp = {"log": "real", "photo": data["photo"], "name": data["name"]}
                        
                    if ans1 == 0: #без все много лучше
                        resp = {"log": "fake", "photo": data["photo"], "name": data["name"]}
                    
                        
                    


        responses.append(resp)

    return make_response(responses)

@photo.post("/api/cam")
def camera_pic():
    data_list = request.json  # Теперь ожидаем список JSON объектов
    responses = []

    for data in data_list:
        image_bytes = base64.b64decode(data["photo"])
        image_io = io.BytesIO(image_bytes)
        image = Image.open(image_io)
        numpy_array = np.array(image)
        if get_numbers(image_io) == 0:
            resp = {'log': 'empty' , "photo": data["photo"]}
        else:
            resp = {'log': 'real', "photo": data["photo"]} if get_sreenshot(numpy_array) == 1 else {'log': 'fake', "photo":  data["photo"]}
        responses.append(resp)

    return make_response(responses)


@photo.post("/api/download")
def download():
    data_list = request.json 
    
    csv_data = [{"filename": item["name"], "preds": item["log"]} for item in data_list]
    current_directory = os.path.abspath(os.path.dirname(__file__))
    csv_file_path = os.path.join(current_directory, "output.csv")
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "preds"])  # Заголовки столбцов
        for row in csv_data:  # Используйте csv_data для записи данных
            writer.writerow([row["filename"], row["preds"]])
    response = send_file(csv_file_path, as_attachment=True)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    response.headers["Content-Type"] = "text/csv"
    return response