exec {'change op hard limits':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1024/" /etc/security/limits.conf',
  provider => 'shell'
}
exec {'change op soft limits':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" /etc/security/limits.conf',
  provider => 'shell'
}
