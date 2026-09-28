"""Integration coverage for Copier's post-generation Git tasks."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

import pytest


ROOT = Path(__file__).parents[1]


def run(*args: str, cwd: Path, env: dict[str, str] | None = None) -> str:
    """Run a command and return its stripped standard output."""
    return subprocess.run(
        args,
        cwd=cwd,
        env=env,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


@pytest.mark.skipif(shutil.which("copier") is None, reason="copier is not installed")
def test_copy_initializes_git_but_update_does_not_commit(tmp_path: Path) -> None:
    """A copy gets one initial commit, while an update leaves changes uncommitted."""
    source = tmp_path / "source"
    destination = tmp_path / "exam"
    home = tmp_path / "home"
    home.mkdir()
    shutil.copytree(
        ROOT, source, ignore=shutil.ignore_patterns(".git", ".pytest_cache")
    )

    env = os.environ.copy()
    env["HOME"] = str(home)
    run("git", "init", "--initial-branch=main", cwd=source, env=env)
    run("git", "config", "user.name", "Exam Test", cwd=source, env=env)
    run("git", "config", "user.email", "exam-test@example.invalid", cwd=source, env=env)
    run("git", "add", "--all", cwd=source, env=env)
    run("git", "commit", "-m", "Template version 1", cwd=source, env=env)
    run("git", "tag", "1.0.0", cwd=source, env=env)

    run("git", "config", "--global", "user.name", "Generated Exam Test", cwd=home, env=env)
    run(
        "git",
        "config",
        "--global",
        "user.email",
        "generated-exam@example.invalid",
        cwd=home,
        env=env,
    )
    run(
        "copier",
        "copy",
        "--trust",
        "--defaults",
        "--data",
        "course=IT Security Management",
        str(source),
        str(destination),
        cwd=tmp_path,
        env=env,
    )

    assert (
        run("git", "rev-parse", "--is-inside-work-tree", cwd=destination, env=env)
        == "true"
    )
    assert run("git", "branch", "--show-current", cwd=destination, env=env) == "main"
    assert run("git", "log", "-1", "--format=%s", cwd=destination, env=env) == (
        "Initialize exam from template"
    )
    assert run("git", "show", "HEAD:.copier-answers.yml", cwd=destination, env=env)
    assert not (destination / ".copier_generate_tasks.py").exists()

    with (source / "template" / "README.md.jinja").open("a", encoding="utf-8") as readme:
        readme.write("\nUpdated template marker.\n")
    run("git", "add", "--all", cwd=source, env=env)
    run("git", "commit", "-m", "Template version 2", cwd=source, env=env)
    run("git", "tag", "2.0.0", cwd=source, env=env)

    head_before_update = run("git", "rev-parse", "HEAD", cwd=destination, env=env)
    run("copier", "update", "--trust", "--defaults", ".", cwd=destination, env=env)

    assert run("git", "rev-parse", "HEAD", cwd=destination, env=env) == head_before_update
    assert "Updated template marker." in (destination / "README.md").read_text()
    assert run("git", "status", "--short", cwd=destination, env=env)
    assert not (destination / ".copier_generate_tasks.py").exists()
