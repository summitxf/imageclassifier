from flask_restful import request, reqparse, Resource
from resources.doclassify import do_classify

class ImageClassifier(Resource):
    def post(self):
        
        imgbase64 = request.json.get('imgbase64')
        result = do_classify(imgbase64)
        print(result)
        return result
        