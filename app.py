from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Greet(Resource):

    def get(self, name):

        return {"data": name}

    def post(self):

        return {"data": "Posted!"}


api.add_resource(Greet, "/greet/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
