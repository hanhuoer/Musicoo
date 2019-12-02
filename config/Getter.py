from config.Setting import *
from util.ClassUtils import LazyProperty


class ConfigGetter(object):
    """
    config getter
    """

    def __init__(self):
        pass

    @LazyProperty
    def host_ip(self):
        return WEB_SERVER.get("HOST", "127.0.0.1")

    @LazyProperty
    def host_port(self):
        return WEB_SERVER.get("PORT", "8888")


config = ConfigGetter()

if __name__ == '__main__':
    print(config.host_ip)
    print(config.host_port)
