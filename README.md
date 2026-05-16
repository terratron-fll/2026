# Team Terratron 2026 - FLL

This repository contains the code for Team Terratron's 2026 FIRST LEGO League (FLL) season. We use the Pybricks platform to program our LEGO Technic hubs.

## Project Structure

- **`harness/`**: This is the shared library for the team. It contains the "building blocks" — functions and classes that help us operate the robot (e.g., specific turns, motor synchronization, sensor handling). This code is maintained by coaches and team members together to ensure we have a robust foundation for all missions.
- **`projects/`**: This directory contains specific mission scripts. Each mission is a standalone file that utilizes the shared code defined in the `harness`.
- **`pyproject.toml` & `uv.lock`**: These files manage our project's dependencies and environment settings using `uv`.

## Getting Started

We use `uv` for modern, fast Python package and environment management.

### Prerequisites

1.  **Python 3.11+**: Ensure you have Python installed on your system.
2.  **uv**: If you don't have it yet, install it via:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

### Setup

Clone the repository and run the following command to set up your virtual environment and install all necessary dependencies:

```bash
uv sync
```

This will create a `.venv` directory and ensure all tools (like `ruff` for linting and `mypy` for type checking) are ready to use.

## Workflow

### Running Code

To run a script (like our hello world example), use `uv run`:

```bash
uv run run
```
*(Note: We've added a shortcut! `uv run run` will execute the current main mission script).*

### Code Quality (Linters & Type Checking)

We use several tools to help us write clean, error-free code:

-   **Ruff**: Automatically fixes small mistakes and formats our code to look professional.
-   **Mypy**: Checks our "types" (making sure we don't accidentally treat a number like a piece of text, for example).

You can run these checks manually:

```bash
uv run check
```

Or format your code:

```bash
uv run format
```

### Shared Robot Code

Instead of setting up motors and sensors in every single mission script, we use a shared **`Robot`** class.

1.  Check out `harness/robot.py` and update the ports to match your robot build.
2.  In your mission scripts, you can now do:
    ```python
    from harness.robot import Robot
    
    def run_mission():
        bot = Robot()
        bot.beep()
        bot.drive_base.straight(100)
    ```

### VS Code Integration

We've included a `.vscode` folder that sets up:
- **Format on Save**: Every time you save a file, it will be automatically cleaned up.
- **Recommended Extensions**: VS Code will prompt you to install the best tools for Python and Pybricks.
