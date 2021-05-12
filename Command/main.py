from remote import Remote
from lights import Lights
from lights_on_command import LightsOnCommand
from lights_off_command import LightsOffCommand


def main():
    remote = Remote()
    lights = Lights()
    lights_on_command = LightsOnCommand(lights)
    lights_off_command = LightsOffCommand(lights)

    remote.set_command(lights_on_command)
    remote.pressButton()

    remote.set_command(lights_off_command)
    remote.pressButton()


if __name__ == "__main__":
    main()
