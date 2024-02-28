# installs and configures an Nginx server & performs a 301 redirect when querying /redirect_me
exec { 'update_packages':
  command => '/usr/bin/apt-get -y update && /usr/bin/apt-get -y upgrade',
}

package { 'nginx':
  ensure   => installed,
  provider => 'apt',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec {'redirect_me':
  command  => '/usr/bin/sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure  => running,
}
