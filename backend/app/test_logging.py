from .core.logging import get_logger

logger = get_logger("scrape2insights")

logger.info("Hello from logging!")
logger.warning("Something might be off...")
logger.error("Oops, an error occurred!")
