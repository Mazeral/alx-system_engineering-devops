# Kills a process names 'killmenow'

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
