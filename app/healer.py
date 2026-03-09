import subprocess
from logger import setup_logger

logger = setup_logger()

def restart_service(service):
    try:
        subprocess.run(
            ["pkill", "-f", service],
            check=False
        )
        logger.info(f"Simulated restart for process: {service}")
    except Exception as e:
        logger.error(f"Healing failed: {e}")
