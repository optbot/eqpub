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
        _section = constants.CFGSECTION_MAIN
        _config.read(constants.CONFIGFILE)
        #self._setup_logging(_config)
        signal.signal(signal.SIGTERM, self._stop_handler)

    def start(self):
        #self.logger.info('starting')
        signal.pause()

    def _stop_handler(self):
        #self.logger.info('stopping')
        sys.exit(0)

    def _setup_logging(self, config):
        self.logger = logging.getLogger(constants.USER)
        _logpath = _config.get(_section, 'logpath', 1) 
        _logfmt = _config.get(_section, 'logfmt', 1)
        _handler = logging.FileHandler(os.path.join(_logpath, 'service.log'))
        _formatter = logging.Formatter(_logfmt)
        _handler.setFormatter(_formatter)
        self.logger.addHandler(_handler)
        self.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    EqPub().start()
