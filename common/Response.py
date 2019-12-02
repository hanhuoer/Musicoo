import json


class Response(object):
    """
    封装 response
    """

    def __init__(self, data, message, code):
        self.data = data
        self.message = message
        self.code = code

    def to_string(self):
        return json.dumps({
            'data': self.data,
            'message': self.message,
            'code': self.code
        }, ensure_ascii=False)

    def to_json(self):
        return {
            'data': self.data,
            'message': self.message,
            'code': self.code
        }

    @staticmethod
    def error(data=None, message='error', code=-1):
        return json.dumps(Response(data, message, code).to_json(), ensure_ascii=False)

    @staticmethod
    def fail(data=None, message='fail', code=0):
        return json.dumps(Response(data, message, code).to_json(), ensure_ascii=False)

    @staticmethod
    def success(data=None, message='success', code=1):
        return json.dumps(Response(data, message, code).to_json(), ensure_ascii=False)
