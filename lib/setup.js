(function() {
  'use strict';

  var daemonSetup = require('@optbot/daemon-setup');
  var pyDaemon = require('@optbot/py-daemon');
  var path = require('path');
  var user = process.env.npm_package_config_user;

  daemonSetup.init({
    command: process.env.npm_package_config_command,
    service: process.env.npm_package_config_service,
    user: user,
    pathToFiles: path.join(__dirname, '..', process.env.npm_package_config_serviceDir),
    noupstart: true
  });
  pyDaemon.init({
    user: user,
    configWriter: path.join(__dirname, 'configure.py')
  });
})();
