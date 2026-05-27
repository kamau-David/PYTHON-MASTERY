"""logging - the proper alternative to print() for anything beyond a
quick script. Supports levels, timestamps, and easy on/off per module."""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

logger.debug("debug detail - verbose, usually off in production")
logger.info("info - normal operational messages")
logger.warning("warning - something unexpected, but not broken")
logger.error("error - something failed")

def risky_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("division failed")   # logs the full traceback
        return None

risky_division(10, 0)
