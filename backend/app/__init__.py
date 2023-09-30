from flask import Flask , request , make_response
from config import Config
<<<<<<< HEAD
from app.photo import photo
=======
from app.products import products 
from app.categories import categories
from app.correct import correct
>>>>>>> 5b6ca6f6f03a8bd50c22449ca291b16842183d83
from flask_cors import CORS, cross_origin

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

<<<<<<< HEAD
    blueprints = [photo] #products, categories, correct
=======
    blueprints = [products, categories, correct]
>>>>>>> 5b6ca6f6f03a8bd50c22449ca291b16842183d83
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    
    CORS(app)
    
    @app.after_request
    def after_request_func(response):
        origin = request.headers.get('Origin')
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
            response.headers.add('Access-Control-Allow-Methods',
                                'GET, POST, OPTIONS, PUT, PATCH, DELETE')
            if origin:
                response.headers.add('Access-Control-Allow-Origin', origin)
        else:
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            if origin:
                response.headers.add('Access-Control-Allow-Origin', origin)

        return response
    
    return app


