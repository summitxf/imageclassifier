from flask_restful import Resource

class ImageClassifier(Resource):
    def post(self):
        return {'hello': 'ImageClassifier'}