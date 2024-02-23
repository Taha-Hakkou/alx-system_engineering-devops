# installs flask from pip3
exec { 'flask':
  command => 'pip3 install flask -v 2.1.0',
}
