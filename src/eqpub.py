"""
.. Copyright (c) 2015 Marshall Farrier, Robert Rodrigues, Mark Scappini
   license http://opensource.org/licenses/MIT

Equity publisher service main
=============================
"""

import ConfigParser
import logging
import os.path
import signal
import sys

import constants

class EqPub(object):
    def __init__(self):
        _config = ConfigParser.SafeConfigParser()
        _config.read(constants.CONFIGFILE)
        self._setup_logging(_config)
        signal.signal(signal.SIGTERM, self.stop)

    def start(self):
        self.logger.info('starting')
        signal.pause()

    def stop(self, sig, frame):
        self.logger.info('stopping')
        logging.shutdown()
        sys.exit(0)

    def _setup_logging(self, config):
        self.logger = logging.getLogger(constants.USER)
        _section = constants.CFGSECTION_MAIN
        _logpath = config.get(_section, 'logpath', 1) 
        _logfmt = config.get(_section, 'logfmt', 1)
        _handler = logging.FileHandler(os.path.join(_logpath, 'service.log'))
        _formatter = logging.Formatter(_logfmt)
        _handler.setFormatter(_formatter)
        self.logger.addHandler(_handler)
        self.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    EqPub().start()
