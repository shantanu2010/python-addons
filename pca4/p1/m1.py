import logging


def f1():
    logger = logging.getLogger(__name__)
    logger.info("Entering method f1")
    logger.warning("This is a log from f1 at WARNING level")
    logger.error("This is a log from f1 at ERROR level")
    logger.debug("Leaving method f1")


def f2():
    logger = logging.getLogger(__name__)
    
    logger.info("Entering method f2")
    logger.warning("This is a log from f2 at WARNING level")
    logger.error("This is a log from f2 at ERROR level")
    logger.debug("Leaving method f2")
    