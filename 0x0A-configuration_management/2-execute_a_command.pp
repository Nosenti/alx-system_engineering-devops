# Executing a command with puppet
exec { 'kill':
  command => '/usr/bin/pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
