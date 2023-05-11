#!/usr/bin/env bash
#Sets up web servers for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# configure firewall
sudo ufw allow 'Nginx HTTP'

# creates directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "felixhatesbugs" > /data/web_static/releases/test/index.html

# creates symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# removes circular symbolic link reference
sudo rm /data/web_static/current/test

# changes owner and group owner of /data
sudo chown -hR ubuntu:ubuntu /data

# edits config file
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restarts  nginx
sudo service nginx restart
