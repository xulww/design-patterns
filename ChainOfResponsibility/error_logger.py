from logger import Logger


class ErrorLogger(Logger):

    def __init__(self):
        self.level = Logger.ERROR

    def handle_message(self, message):
        print("Error: " + message)
