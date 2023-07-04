#! /usr/bin/env python3
import rich_click as click
from rich.console import Console

console=Console()
CONTEXT_SETTINGS={'help_option_names':['-h','--help']}



@click.group(context_settings=CONTEXT_SETTINGS)
def start_sm():
    pass

@start_sm.command()
def interactive():
    pass




if __name__ == "__main__":
    start_sm()