# Using puppet to install a package

exec { 'Installing python package':
  command =>  'pip3 install flask',
  path    =>  '/usr/bin',
  unless  =>  '/usr/bin/test -f /usr/local/lib/python3.4/dist-packages/flask/app.py',
}
