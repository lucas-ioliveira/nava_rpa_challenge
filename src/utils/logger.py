import logging
from datetime import datetime
from pathlib import Path


path_logs = Path("src/logs")
path_logs.mkdir(parents=True, exist_ok=True)
datetime_now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
file_path = path_logs / f"execution_{datetime_now}.log"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(file_path, encoding="utf-8")
    ]
)

def get_logger(nome_modulo):
    return logging.getLogger(nome_modulo)