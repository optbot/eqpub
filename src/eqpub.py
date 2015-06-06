"""
.. Copyright (c) 2015 Marshall Farrier, Robert Rodrigues, Mark Scappini
   license http://opensource.org/licenses/MIT

Equity publisher service main
=============================
"""

import signal
import sys

class EqPub(object):
    def __init__(self):
        signal.signal(signal.SIGTERM, self._stop_handler)

    def start(self):
        signal.pause()

    def _stop_handler(self):
        sys.exit(0)

if __name__ == '__main__':
    EqPub().start()
