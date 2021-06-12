from media_package import MediaPackage


class Mp3(MediaPackage):

    def play_file(self, file_name):
        print("Playing mp3 file " + file_name)
