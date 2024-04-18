exec {'update ulimit':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => 'shell'
}

service { 'nginx':
  ensure  => 'running'
}
