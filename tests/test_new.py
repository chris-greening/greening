import sys
import json
import shutil
import tempfile
from pathlib import Path
import os

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from greening._commands.new import new

@pytest.fixture
def temp_project_dir():
    """Creates a temporary directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)

def test_scaffold_basic_project(temp_project_dir, monkeypatch):
    monkeypatch.chdir(temp_project_dir)

    (temp_project_dir / "greening.json").write_text(json.dumps({
        "project_name": "Basic Project",
        "project_slug": "basic_project"
    }))

    new(".")

    assert (temp_project_dir / ".git").exists(), ".git directory should exist"
    assert (temp_project_dir / "README.md").exists(), "README.md should exist"

    src_path = temp_project_dir / temp_project_dir
    # print(os.listdir(temp_project_dir))
    assert src_path.exists() and src_path.is_dir(), f"{temp_project_dir}/ directory should exist"
    assert any(p.suffix == ".py" for p in src_path.rglob("*")), f"No .py files found in {temp_project_dir}/"
