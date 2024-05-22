from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
api = Api(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)


class VideoModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Video(name = {name} , views = {views} , likes = {likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video", required=True)
video_put_args.add_argument(
    "views", type=int, help="Number of views of the video", required=True)
video_put_args.add_argument(
    "likes", type=int, help="Number of likes of the video", required=True)

videos = {}


def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, "Video already exists with this ID...")


def abort_if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, "Could not find video...")


class Video(Resource):
    def get(self, video_id):
        if video_id not in videos:
            return {"message": "Video not found"}, 404
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id=video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_doesnt_exist(video_id=video_id)
        del videos[video_id]
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
