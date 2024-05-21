from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video", required=True)
video_put_args.add_argument(
    "views", type=int, help="Number of views of the video", required=True)
video_put_args.add_argument(
    "likes", type=int, help="Number of likes of the video", required=True)

videos = {}


class Video(Resource):
    def get(self, video_id):
        if video_id not in videos:
            return {"message": "Video not found"}, 404
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
