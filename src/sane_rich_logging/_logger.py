import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Literal

from rich.logging import RichHandler


def setup_logging(
    log_file: str | None = None,
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] | None = None,
    log_max_size: int | None = None,
) -> None:
    """
    Configures logging for console and file outputs with different handlers and formats.

    Args:
        log_file (str | None): The file path to store log outputs. If provided, enables file
            logging at the specified path. Defaults to None (no file logging).
        log_level (Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] | None): The log level
            for both console and file handlers. Defaults to environment variable LOG_LEVEL or
            "DEBUG".
        log_max_size (int | None): Maximum size of the log file before it gets rotated.
            Only used if log_file is provided. Defaults to environment variable LOG_MAX_SIZE or 5MB.
    """
    # Determine log configuration from arguments or environment variables
    log_level = log_level or os.environ.get("LOG_LEVEL", "DEBUG").upper()
    log_level_numeric = getattr(logging, log_level, logging.DEBUG)

    # Root logger configuration
    logger = logging.getLogger()
    logger.setLevel(log_level_numeric)

    # Rich console handler
    console_handler = RichHandler(rich_tracebacks=True, show_path=False)
    console_handler.setLevel(log_level_numeric)
    console_handler.setFormatter(
        logging.Formatter(fmt="[%(asctime)s] %(message)s", datefmt="%m/%d/%y %H:%M:%S")
    )
    logger.addHandler(console_handler)

    if log_file is not None:
        # Only configure file logging if log_file is provided
        log_max_size = log_max_size or int(os.environ.get("LOG_MAX_SIZE", 5 * 1024 * 1024))

        # File handler with rotation
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s"
        )
        file_handler = RotatingFileHandler(log_file, maxBytes=log_max_size, backupCount=5)
        file_handler.setLevel(log_level_numeric)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
