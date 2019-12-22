import json

from model.Album import Album
from model.Privilege import Privilege


class Song(object):
    """
    音乐实体类，存放音乐信息
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.url = None
        self.duration = None
        self.lyric = None
        self.picture_url = None
        self.artist = None
        self.album = Album()
        self.privilege = Privilege()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_duration(self):
        return self.duration

    def get_lyric(self):
        return self.lyric

    def get_picture_url(self):
        return self.picture_url

    def get_artist(self):
        return self.artist

    def get_album(self):
        return self.album

    def get_privilege(self):
        return self.privilege

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_url(self, url):
        self.url = url

    def set_duration(self, duration):
        self.duration = duration

    def set_lyric(self, lyric):
        self.lyric = lyric

    def set_picture_url(self, picture_url):
        self.picture_url = picture_url

    def set_artist(self, artist):
        self.artist = artist

    def set_album(self, album):
        self.album = album

    def set_privilege(self, privilege):
        self.privilege = privilege

    def to_string(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'artist': self.get_artist(),
            'url': self.get_url(),
            'duration': self.get_duration(),
            'lyric': self.get_lyric(),
            'picture_url': self.get_picture_url(),
            'album': self.get_album().to_string(),
            'privilege': self.get_privilege().to_string()
        }, ensure_ascii=False)

    def to_json(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'artist': self.get_artist(),
            'url': self.get_url(),
            'duration': self.get_duration(),
            'lyric': self.get_lyric(),
            'picture_url': self.get_picture_url(),
            'album': self.get_album().to_json(),
            'privilege': self.get_privilege().to_json()
        }

    def dict_to_object(dictObject: dict, object):
        for k, v in dictObject.items():
            if k is 'album':
                object.__dict__[k] = Album.dict_to_object(v, Album())
            elif k is 'privilege':
                object.__dict__[k] = Privilege.dict_to_object(v, Privilege())
            else:
                object.__dict__[k] = v
        return object
