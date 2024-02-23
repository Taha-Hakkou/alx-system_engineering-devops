# installs flask from pip3
package { 'flask':
  ensure   => '2.1.0',
  require  => 'python-3.8.10',
  provider => 'pip3',
}
