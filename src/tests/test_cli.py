from click.testing import CliRunner
import pytest
from cli import cli

@pytest.fixture
def runner():
    return CliRunner()

def test_checkdb_command(runner):
    result = runner.invoke(cli, ['checkdb'])
    assert result.exit_code == 0
    assert "Database reachable" in result.output or "Failed to reach database" in result.output

def test_listplayer_not_found(runner):
    result = runner.invoke(cli, ['listplayer', 'NonExistent'])
    assert result.exit_code == 0
    assert "No player found" in result.output