from error_logger import ErrorLogger
from warn_logger import WarnLogger
from info_logger import InfoLogger


def main():
    error_logger = ErrorLogger()
    warn_logger = WarnLogger()
    info_logger = InfoLogger()

    error_logger.set_next_logger(warn_logger)
    warn_logger.set_next_logger(info_logger)

    error_logger.log_message(2, "Test message")
    error_logger.log_message(5, "QA test")


if __name__ == "__main__":
    main()
