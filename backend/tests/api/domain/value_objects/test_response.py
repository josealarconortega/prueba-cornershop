import typing

from api.domain.value_objects import (
    Response
)

import json

def create_response() -> Response:
    return Response(code = 1, status = 200, message = "test", data = [])

def test_toJSON():
    response = create_response()
    assert isinstance(json.loads(response.toResponse()), dict)