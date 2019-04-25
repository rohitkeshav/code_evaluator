from flask import Flask, jsonify
from flask_restful import Resource, Api


# instantiate flask app
app = Flask(__name__)

api = Api(app)

# set config
app.config.from_object('project.config.DevelopmentConfig')  # new


class UserPings(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(UserPings, '/users/ping')
