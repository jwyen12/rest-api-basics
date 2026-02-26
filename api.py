from flask import Flask, abort, request, jsonify
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db = SQLAlchemy(app)


class VideoModel(db.Model):
    __tablename__ = "videos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = True)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="Name of video", required=True)
video_post_args.add_argument("views", type=int, help="Views of the video", required=True)
video_post_args.add_argument("likes", type=int, help="Likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of video", required=False)
video_update_args.add_argument("views", type=int, help="Views of the video", required=False)
video_update_args.add_argument("likes", type=int, help="Likes of the video", required=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404)
        return result
    

    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_post_args.parse_args()
        result = VideoModel.query.get(video_id)
        if result:
            abort(409)
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    

    def delete(self, video_id):
        video = VideoModel.query.get(video_id)
        if not video:
            abort(404)
        try:
            db.session.delete(video)
            db.session.commit()
            return 204
        except Exception as e:
            db.session.rollback()
            return 500

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.get(video_id)
        if not result:
            abort(404)
        for column in args:
            if column in resource_fields and args[column] != None:
                setattr(result, column, args[column])
        
        db.session.commit()
        return result

        
api.add_resource(Video, "/video/<string:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
