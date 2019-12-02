"""
------------------------------------------------------------------------------------------------------------------------
>                                                                                                                      <
>                                                   The test case                                                      <
>                                                                                                                      <
👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
"""

from model.Song import Song
from resolve.NeteaseResolver import NeteaseResolver

SONG_URL_RESULT = {
    'data': [{
        'id': 36270426,
        'url': 'http://m801.music.126.net/20191202003049/ea0c355e919bd40caac1546f8f782cf9/jdyyaac/0358/0709/5352/421539417c0cc8347406d8c3f0391dfd.m4a',
        'br': 96000,
        'size': 2989749,
        'md5': '421539417c0cc8347406d8c3f0391dfd',
        'code': 200,
        'expi': 1200,
        'type': 'm4a',
        'gain': 0.0,
        'fee': 8,
        'uf': None,
        'payed': 0,
        'flag': 0,
        'canExtend': False,
        'freeTrialInfo': None,
        'level': 'standard',
        'encodeType': 'aac'
    }],
    'code': 200
}

SONG_LYRICS_RESULT = {
    'sgc': False,
    'sfy': False,
    'qfy': False,
    'lyricUser': {
        'id': 186453,
        'status': 99,
        'demand': 0,
        'userid': 404241265,
        'nickname': 'Monica12956',
        'uptime': 1499330955480
    },
    'lrc': {
        'version': 10,
        'lyric': '[by:Monica12956]\n[00:00.000] 作曲 : 叶良俊\n[00:01.000] 作词 : 林振强\n[00:06.00]编曲:陈伟文\n[00:14.00]秋天该很好 你若尚在场\n[00:22.00]秋风即使带凉 亦漂亮\n[00:29.00]深秋中的你填密我梦想\n[00:36.00]就像落叶飞 轻敲我窗\n[00:43.00]冬天该很好 你若尚在场\n[00:50.00]天空多灰 我们亦放亮\n[00:57.00]一起坐坐谈谈来日动向\n[01:04.00]漠视外间低温 这样唱\n[02:27.00][01:10.00]能同途偶遇在这星球上\n[02:33.00][01:16.00]燃亮飘渺人生\n[02:37.00][01:20.00]我多么够运\n[02:41.00][01:24.00]无人如你逗留我思潮上\n[02:47.00][01:30.00]从没再疑问\n[02:50.00][01:34.00]这个世界好得很\n[01:40.00]暑天该很好 你若尚在场\n[01:46.00]火一般的太阳在脸上\n[01:53.00]烧得肌肤如情 痕极又痒\n[02:00.00]滴着汗的一双 笑着唱\n[02:55.00]能同途偶遇在这星球上\n[03:02.00]是某种缘份\n[03:06.00]我多么庆幸\n[03:09.00]如离别 你亦长处心灵上\n[03:15.00]宁愿有遗憾\n[03:19.00]亦愿和你远亦近\n[03:25.00]春天该很好 你若尚 在场\n[03:32.00]春风仿佛爱情\n[03:35.00]在蕴酝\n[03:39.00]初春中的你 撩动我幻想\n[03:46.00]就像嫩绿草使\n[03:52.00]春雨香\n'
    },
    'tlyric': {
        'version': 0
    },
    'code': 200
}

SONG_SEARCH_RESULT = {
    'result': {
        'songs': [{
            'name': '春夏秋冬',
            'id': 186453,
            'pst': 0,
            't': 0,
            'ar': [{
                'id': 6457,
                'name': '张国荣',
                'tns': [],
                'alias': []
            }],
            'alia': [],
            'pop': 100.0,
            'st': 0,
            'rt': '',
            'fee': 8,
            'v': 208,
            'crbt': None,
            'cf': '',
            'al': {
                'id': 18937,
                'name': 'I Am What I Am',
                'picUrl': 'http://p2.music.126.net/2YIpNoCzXfYgz4zIw3s0Vg==/73667279073787.jpg',
                'tns': [],
                'pic': 73667279073787
            },
            'dt': 250586,
            'h': {
                'br': 320000,
                'fid': 0,
                'size': 10025839,
                'vd': 7200.0
            },
            'm': {
                'br': 192000,
                'fid': 0,
                'size': 6015520,
                'vd': 9700.0
            },
            'l': {
                'br': 128000,
                'fid': 0,
                'size': 4010361,
                'vd': 11399.0
            },
            'a': None,
            'cd': '1',
            'no': 13,
            'rtUrl': None,
            'ftype': 0,
            'rtUrls': [],
            'djId': 0,
            'copyright': 1,
            's_id': 0,
            'mark': 8192,
            'rtype': 0,
            'rurl': None,
            'mst': 9,
            'cp': 7003,
            'mv': 5570704,
            'publishTime': 1269273600000,
            'privilege': {
                'id': 186453,
                'fee': 8,
                'payed': 0,
                'st': 0,
                'pl': 128000,
                'dl': 0,
                'sp': 7,
                'cp': 1,
                'subp': 1,
                'cs': False,
                'maxbr': 999000,
                'fl': 128000,
                'toast': False,
                'flag': 4
            }
        }],
        'songCount': '600'
    },
    'code': '200'
}

SONG_DETAIL_RESULT = a = {
    'songs': [{
        'name': '差不多姑娘',
        'id': 1379444316,
        'pst': 0,
        't': 0,
        'ar': [{
            'id': 7763,
            'name': 'G.E.M.邓紫棋',
            'tns': [],
            'alias': []
        }],
        'alia': [],
        'pop': 100.0,
        'st': 0,
        'rt': '',
        'fee': 0,
        'v': 7,
        'crbt': None,
        'cf': '',
        'al': {
            'id': 80536158,
            'name': '差不多姑娘',
            'picUrl': 'http://p1.music.126.net/9K3XB_8nwqQwbWdt-Suj-w==/109951164231366714.jpg',
            'tns': [],
            'pic_str': '109951164231366714',
            'pic': 109951164231366714
        },
        'dt': 230008,
        'h': {
            'br': 320000,
            'fid': 0,
            'size': 9202460,
            'vd': -39996.0
        },
        'm': {
            'br': 192000,
            'fid': 0,
            'size': 5521493,
            'vd': -37471.0
        },
        'l': {
            'br': 128000,
            'fid': 0,
            'size': 3681010,
            'vd': -35861.0
        },
        'a': None,
        'cd': '01',
        'no': 1,
        'rtUrl': None,
        'ftype': 0,
        'rtUrls': [],
        'djId': 0,
        'copyright': 0,
        's_id': 0,
        'mark': 16,
        'mst': 9,
        'cp': 1416446,
        'mv': 10880291,
        'rtype': 0,
        'rurl': None,
        'publishTime': 0
    }],
    'privileges': [{
        'id': 1379444316,
        'fee': 0,
        'payed': 0,
        'st': 0,
        'pl': 320000,
        'dl': 0,
        'sp': 7,
        'cp': 1,
        'subp': 1,
        'cs': False,
        'maxbr': 320000,
        'fl': 999000,
        'toast': False,
        'flag': 0,
        'preSell': False
    }],
    'code': 200
}


def test_song_url_resolver(song=Song()):
    resolver = NeteaseResolver.song_url_resolver(song, SONG_URL_RESULT)
    print(resolver.to_string())
    return resolver


def test_song_lyric_resolver(song=Song()):
    resolver = NeteaseResolver.song_lyric_resolver(song, SONG_LYRICS_RESULT)
    print(resolver.to_string())
    return resolver


def test_song_search_resolver(song=Song()):
    resolver = NeteaseResolver.song_search_resolver(song, SONG_SEARCH_RESULT)
    print(resolver.to_string())
    return resolver


def test_song_detail_resolver(song=Song()):
    resolver = NeteaseResolver.song_detail_resolver(song, SONG_DETAIL_RESULT)
    print(resolver.to_string())
    return resolver


def start():
    song = Song()
    song = test_song_search_resolver(song)
    song = test_song_url_resolver(song)
    song = test_song_lyric_resolver(song)
    song = test_song_detail_resolver(song)
    print(song.to_string())


if __name__ == '__main__':
    start()
