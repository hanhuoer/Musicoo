"""
-------------------------------------------------
   File Name    :   MusicooApi.py
   Description  :   Web Api
   Author       :   H
   Date         :   2019/12/1
-------------------------------------------------
"""

import platform

from flask import Flask

from common.Response import Response
from config.Getter import config
from service.MusicooService import MusicooService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'index'


@app.route('/netease/song/<song_id>/url', methods=['GET'])
def song_url(song_id):
    """
    获取音乐链接
        /netease/song/1379444316/url
    :param song_id:
    :return:
    """
    if song_id is None or song_id is '' or len(song_id) is 0:
        return Response.error(song_id, message='song_id can not be null.')
    if song_id.isdigit() is False:
        return Response.error(song_id, message='song_id must be digit.')

    return Response.success(MusicooService.song_url(song_id).to_json())


@app.route('/netease/song/<song_id>/lyric', methods=['GET'])
def song_lyric(song_id):
    """
    获取音乐歌词
        /netease/song/1379444316/lyric
    :param song_id:
    :return:
    """
    if song_id is None or song_id is '' or len(song_id) is 0:
        return Response.error(song_id, message='song_id can not be null.')
    if song_id.isdigit() is False:
        return Response.error(song_id, message='song_id must be digit.')

    return Response.success(MusicooService.song_lyric(song_id).to_json())


@app.route('/netease/song/<keyword>/search', methods=['GET'])
def song_search(keyword):
    """
    搜索音乐
        /netease/song/keyword/search
    :return:
    """
    if keyword is None or keyword is '' or len(keyword) is 0:
        return Response.error(keyword, message='keyword can not be null.')

    return Response.success(MusicooService.song_search(keyword).to_json())


@app.route('/netease/song/<song_id>/detail')
def song_detail(song_id=''):
    """
    获取音乐详情
        /netease/song/1379444316/detail
    :param song_id: eg 1379444316
    :return:
    """
    if song_id is None or song_id is '' or len(song_id) is 0:
        return Response.error(song_id, message='song_id can not be null.')
    if song_id.isdigit() is False:
        return Response.error(song_id, message='song_id must be digit.')

    return Response.success(MusicooService.song_detail(song_id).to_json())


@app.route('/netease/song/<keyword>', methods=['GET'])
def song(keyword):
    """
    url，歌词，detail
        /netease/song/1379444316
        /netease/song/差不多姑娘
    :param keyword:
    :return:
    """
    if keyword is None or keyword is '' or len(keyword) is 0:
        return Response.error(keyword, message='keyword can not be null.')

    return Response.success(MusicooService.song(keyword).to_json())


"""
------------------------------------------------------------------------------------------------------------------------
>                                                                                                                      <
>                                                   The start                                                          <
>                                                                                                                      <
👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
"""

if platform.system() != "Windows":
    import gunicorn.app.base
    from gunicorn.six import iteritems


    class StandaloneApplication(gunicorn.app.base.BaseApplication):

        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(StandaloneApplication, self).__init__()

        def load_config(self):
            _config = dict([(key, value) for key, value in iteritems(self.options)
                            if key in self.cfg.settings and value is not None])
            for key, value in iteritems(_config):
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application


def run():
    app.run(host=config.host_ip, port=config.host_port)


def run_():
    _options = {
        'bind': '%s:%s' % (config.host_ip, config.host_port),
        'workers': 4,
        'accesslog': '-',
        'access_log_format': '%(h)s %(l)s %(t)s "%(r)s" %(s)s "%(a)s"'
    }
    StandaloneApplication(app, _options).run()


if __name__ == '__main__':
    if platform.system() == "Windows":
        print("Windows")
        run()
    else:
        print("Not Windows")
        run_()
