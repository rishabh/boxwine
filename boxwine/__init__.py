# Copyright (C) 2020 Rishabh Moudgil

import sys
import click
from config import Config, save_example_config


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    """A simple command line tool."""


@cli.command("create", short_help="create a Mac app from a config file")
@click.option(
    "--file",
    type=click.Path(exists=True),
    default="./app.boxwine.yaml",
    help="path to config file",
)
def create(file):
    """
    Create a Mac app from the supplied config file.
    """
    print(file)
    sys.exit(1)


@cli.command("init", short_help="initialize an example config file")
@click.option(
    "--file",
    type=click.Path(),
    default="./app.boxwine.yaml",
    help="path to where you want the example config file",
)
def init(file):
    """
    Initialize an example config file and exit.
    """
    save_example_config(file)
    print(f"Wrote example config file at {file}")


if __name__ == "__main__":
    cli()
