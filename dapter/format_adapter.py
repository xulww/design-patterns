from media_player import MediaPlayer


class FormatAdapter(MediaPlayer):

    _media_package = None

    def __init__(self, media_package):
        self._media_package = media_package

    def play(self, file_name):
        print("Opening file with an adapter")
        self._media_package.play_file(file_name)
