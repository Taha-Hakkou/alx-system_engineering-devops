# installs flask from pip3
exec { 'flask':
  require => 'python-3.8.10',
  command => 'pip3 install flask -v 2.1.0',
}
