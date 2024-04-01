# Script customize http response header by adding a header "X-Served-By" 
# which returns the server name as [Student-ID]-web-01 or [Student-ID]-web-02

exec { 'command':
  command  => 'apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
