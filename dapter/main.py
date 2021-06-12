from format_adapter import FormatAdapter
from mp3 import Mp3


def main():
    player = Mp3()
    player.play_file("test_song.mp3")

    media_player = FormatAdapter(player)
    media_player.play("file.avi")


if __name__ == "__main__":
    main()
