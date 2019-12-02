import platform
import sys

import click

sys.path.append('../')

from api.MusicooApi import run, run_
from config.Setting import BANNER

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='2.0.0')
def cli():
    """Musicoo tool"""


@cli.command(name="run")
def schedule():
    """start the web server"""
    click.echo(BANNER)
    if platform.system() == "Windows":
        run()
    else:
        run_()


if __name__ == '__main__':
    cli()
