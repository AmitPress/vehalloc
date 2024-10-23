from fastapi import Response
from bson import json_util


def build_response(data, status_code=200):
    response = Response(content=json_util.dumps(data), status_code=status_code)
    return response