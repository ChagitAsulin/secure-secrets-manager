import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def log_event(event_type: str, user_id: str, detail: str = ""):
    """Log an access or security event"""
    logger.info(f"EVENT={event_type} | USER={user_id} | DETAIL={detail}")