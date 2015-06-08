(function() {
  'use strict';

  var daemonSetup = require('@optbot/daemon-setup');
  var path = require('path');

  daemonSetup.init({
    command: process.env.npm_package_config_command,
    service: process.env.npm_package_config_service,
    user: process.env.npm_package_config_user,
    pathToFiles: path.join(__dirname, '..', process.env.npm_package_config_serviceDir),
    noupstart: true
  });
})();
