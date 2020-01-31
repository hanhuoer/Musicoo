"""
-------------------------------------------------
   File Name    :   Api.py
   Description  :   netease api，请求方式，加密方式都在这里
   Author       :   H
   Date         :   2019/11/30
-------------------------------------------------
"""

import json

import requests

import netease.Encrypt as netease
from util.LogHandler import LogHandler

BASE_URL = "http://music.163.com"
DEFAULT_TIMEOUT = 10

POST = "POST"
GET = "GET"


class NetEase(object):

    def __init__(self):
        """
        构造默认 header request session
        """
        self.header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "music.163.com",
            "Referer": "http://music.163.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        self.session = requests.session()
        self.log = LogHandler('NeteaseApi')

    def _raw_request(self, method, url, data=None):
        """
        实际发起请求方法
        :param method: POST | GET
        :param url: url
        :param data: 请求携带的数据
        :return: response
        """
        if method == "GET":
            response = self.session.get(
                url, params=data, headers=self.header, timeout=DEFAULT_TIMEOUT
            )
        elif method == "POST":
            response = self.session.post(
                url, data=data, headers=self.header, timeout=DEFAULT_TIMEOUT
            )
        return response

    def _get_form_data(self, encrypt_data):
        """
        获取加密后的 form data 参数
        :param encrypt_data: 待加密的参数
        :return: 加密后的参数 {"params":"", "encSecKey":""}
        """
        key = netease.create_key(16)
        return {
            "params": netease.aes(netease.aes(encrypt_data, netease.NONCE), key),
            "encSecKey": netease.rsa(key, netease.PUBKEY, netease.MODULUS)
        }

    def request(self, method, path, data={}, default={"code": -1}):
        """
        统一请求方法
        :param method: POST | GET
        :param path: 路径
        :param data: 未加密的 data
        :param default: 默认的 response
        :return: response
        """
        url = "{}{}".format(BASE_URL, path)
        response = default
        csrf_token = ""

        data.update({"csrf_token": csrf_token})
        params = self._get_form_data(json.dumps(data).encode('utf-8'))
        try:
            self.log.debug('[Netease api] url: {};\trequest  data: {};\tparams: {}'.format(url, data, params))
            response = self._raw_request(method, url, params)
            response = response.json()
            self.log.debug('[Netease api] url: {};\tresponse data: {}'.format(url, response))
        except requests.exceptions.RequestException as e:
            self.log.error('[Netease api] request error: {}'.format(e))
        except ValueError as e:
            self.log.error("[Netease api] request error; Path: {}, response: {}".format(path, response.text[:200]))
        finally:
            return response

    def songs_url(self, song_id):
        """
        获取音乐的实际 url，外链
            {ids: "[514235010]", level: "standard", encodeType: "aac", csrf_token: ""}
        :param song_id: 音乐 id
        :return: 带有外链的 json 串
        """
        path = "/weapi/song/enhance/player/url/v1?csrf_token="
        params = {
            'ids': '[' + str(song_id) + ']',
            'level': 'standard',
            'encodeType': 'aac',
            'csrf_token': ''
        }
        return self.request(POST, path, params)

    def songs_lyric(self, song_id):
        """
        获取音乐歌词
            {id: "186453", lv: -1, tv: -1, csrf_token: ""}
        :param song_id:
        :return:
        """
        path = "/weapi/song/lyric?csrf_token="
        params = {
            'id': str(song_id),
            'lv': -1,
            'tv': -1,
            'csrf_token': ''
        }
        return self.request(POST, path, params)

    def songs_search(self, keyword, offset=0, limit=30):
        """
        搜索音乐
            按照关键字搜索一般就用这个
            {hlpretag: "<span class="s-fc7">", hlposttag: "</span>", s: "春夏秋冬 张国荣", type: "1", offset: "0", …}
        :return:
        """
        path = '/weapi/cloudsearch/get/web?csrf_token='
        params = {
            'csrf_token': '',
            'hlposttag': '</span>',
            'hlpretag': '<span class="s-fc7">',
            'limit': str(limit),
            'offset': str(offset),
            's': str(keyword),
            'total': 'true',
            'type': '1'
        }
        return self.request(POST, path, params)

    def songs_search_(self, song):
        """
        搜索音乐，搜索框联动接口，不常用
            {s: "春夏秋冬", limit: "8", csrf_token: ""}
        :return:
        """
        path = "/weapi/search/suggest/web?csrf_token="
        params = {
            's': str(song),
            'limit': 8,
            'csrf_token': ''
        }
        return self.request(POST, path, params)

    def songs_detail(self, song_id):
        """
        获取歌曲详情
            给定 song id
            {id: "186453", c: "[{"id":"186453"}]", csrf_token: ""}
        :param song_id: 必传参数，song id
        :return: Song
        """
        path = "/weapi/v3/song/detail?csrf_token="
        params = {
            'id': str(song_id),
            'c': "[{'id': " + str(song_id) + "}]",
            'csrf_token': ''
        }
        return self.request(POST, path, params)

    def playlist_detail(self, playlist_id):
        """
        获取歌单详情
        :param playlist_id: 歌单 id
        :return: json
        """
        path = "/weapi/playlist/detail"
        params = {
            'id': str(playlist_id),
            'ids': "[" + str(playlist_id) + "]",
            'limit': 10000,
            'offset': 0,
            'csrf_token': ''
        }
        return self.request(POST, path, params)


"""
------------------------------------------------------------------------------------------------------------------------
>                                                                                                                      <
>                                                   The test case                                                      <
>                                                                                                                      <
👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
"""


def start():
    pass


if __name__ == '__main__':
    start()
