# installs and configures an HAProxy server with custom "X-Served-By" HTTP header
exec { 'update_packages':
  command  => '/usr/bin/apt -y update && /usr/bin/apt -y upgrade'
}

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'header':
  command  => 'sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-available/default',
  provider => 'shell',
}

service {'nginx':
  ensure  => running
}
