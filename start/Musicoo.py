import platform
import sys

import click

sys.path.append('../')

from api.MusicooApi import run, run_
from config.Setting import BANNER
from config.Getter import ConfigGetter

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='2.0.0')
def cli():
    """Musicoo tool"""


@cli.command(name="run")
@click.option('--host', default=None, help='Number of greetings.')
@click.option('--port', default=None, help='Number of greetings.')
def server(host, port):
    """start the web server"""
    print(host, port)
    click.echo(BANNER)
    if platform.system() == "Windows":
        run(host, port)
    else:
        run_(host, port)


if __name__ == '__main__':
    cli()
