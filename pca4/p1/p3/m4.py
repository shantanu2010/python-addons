import logging
def f6():
    logger = logging.getLogger(__name__)
    
    logger.info("Entering method f6")
    logger.warning("This is a log from f6 at WARNING level")
    logger.error("This is a log from f6 at ERROR level")
    logger.debug("Leaving method f6")