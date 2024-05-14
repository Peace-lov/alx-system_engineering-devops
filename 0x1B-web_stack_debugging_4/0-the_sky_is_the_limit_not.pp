# This manuscript is for increasing the amount of traffic an nginx server can handle.

# This is to increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# This is to restart the nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
