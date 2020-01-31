import json


class Playlist(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.tracks = []

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_tracks(self, tracks):
        self.tracks = tracks

    def get_tracks(self):
        return self.tracks

    def to_string(self):
        return json.dumps({
            'id': self.get_id(),
            'name': self.get_name(),
            'tracks': self.get_tracks(),
        }, ensure_ascii=False)

    def to_json(self):
        return {
            'id': self.get_id(),
            'name': self.get_name(),
            'tracks': self.get_tracks(),
        }


def generate_setter_getter():
    playlist = Playlist()
    print(playlist.__dict__)
    for k in playlist.__dict__:
        print("def set_" + k + "(self," + k + "):")
        print("\tself." + k, "=" + k)
        print("def get_" + k + "(self):")
        print("\treturn self." + k)


def generate_to_string():
    playlist = Playlist()
    print(playlist.__dict__)
    result = 'def to_string(self):\n'
    result += '\treturn json.dumps({\n'
    for k in playlist.__dict__:
        result += "\t\t'" + k + "'" + ":" + " self.get_" + k + "(),\n"
    result += "\t}, ensure_ascii=False)"
    print(result)


def generate_to_json():
    playlist = Playlist()
    print(playlist.__dict__)
    result = 'def to_json(self):\n'
    result += '\treturn {\n'
    for k in playlist.__dict__:
        result += "\t\t'" + k + "'" + ":" + " self.get_" + k + "(),\n"
    result += "\t}"
    print(result)


def test_dict_to_object():
    playlist_dict = {'id': 514235010, 'fee': 4, 'payed': 5, 'st': 0, 'pl': 999000, 'dl': 999000, 'sp': 7, 'cp': 1,
                     'subp': 1, 'cs': False, 'maxbr': 999000, 'fl': 0, 'toast': False, 'flag': 0}
    playlist = Playlist.dict_to_object(playlist_dict, Playlist())
    print(playlist.to_json())
    print(playlist.to_string())


if __name__ == '__main__':
    generate_setter_getter()
    generate_to_string()
    generate_to_json()
    # test_dict_to_object()
