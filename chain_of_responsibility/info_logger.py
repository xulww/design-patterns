from logger import Logger


class InfoLogger(Logger):

    def __init__(self):
        self.level = Logger.INFO

    def handle_message(self, message):
        print("INFO: " + message)
