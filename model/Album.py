import json


class Album(object):
    """
    专辑实体类
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.artist = None
        self.picture_url = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_picture_url(self):
        return self.picture_url

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_artist(self, artist):
        self.artist = artist

    def set_picture_url(self, picture_url):
        self.picture_url = picture_url

    def to_string(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'artist': self.get_artist(),
            'picture_url': self.get_picture_url()
        }, ensure_ascii=False)

    def to_json(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'artist': self.get_artist(),
            'picture_url': self.get_picture_url()
        }

    def dict_to_object(dictObject: dict, object):
        for k, v in dictObject.items():
            object.__dict__[k] = v
        return object