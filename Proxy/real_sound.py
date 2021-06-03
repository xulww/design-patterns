from sound import Sound


class RealSound(Sound):

    _file_name = None

    def __init__(self, file_name):
        self._file_name = file_name

    def play(self):
        print("Playing " + self._file_name)
