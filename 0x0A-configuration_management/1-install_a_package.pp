# installs flask from pip3
package { 'flask':
  require  => 'python-3.8.10'
  ensure   => '2.1.0',
  provider => 'pip3',
}
