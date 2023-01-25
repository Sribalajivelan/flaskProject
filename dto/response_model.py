from flask import make_response
import json


class ResponseModel:
    def __init__(self, code, message, result):
        self.code = code
        self.message = message
        self.result = result

    def to_json_response(self, status_code):
        response = make_response({
            'code': self.code,
            'message': self.message,
            'result': json.loads(self.result)
        }, status_code)
        response.headers["Content-Type"] = "application/json"
        return response
