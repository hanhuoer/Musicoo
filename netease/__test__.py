"""
-------------------------------------------------
   File Name    :   __test__.py
   Description  :   Api.py 的测试用例
   Author       :   H
   Date         :   2019/12/1
-------------------------------------------------
"""

import math
import random
import time

from netease.Api import NetEase
from netease.Setting import *

SONGS_ID = SONGS_ID
SONG_NAME = SONG_NAME


def test_song_url():
    netease = NetEase()
    for i in SONGS_ID:
        response = netease.songs_url(i)
        if response.get('code') is not None and response.get('code') is -1:
            print('error')
            break
        random_number = math.floor(random.random() * 5) + 1
        print('第 {} 首音乐，代码 {}，休眠 {} 秒钟后继续，response {}'.format(SONGS_ID.index(i) + 1, i, random_number, response))
        time.sleep(random_number)


def test_song_lyric(SONGS_ID=['186453', '316686']):
    netease = NetEase()
    for i in SONGS_ID:
        response = netease.songs_lyric(i)
        if response.get('code') is not None and response.get('code') is -1:
            print('error')
            break
        random_number = math.floor(random.random() * 5) + 1
        print('第 {} 首音乐，代码 {}，休眠 {} 秒钟后继续，response {}'.format(SONGS_ID.index(i) + 1, i, random_number, response))
        time.sleep(random_number)


def test_song_search():
    netease = NetEase()
    for i in SONG_NAME:
        response = netease.songs_search(i)
        if response.get('code') is not None and response.get('code') is -1:
            print('error')
            break
        random_number = math.floor(random.random() * 5) + 1
        print('第 {} 首音乐，代码 {}，休眠 {} 秒钟后继续，response {}'.format(SONG_NAME.index(i) + 1, i, random_number, response))
        time.sleep(random_number)


def test_songs_detail():
    netease = NetEase()
    response = netease.songs_detail('1379444316')
    print(response)


def start():
    # test_song_url()
    test_song_lyric(['1379444316'])
    # test_song_search()
    # test_songs_detail()


if __name__ == '__main__':
    start()
