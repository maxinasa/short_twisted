import logging.config
import os

from twisted.internet import asyncioreactor
from twisted.python import log as twisted_log

from generate_html import generate_html_page
from servlets import Component

logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 17995))


LOG_SETUP = {
    'version': 1,
    'formatters': {
        'normal': {
            'format': "%(asctime)s [%(process)d] %(levelname)-5s %(name)s %(message)s"
        }
    },
    'handlers': {
        # This handler prints to Standard Error
        #
        'stderr': {
            'class': "logging.StreamHandler",
            'formatter': "normal",
            'stream': "ext://sys.stderr",
        },
        # This handler prints to Standard Output.
        'stdout': {
            'class': "logging.StreamHandler",
            'formatter': "normal",
            'stream': "ext://sys.stdout",
        },
        # This handler demonstrates logging to a text file on the filesystem.
        # You can use logrotate(8) to perform log rotation.
        #
        'file': {
            'class': "logging.handlers.WatchedFileHandler",
            'formatter': "normal",
            'filename': "./static_dir.log",
        },
    },
    'root': {
      # Specify the handler(s) to send log messages to.
      'handlers': ["stderr", "file"],
      'level': "INFO",
    }
}

if __name__ == '__main__':

    logging.config.dictConfig(LOG_SETUP)

    observer = twisted_log.PythonLoggingObserver()
    observer.start()

    generate_html_page('page', 3)
    generate_html_page('big_page', 1025)

    logger.info('Starting reactor')
    component = Component(custom_reactor=asyncioreactor.AsyncioSelectorReactor(), port=PORT)
    component.run()
