# installs and configures an HAProxy server with custom "X-Served-By" HTTP header
exec { 'update_packages':
  command => '/usr/bin/apt-get -y update && /usr/bin/apt-get -y upgrade',
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

exec {'header':
  command  => 'sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service {'nginx':
  restart => '/usr/sbin/service nginx restart',
}
