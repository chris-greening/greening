import sys
import json
import shutil
import tempfile
from pathlib import Path
import os

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from greening.commands import new

def test_module_imports():
    assert hasattr(new, "new")
    assert callable(new.new)

def test_help_new_prints(capsys):
    new.help_new()
    captured = capsys.readouterr()
    assert "Usage: greening new" in captured.out
