
[package]
sudo apt-get update
sudo apt-get install git nginx python3-dev mysql-client mysql-server libmysqlclient-dev
sudo pip install virtualenv gunicorn

[source]
git clone https://touch8me@bitbucket.org/touch8me/simpleboard.git


[virtualenv]
virtualenv env -p python3
source env/bin/activate
pip3 install -r requirement.txt
pip3 install mysqlclient
deactivate


[mysql]
simpleBoard/mysql.cnf
    username:simpleboard
    password:simpleboard
    host:localhost
    port:3306

deploy/mysql-query.sql 실행
env/bin/python simpleBoard/manage.py migrate



[gunicorn]
sudo ln -s /home/vagrant/simpleBoard/deploy/gunicorn-upstart.template.conf /etc/init/gunicorn.conf

[nginx]
sudo ln -s /home/vagrant/simpleBoard/deploy/simpleboard_nginx.conf /etc/nginx/sites-available/simpleBoard
sudo ln -s /etc/nginx/sites-available/simpleBoard /etc/nginx/sites-enabled/simpleBoard
