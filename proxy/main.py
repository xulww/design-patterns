from real_sound import RealSound
from proxy_sound import ProxySound


def main():
    real_sound = RealSound("laugh.mp3")
    real_sound.play()

    proxy_sound = ProxySound("whistle.mp3")
    proxy_sound.play()


if __name__ == "__main__":
    main()
