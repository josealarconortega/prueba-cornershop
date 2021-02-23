import json
class Response:
    def __init__(self, code, status, message, data) -> None:
        self.code = code
        self.status = status
        self.message = message
        self.data = data


    def toResponse(self):
        return json.dumps({
            'code': self.code,
            'status': self.status,
            'message': self.message,
            'data': self.dat
        })

