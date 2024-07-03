# installs flask 2.1.0

exec { 'install_flask_and_werkzeug':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show flask | grep Version | grep 2.1.0',
}
