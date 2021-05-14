class Lights:

    _lights_on = False

    def switch_on(self):
        self._lights_on = True
        print("Lights are on")

    def switch_off(self):
        self._lights_on = False
        print("Lights are off")
