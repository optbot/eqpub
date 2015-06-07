(function() {
  'use strict';
  var argv = require('yargs').argv;
  var pyDaemon = require('@optbot/py-daemon');
  var daemonParams = {
    python: process.env.npm_package_config_command,
    user: process.env.npm_package_config_user,
    service: process.env.npm_package_config_service,
    action: argv.action
  };

  pyDaemon.exec(daemonParams); 
})();
