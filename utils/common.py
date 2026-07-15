import os
import logging
import logging.config
from datetime import datetime
from pathlib import Path


def get_logger():
    """Return a logger instance for the calling function."""
    log_dir = Path(__file__).parent.parent / "reports" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "test_execution.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger()
    return logger


def read_date():
    """Return current date in YYYY-MM-DD format."""
    return datetime.today().strftime("%Y-%m-%d")


def read_time():
    """Return current time in HH-MM-SS format."""
    return datetime.today().strftime("%I-%M-%S-%p")


def clean_directory(directory):
    """Remove all files in directory except excluded subdirectories."""
    exclude = {"screenshots", "allure_report", "htmlreport", "logs", "xml_report"}
    for root, dirs, files in os.walk(directory, topdown=False):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except OSError:
                pass
