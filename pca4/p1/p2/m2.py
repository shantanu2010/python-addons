import logging
def f3():
    logger = logging.getLogger(__name__)
    
    logger.info('Entering function f3')
    logger.warning('This cannot be done using function f3')
    logger.error('Error occurred in function f3')
    logger.debug('Leaving function f3')
    
    
def f4():
    logger = logging.getLogger(__name__)
    
    logger.info("Entering method f4")
    logger.warning("This is a log from f4 at WARNING level")
    logger.error("This is a log from f4 at ERROR level")
    logger.debug("Leaving method f4")