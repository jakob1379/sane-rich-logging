from sane_rich_logging import setup_logging
import logging

if __name__ == "__main__":
    # Test the logging configuration
    setup_logging()

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")
