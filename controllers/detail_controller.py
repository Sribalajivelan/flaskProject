from flask import Blueprint, request

from dao.details import Detail
from dto.response_model import ResponseModel

detail_api = Blueprint('detail_api', __name__)


@detail_api.route('/', methods=['POST'])
def post_data():
    body = request.get_json()
    data = Detail(**body)
    data.save()
    return ResponseModel(1, "Details Added", data.to_json()).to_json_response(200)


@detail_api.route('/', methods=['GET'])
def get_all():
    data = Detail.objects()
    return ResponseModel(1, "Details List", data.to_json()).to_json_response(200)


@detail_api.route('/<id>', methods=['GET'])
def get_one_detail(id: str):
    data = Detail.objects.get_or_404(id=id)
    return ResponseModel(1, "Details", data.to_json()).to_json_response(200)


@detail_api.route('/<id>', methods=['PUT'])
def update_data(id: str):
    body = request.get_json()
    data = Detail.objects.get_or_404(id=id)
    data.update(**body)
    return get_one_detail(id)


@detail_api.route('/<id>', methods=['DELETE'])
def delete_data(id: int):
    data = Detail.objects.get_or_404(id=id)
    data.delete()
    return ResponseModel(1, "Detail Deleted", data.to_json()).to_json_response(200)
