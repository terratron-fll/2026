import subprocess
import sys

def check() -> None:
    """Runs ruff and mypy checks."""
    print("🚀 Running code quality checks...")
    subprocess.run(["ruff", "check", "."], check=True)
    subprocess.run(["mypy", "."], check=True)
    print("✅ All checks passed!")

def format_code() -> None:
    """Fixes linting and formats code."""
    print("🧹 Cleaning up code...")
    subprocess.run(["ruff", "check", "--fix", "."], check=True)
    subprocess.run(["ruff", "format", "."], check=True)
    print("✨ Code is now sparkling clean!")

def run_mission() -> None:
    """Runs the main mission script."""
    print("🤖 Starting robot mission...")
    subprocess.run([sys.executable, "projects/helloworld.py"], check=True)
