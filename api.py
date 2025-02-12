# pip install flask-restful - создание API интерфейсов

from flask import Flask 
from flask_restful import Api, Resource, reqparse  
import random


my_list = [
    {
        "id": 1, 
        "text": "Hello World!",
        "language": "en"
    },
    {
        "id": 2, 
        "text": "Привет мир!",
        "language": "ru"
    },
    {
        "id": 3, 
        "text": "Hallo Welt!",
        "language": "de"
    }
]


# В идеале название endpoint'а
class HiResource(Resource):
    
    def get(self, id=0): 
        if id == 0:
            return random.choice(my_list), 200 
        for val in my_list: 
            if (val["id"] == id): 
                return val, 200
        return "Warning, coun't find text!", 404

    def put(self, id): 
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("language")
        params = parser.parse_args() 
        for val in my_list: 
            if (id == val["id"]): 
                val["text"] = params["text"]
                val["language"] = params["language"]
                return val, 200
        val = {
            "id": id, 
            "text": params["text"], 
            "language": params["language"]
        }
        my_list.append(val)
        return val, 201

    def post(self, id): 
        parser = reqparse.RequestParser()
        parser.add_argument("text")
        parser.add_argument("language")
        params = parser.parse_args() 
        for val in my_list: 
            if (id == val["id"]): 
                return f"This text with id={id} already exists", 400
        val = {
            "id": id, 
            "text": params["text"], 
            "language": params["language"]
        }
        my_list.append(val)
        return val, 201

    def delete(self, id): 
        global my_list 
        my_list = [val for val in my_list if val["id"] != id]
        return f"Record with id={id} was deleted!", 200

    
app = Flask(__name__)
api = Api(app)
api.add_resource(HiResource, "/hi", "/h1/", "/hi/<int:id>")
app.run(debug=True)