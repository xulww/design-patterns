from media_player import MediaPlayer


class Vlc(MediaPlayer):

    def play(self, file_name):
        print("Playing vlc file " + file_name)
