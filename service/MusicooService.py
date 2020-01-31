"""
-------------------------------------------------
   File Name    :   MusicooService.py
   Description  :   接口业务具体处理
   Author       :   H
   Date         :   2019/12/2
-------------------------------------------------
"""

from model.Song import Song
from netease.Api import NetEase
from resolve.NeteaseResolver import NeteaseResolver


class MusicooService(object):

    @staticmethod
    def song_url(song_id, song=Song()):
        """
        song url service
            获取音乐链接
            https://github.com/hanhuoer/Musicoo/wiki/web-api#1-%E8%8E%B7%E5%8F%96%E9%9F%B3%E4%B9%90%E9%93%BE%E6%8E%A5
        :param song_id:
        :param song:
        :return:
        """
        netease = NetEase()
        result = netease.songs_url(str(song_id))
        song = NeteaseResolver.song_url_resolver(song, result)
        return song

    @staticmethod
    def song_lyric(song_id, song=Song()):
        """
        song lyric service
            获取歌词
            https://github.com/hanhuoer/Musicoo/wiki/web-api#2-%E6%AD%8C%E8%AF%8D
        :param song_id:
        :param song:
        :return:
        """
        netease = NetEase()
        result = netease.songs_lyric(str(song_id))
        song = NeteaseResolver.song_lyric_resolver(song, result)
        song.set_id(song_id)
        return song

    @staticmethod
    def song_search(keyword, song=Song()):
        """
        song search service
            搜索音乐
            https://github.com/hanhuoer/Musicoo/wiki/web-api#3-%E9%9F%B3%E4%B9%90%E8%AF%A6%E6%83%85
        :param keyword:
        :param song:
        :return:
        """
        netease = NetEase()
        result = netease.songs_search(keyword)
        song = NeteaseResolver.song_search_resolver(song, result)
        return song

    @staticmethod
    def songs_search(keyword, offset=0, limit=30):
        """
        songs search service
            搜索音乐
            https://github.com/hanhuoer/Musicoo/wiki/web-api#3-%E9%9F%B3%E4%B9%90%E8%AF%A6%E6%83%85
        :param limit:
        :param offset:
        :param keyword:
        :param song:
        :return:
        """

        netease = NetEase()
        result = netease.songs_search(keyword, offset=offset, limit=limit)
        return NeteaseResolver.songs_search_resolver(result)

    @staticmethod
    def song_detail(song_id, song=Song()):
        """
        song detail service
            获取音乐信息
            https://github.com/hanhuoer/Musicoo/wiki/web-api#4-%E9%9F%B3%E4%B9%90%E6%90%9C%E7%B4%A2
        :param song_id:
        :param song: [optional]
        :return:
        """
        netease = NetEase()
        result = netease.songs_detail(song_id)
        song = NeteaseResolver.song_detail_resolver(song, result)
        return song

    @staticmethod
    def song(keyword, song=Song()):
        """
        song service
            获取音乐
            https://github.com/hanhuoer/Musicoo/wiki/web-api#5-%E8%8E%B7%E5%8F%96%E9%9F%B3%E4%B9%90
        :param keyword: 关键字
        :param song: [optional]
        :return:
        """
        search_results = MusicooService.songs_search(keyword, 0, 10)
        if search_results.get('count') > 0:
            song = Song.dict_to_object(search_results.get('data')[0], Song())
            song = MusicooService.song_url(song.get_id(), song)
            song = MusicooService.song_lyric(song.get_id(), song)
            song = MusicooService.song_detail(song.get_id(), song)
        else:
            pass
        return song

    @staticmethod
    def playlist_songs(playlist_id):
        """
        playlist songs
            获取歌单音乐列表
        :param playlist_id: 歌单 id
        :return: See: Playlist.py
        """

        netease = NetEase()
        result = netease.playlist_detail(playlist_id)
        return NeteaseResolver.playlist_songs_resolver(result)
