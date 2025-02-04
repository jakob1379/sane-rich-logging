# tests/test_import_logger.py

import logging
import os

import pytest

from sane_rich_logging import setup_logging

# Define a temporary log file for testing
LOG_FILE = "test_log.log"


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Cleanup the log file after each test."""
    yield
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


def test_logging_levels_and_output(caplog):
    """Test logging levels, content of log file, and output to terminal."""
    # Setup logging with a specific log file and level
    setup_logging(log_file=LOG_FILE, log_level="DEBUG")

    # Log messages of various levels
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")

    # Check the captured log output
    assert "This is a debug message." in caplog.text
    assert "This is an info message." in caplog.text
    assert "This is a warning message." in caplog.text
    assert "This is an error message." in caplog.text
    assert "This is a critical message." in caplog.text

    # Check the content of the log file
    with open(LOG_FILE, "r") as f:
        log_content = f.read()
        assert "This is a debug message." in log_content
        assert "This is an info message." in log_content
        assert "This is a warning message." in log_content
        assert "This is an error message." in log_content
        assert "This is a critical message." in log_content
