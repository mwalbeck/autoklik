import subprocess
from autoklik.main import get_window_name_from_id


def test_get_window_name_from_id_exists(monkeypatch):
    def mock_subprocess_run(*args, **kwargs):
        return subprocess.CompletedProcess("", 0, stdout=b"Minecraft\n")

    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    result = get_window_name_from_id("1236721")
    assert result == "Minecraft"


def test_get_window_name_from_id_does_not_exist(monkeypatch):
    def mock_subprocess_run(*args, **kwargs):
        return subprocess.CompletedProcess("", 0, stdout=b"")

    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)

    result = get_window_name_from_id("1236721")
    assert result == ""
