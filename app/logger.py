# import logging
# from pathlib import Path

# def setup_logger():
#     log_dir = Path(__file__).resolve().parent.parent / "logs"
#     log_dir.mkdir(parents=True, exist_ok=True)

#     logging.basicConfig(
#         filename=log_dir / "auto_heal.log",
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s"
#     )
#     return logging.getLogger()


# import logging
# from pathlib import Path

# def setup_logger():
#     logger = logging.getLogger()

#     # Prevent duplicate handlers
#     if logger.hasHandlers():
#         return logger

#     logger.setLevel(logging.INFO)

#     log_dir = Path(__file__).resolve().parent.parent / "logs"
#     log_dir.mkdir(parents=True, exist_ok=True)

#     formatter = logging.Formatter(
#         "%(asctime)s - %(levelname)s - %(message)s"
#     )

#     # File handler
#     file_handler = logging.FileHandler(log_dir / "auto_heal.log")
#     file_handler.setFormatter(formatter)

#     # Console handler
#     console_handler = logging.StreamHandler()
#     console_handler.setFormatter(formatter)

#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)

#     return logger


# from pathlib import Path
# import logging

# def setup_logger():
#     log_dir = Path("/app/logs")
#     log_dir.mkdir(parents=True, exist_ok=True)

#     logging.basicConfig(
#         filename=log_dir / "auto_heal.log",
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s"
#     )

#     return logging.getLogger()

from pathlib import Path
import logging
import sys

def setup_logger():
    log_dir = Path("/app/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # File handler
    file_handler = logging.FileHandler(log_dir / "auto_heal.log")
    file_handler.setFormatter(formatter)

    # Console handler (for Docker logs)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger