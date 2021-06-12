from sound import Sound
from real_sound import RealSound


class ProxySound(Sound):

    _real_sound = None
    _file_name = None

    def __init__(self, file_name):
        self._file_name = file_name

    def play(self):
        # here if a condition is not true return

        if not self._real_sound:
            self._real_sound = RealSound(self._file_name)

        self._real_sound.play()
