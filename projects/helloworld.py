from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait


def run_mission() -> None:
    """A simple Hello World mission for the Prime Hub."""
    # Initialize the hub
    hub = PrimeHub()

    # Visual Hello: Change the status light to green
    hub.light.on(Color.GREEN)

    # Audio Hello: Play a quick beep
    hub.speaker.beep()

    # Console Hello: This will show up in your terminal
    print("Hello, Team Terratron 2026!")

    # Wait for 2 seconds so we can see the light
    wait(2000)

if __name__ == "__main__":
    run_mission()
