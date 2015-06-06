(function() {
  'use strict';
  var argv = require('yargs').argv;
  var pyDaemon = require('@optbot/py-daemon');
  var daemonParams = {
    python: '/usr/bin/python',
    user: 'eqpub',
    service: 'eqpub.py',
    action: argv.action
  };

  pyDaemon.exec(daemonParams); 
})();
