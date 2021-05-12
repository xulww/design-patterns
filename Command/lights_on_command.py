from command import Command


class LightsOnCommand(Command):
    _lights = None

    def __init__(self, lights):
        self._lights = lights

    def execute(self):
        self._lights.switch_on()
