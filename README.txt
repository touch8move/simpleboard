
[package]
#sudo apt-get update
sudo apt-get install git nginx python3-dev mysql-client mysql-server libmysqlclient-dev python-pip
sudo pip install virtualenv

[source]
git clone https://touch8me@bitbucket.org/touch8me/simpleboard.git


[virtualenv]
virtualenv env -p python3
source env/bin/activate
cd simpleboard/
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
create user 'simpleboard'@'localhost' identified by 'simpleboard';
grant all privileges on simpleboard.* to 'simpleboard'@'localhost';
create database simpleboard DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

../env/bin/python manage.py migrate
../env/bin/python manage.py collectstatic

[gunicorn]
vi /home/USER_NAME/simpleboard/deploy/gunicorn-upstart.template.conf
USER_NAME 변경
sudo ln -s /home/USER_NAME/simpleboard/deploy/gunicorn-upstart.template.conf /etc/init/gunicorn.conf
sudo initctl reload-configuration
sudo start gunicorn

[nginx]
sudo service nginx stop
file: simpleboard/deploy/simpleboard_nginx.conf
SERVER_NAME(Domain), USER_NAME 값 세팅
file: simpleboard/deploy/gunicorn-upstart.template.conf
USER_NAME 값 세팅

sudo ln -s /home/USER_NAME/simpleboard/deploy/simpleboard_nginx.conf /etc/nginx/sites-available/simpleboard
sudo ln -s /etc/nginx/sites-available/simpleboard /etc/nginx/sites-enabled/simpleboard
sudo service nginx start
