import sys
import json
import shutil
import tempfile
from pathlib import Path
import os
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from greening.commands import new

class DummyConfig:
    def __init__(self, tmp_path, config_data=None):
        self.data = config_data or {
            "project_slug": "testproject",
            "github_username": "testuser",
            "project_name": "Test Project",
            "venv": {"create": True, "python": "python3"},
        }
        self.path = tmp_path / "greening.yaml"

@pytest.fixture
def dummy_config(tmp_path):
    return DummyConfig(tmp_path)

class DummyConfigWithGit:
    def __init__(self, project_dir):
        self.path = project_dir / "greening.yaml"
        self.data = {}  # minimal config for now

def test_module_imports():
    assert hasattr(new, "new")
    assert callable(new.new)

def test_help_new_prints(capsys):
    new.help_new()
    captured = capsys.readouterr()
    assert "Usage: greening new" in captured.out

def test_virtualenv_runs_when_enabled(dummy_config, mocker):
    mock_run = mocker.patch("subprocess.run")

    new._maybe_create_virtualenv(dummy_config)
    mock_run.assert_called_once()

def test_skips_virtualenv_when_disabled(tmp_path):
    config = DummyConfig(tmp_path, {"venv": {"create": False}})
    new._maybe_create_virtualenv(config)

def test_git_init_skipped_if_git_exists(tmp_path):
    project_dir = tmp_path
    (project_dir / ".git").mkdir()

    config = DummyConfigWithGit(project_dir)
    new._maybe_initialize_git_repo(config)

def test_git_initialization_when_git_missing(dummy_config, tmp_path, mocker):
    # Simulate a project directory with a dummy file
    dummy_config.path = tmp_path / "greening.yaml"
    project_dir = dummy_config.path.parent
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "README.md").write_text("# Test Project")

    mock_run_git = mocker.patch("greening.commands.new.run_git")
    new._maybe_initialize_git_repo(dummy_config)

    calls = [call.args[0] for call in mock_run_git.call_args_list]
    assert "git init" in calls
    assert "git add ." in calls
    assert "git commit -m 'Initial commit'" in calls
    assert "git branch -M main" in calls