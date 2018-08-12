import logging
import logging.config
import p1
from p1 import m1, m3
from p1.p2 import m2
from p1.p3 import m4
config={
    
    'version': 1,
    
    'disable_existing_loggers': False,
    
    'formatters': {
        'standard': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s : [%(levelname)s] -> %(name)s: %(message)s'
        },
    
    },
    
    'handlers': {

        'main':
            {
                'level':'DEBUG',
                'formatter': 'standard',
               'class':'logging.FileHandler',
                'filename':'main.log',
                'mode':'w'

            },
        'p1':
            {
                'level':'DEBUG',
                'formatter': 'standard',
               'class':'logging.FileHandler',
                'filename':'p1.log',
                'mode':'w'
            },
        'p1.p2': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename':'p2.log',
            'mode':'w'

        },
        'console':
            {
              'level':'WARNING',
                'formatter':'standard',
                'class':'logging.StreamHandler'
            },

    },
    "loggers": {
        "pca.p1": {
            "level": "DEBUG",
            "handlers": ["console", "p1"],
            "propagate": False
        },

        "pca.p1.p2": {
            "level": "DEBUG",
            "handlers": ["console", "p1.p2"],
            "propagate": False
        }
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "main"],
        'propagate':False
    }
}
if __name__=='__main__':

    logger=logging.config.dictConfig(config)
    logger=logging.getLogger(__name__)
    logger.error("This is a log from main at ERROR level")
    logger.warning("This is a log from main at ERROR level")
    logger.info("Entering Main")
    
    m1.f1()
    m1.f2()
    m2.f3()
    m2.f4()
    m3.f5()
    m4.f6()
    
    logger.error("Exiting Main")




