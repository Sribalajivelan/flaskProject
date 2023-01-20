from flask import jsonify, Blueprint, Response, json

from models.Users import User

user_api = Blueprint('user_api', __name__)


@user_api.route('/', methods=['POST'])
def create_user():
    users = User.objects(email= "sribalajivelan@gmail.com").first()
    if not users:
        users = User(name='Balaji', email='sribalajivelan@gmail.com').save()
    return jsonify({'name' : users.name})
