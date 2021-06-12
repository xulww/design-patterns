class Logger:

    ERROR = 3
    WARN = 2
    INFO = 1
    # _level = None
    _level = 0
    _next_logger = None

    def set_next_logger(self, next_logger):
        self._next_logger = next_logger
        self._level = self.level

    def log_message(self, level, message):
        if self._level <= level:
            self.handle_message(message)
            return

        if self._next_logger != None:
            self._next_logger.log_message(level, message)

    def handle_message(self, message):
        pass
