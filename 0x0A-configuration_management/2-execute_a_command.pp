# Using puppet to kill a process name "killmenow"

exec { 'Kill a process':
  command  =>  'pkill -f killmenow',
  provider =>  'shell',
}
