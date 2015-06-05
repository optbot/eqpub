(function() {
  'use strict';

  var daemonSetup = require('@optbot/daemon-setup');

  daemonSetup.init({
    command: '/usr/bin/python',
    service: 'eqpub.py',
    user: 'eqpub'
  });
})();
