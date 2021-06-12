from logger import Logger


class WarnLogger(Logger):

    def __init__(self):
        self.level = Logger.WARN

    def handle_message(self, message):
        print("Warn: " + message)
