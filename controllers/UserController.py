from flask import jsonify, Blueprint, request, make_response
from flask_jwt_extended import create_access_token, jwt_required

from models.Users import User

user_api = Blueprint('user_api', __name__)


@user_api.route('/', methods=['POST'])
def create_user():
    users = User.objects(email="sribalajivelan@gmail.com").first()
    if not users:
        users = User(name='Balaji', email='sribalajivelan@gmail.com').save()
    return jsonify({'name': users.name})


@user_api.route('/login', methods=['POST'])
def login():
    request_body = request.get_json()
    users = User.objects(email=request_body['email']).first()
    if not users:
        return jsonify({'msg': 'Username Not Found'}), 404
    access_token = create_access_token(identity=request_body['email'])  # create jwt token
    return make_response(jsonify(access_token=access_token), 200)


@user_api.route("/email/<string:email>", methods=['GET'])
@jwt_required()
def get_user_by_id(email):
    users = User.objects(email=email).first()
    if not users:
        return jsonify({'msg': 'Username Not Found'}), 404
    response = make_response(users.to_json(), 200)
    response.headers["Content-Type"] = "application/json"
    return response

