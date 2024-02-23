# sets up the client SSH configuration file so that we can connect to a server without typing a password
include stdlib
file_line { 'Turn off passwd auth':
  ensure => created,
  path   => '/etc/ssh/ssh_config',
  match  => '#   PasswordAuthentication yes',
  line   => '#   PasswordAuthentication no'
}
file_line { 'Declare identity file':
  ensure => created,
  path   => '/etc/ssh/ssh_config',
  line   => '#   IdentityFile ~/.ssh/school'
}
