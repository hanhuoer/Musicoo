class NeteaseResolverException(Exception):
    """
    NeteaseResolverException
    """

    def __init__(self, *args):
        self.args = args


if __name__ == '__main__':
    try:
        raise NeteaseResolverException('e')
    except NeteaseResolverException as e:
        print(e)
