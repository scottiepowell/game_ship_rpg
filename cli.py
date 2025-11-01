import click
from src.game.db import check_connection
from src.game.models import Player

@click.group()
def cli():
    """Ship RPG CLI – administration and diagnostics."""
    pass

@cli.command()
def checkdb():
    """Check database connectivity."""
    if check_connection():
        click.echo("✅ Database reachable.")
    else:
        click.echo("❌ Failed to reach database.", err=True)

@cli.command()
@click.argument('name')
def listplayer(name):
    """List basic info of a player by name."""
    player = Player.find_one({"name": name})
    if player:
        click.echo(f"Player {player.name}: Level {player.level}, Exp {player.experience}")
    else:
        click.echo(f"No player found with name '{name}'", err=True)

@cli.command()
@click.argument('name')
def levelup(name):
    """Force level up a player."""
    player = Player.find_one({"name": name})
    if player:
        player.level_up()
        click.echo(f"Player {player.name} is now Level {player.level}, Exp {player.experience}")
    else:
        click.echo(f"No player found with name '{name}'", err=True)

if __name__ == "__main__":
    cli()