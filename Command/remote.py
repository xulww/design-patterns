class Remote:
    _command = None

    def set_command(self, command):
        self._command = command

    def pressButton(self):
        print("Executing command")
        self._command.execute()
