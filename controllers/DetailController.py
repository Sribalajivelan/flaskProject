from flask import Blueprint, request, jsonify, make_response

from models.Details import Detail

detail_api = Blueprint('detail_api', __name__)


@detail_api.route('/', methods=['POST'])
def post_data():
    body = request.get_json()
    data = Detail(**body)
    data.save()
    return {
        "message": "data inserted"
    }


@detail_api.route('/', methods=['GET'])
def get_all():
    data = Detail.objects()
    response = make_response(data.to_json(), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@detail_api.route('/<id>', methods=['PUT'])
def update_data(id: str):
    body = request.get_json()
    data = Detail.objects.get_or_404(id=id)
    data.update(**body)
    return jsonify(str(data.id)), 200


@detail_api.route('/<id>', methods=['DELETE'])
def delete_data(id: int):
    data = Detail.objects.get_or_404(id=id)
    data.delete()
    return jsonify(str(data.id)), 200
