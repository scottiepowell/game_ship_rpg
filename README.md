# Ship RPG (Desktop)

## Overview  
This is a sci-fi RPG that takes place aboard a spaceship. Built with Kivy (desktop only for now) and MongoDB for persistence.

## Project Setup  
```bash
make setup
make run

## CLI Interface  
You can use the CLI tool for diagnostics and admin tasks:

```bash
make setup
make cli
python cli.py checkdb
python cli.py listplayer TestHero
python cli.py levelup TestHero
