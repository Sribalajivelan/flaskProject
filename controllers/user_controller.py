from flask import jsonify, Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required

from dao.users import User
from dto.response_model import ResponseModel

user_api = Blueprint('user_api', __name__)


@user_api.route('/', methods=['POST'])
def create_user():
    users = User.objects(email="sribalajivelan@gmail.com").first()
    if not users:
        users = User(name='Balaji', email='sribalajivelan@gmail.com').save()
    return ResponseModel(1, "User Added", users.to_json()).to_json_response(200)


@user_api.route('/login', methods=['POST'])
def login():
    request_body = request.get_json()
    users = User.objects(email=request_body['email']).first()
    if not users:
        return jsonify({'msg': 'Username Not Found'}), 404
    access_token = create_access_token(identity=request_body['email'])  # create jwt token
    result = {
        'id': users.id.__str__(),
        'email': users.email,
        'access_token': access_token
    }
    return ResponseModel(1, "Login Details", result).to_jsonify_response(200)


@user_api.route("/email/<string:email>", methods=['GET'])
@jwt_required()
def get_user_by_id(email):
    users = User.objects(email=email).first()
    if not users:
        return jsonify({'msg': 'Username Not Found'}), 404
    return ResponseModel(1, "User", users.to_json()).to_json_response(200)

