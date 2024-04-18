# 0-the_sky_is_the_limit_not.pp
exec {'update ulimit':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider => 'shell'
}
exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => 'shell'
}
