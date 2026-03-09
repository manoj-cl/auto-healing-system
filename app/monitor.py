import psutil
import time
import yaml
from healer import restart_service
from alerts import send_slack_alert
from logger import setup_logger

logger = setup_logger()

with open("config.yaml") as f:
    config = yaml.safe_load(f)

CPU_LIMIT = config["cpu_threshold"]
MEM_LIMIT = config["memory_threshold"]
SERVICE = config["service_name"]

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    logger.info(f"CPU={cpu}% MEM={mem}%")

    if cpu > CPU_LIMIT or mem > MEM_LIMIT:
        logger.warning("Threshold breached → Auto-healing triggered")
        restart_service(SERVICE)
        send_slack_alert(cpu, mem, SERVICE)

while True:
    check_system()
    time.sleep(config["check_interval"])
