from sane_rich_logging import setup_logging
import logging
import tempfile
from rich import print

if __name__ == "__main__":
    # Test the logging configuration
    with tempfile.NamedTemporaryFile(delete=False, suffix="-rich.log") as tmp:
        setup_logging(log_file=tmp.name)

        logging.debug("This is a debug message.")
        logging.info("This is an info message.")
        logging.warning("This is a warning message.")
        logging.error("This is an error message.")
        logging.critical("This is a critical message.")

        print(f"\n[bold]You can see the log at {tmp.name}[/bold]")
