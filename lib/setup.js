(function() {
  'use strict';

  var daemonSetup = require('@optbot/daemon-setup');
  var path = require('path');

  daemonSetup.init({
    command: '/usr/bin/python',
    service: 'eqpub.py',
    user: 'eqpub',
    pathToFiles: path.join(__dirname, '../src')
  });
})();
