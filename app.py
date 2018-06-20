from flask import Flask
from flask_restful import Api
from resources.hello import Hello
from resources.imageclassifier import ImageClassifier

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/hello')
api.add_resource(ImageClassifier, '/imageclassifier')

if __name__ == '__main__':
    app.run(port=8080, debug=True)