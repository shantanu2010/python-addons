import logging
def f5():
    logger = logging.getLogger(__name__)
    
    logger.info("Entering method f5")
    logger.warning("This is a log from f5 at WARNING level")
    logger.error("This is a log from f5 at ERROR level")
    logger.debug("Leaving method f5")