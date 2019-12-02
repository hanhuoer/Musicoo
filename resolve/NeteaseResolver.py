"""
-------------------------------------------------
   File Name    :   NeteaseResolver.py
   Description  :   netease api 解析
   Author       :   H
   Date         :   2019/12/2
-------------------------------------------------
"""

from model.Album import Album
from model.Song import Song


class NeteaseResolver(object):
    """netease 解析器"""

    def __init__(self):
        pass

    @staticmethod
    def song_url_resolver(song=Song(), json={}):
        """
        解析 netease 歌曲 api 的响应结果
            解析目标：音乐 id，音乐 url
        :param song: 解析结果
        :param json: netease api 响应 json 串
        :return: Song
        """
        json = json.get('data')

        if isinstance(json, list) and len(json) < 1:
            return song

        if isinstance(json, list) and len(json) > 0:
            json = json[0]

        song.set_id(json.get('id'))
        song.set_url(json.get('url'))
        return song

    @staticmethod
    def song_lyric_resolver(song=Song(), json={}):
        """
        解析 netease 歌词 api 的响应结果
            可以拿到：原生歌词信息
        :param song: 解析结果
        :param json: netease api 响应 json 串
        :return: Song
        """
        json = json.get('lrc')
        song.set_lyric(json.get('lyric'))
        return song

    @staticmethod
    def song_search_resolver(song=Song(), json={}):
        """
        解析音乐的搜索结果
            重点拿到 id 就好了，其余的交给 detail 去解析
        :param song:
        :param json:
        :return:
        """
        json = json.get('result')
        json = json.get('songs')
        if isinstance(json, list) and len(json) > 0:
            json = json[0]

        song.set_id(json.get('id'))
        return song

    @staticmethod
    def song_detail_resolver(song=Song(), json={}):
        """
        解析歌曲详情
            这里可以拿到：音乐名，音乐id，音乐时长，艺人，专辑名，专辑图片，专辑id
        :param song:
        :param json:
        :return:
        """
        json = json.get('songs')

        if isinstance(json, list) and len(json) > 0:
            json = json[0]

        album_json = json.get('al')
        artist_json = json.get('ar')
        if isinstance(artist_json, list) and len(artist_json) > 0:
            artist_json = artist_json[0]

        song.set_name(json.get('name'))
        song.set_id(json.get('id'))
        song.set_duration(json.get('dt'))
        song.set_picture_url(album_json.get('picUrl'))
        song.set_artist(artist_json.get('name'))

        album = Album()
        album.set_id(album_json.get('id'))
        album.set_name(album_json.get('name'))
        album.set_artist(artist_json.get('name'))
        album.set_picture_url(album_json.get('picUrl'))
        song.set_album(album)

        return song
