# This is a tool for developers to improve their Git Workflow
# Introducing .......... Gutter
# A TUI for developers 

import click
from pyfiglet import Figlet  # You need to install this library using: pip install pyfiglet

# Function to create a big text UI
def print_big_text(text, font='standard'):
    fig = Figlet(font=font)
    click.echo(fig.renderText(text))


@click.group()
def cli():
    """My Beautiful CLI"""


@cli.command()
@click.option('--name', default='World', help='Name to greet')
def hello(name):
    """Say hello."""
    greeting = f"Hello, {name}!"
    styled_greeting = click.style(greeting, fg='green', bold=True)
    click.echo(styled_greeting)

@cli.command()
def goodbye():
    """Say goodbye."""
    click.echo("Goodbye, cruel world!")

@cli.command()
@click.argument('text')
@click.option('--font', default='slant', help='Font style for big text UI')
def bigtext(text, font):
    """Create a big text UI."""
    print_big_text(text, font)

if __name__ == '__main__':
    cli()