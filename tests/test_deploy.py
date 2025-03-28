import os
import json
import shutil
import subprocess
from pathlib import Path
import tempfile

import pytest

from greening._commands.deploy import deploy_site

@pytest.fixture
def temp_git_repo(monkeypatch):
    temp_dir = Path(tempfile.mkdtemp())
    monkeypatch.chdir(temp_dir)

    subprocess.run(["git", "init", "-b", "main"], cwd=temp_dir, check=True)
    (temp_dir / "README.md").write_text("# Temp project")
    subprocess.run(["git", "add", "."], cwd=temp_dir, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=temp_dir, check=True)

    (temp_dir / "greening.json").write_text(json.dumps({
        "project_name": "Deploy Test Project",
        "project_slug": "deploy_test_project"
    }))

    yield temp_dir
    shutil.rmtree(temp_dir)

def test_deploy_site_creates_gh_pages(temp_git_repo):
    repo_path = temp_git_repo
    deploy_site()

    result = subprocess.run(["git", "branch"], cwd=repo_path, capture_output=True, text=True)
    assert "gh-pages" in result.stdout, "gh-pages branch should be created"
