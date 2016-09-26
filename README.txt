DB생성
    deploy/mysql-query.sql 참조
    default-setting
    simpleBoard/settings.py DATABASE
        username:simpleboard
        password:simpleboard
        host:localhost
        port:3306
패키지인스톨
git nginx python
pip install requirement.txt

#환경설정
#nginx.conf -> deploy/simplboard_nginx.conf 을 /etc/nginx/nginx.conf에 덮어쓰기

sed "s?SITENAME/simpleboard/g" \
deploy_tools/nginx.template.conf | sudo tee \
/etc/nginx/sites-available/simpleboard

gunicorn-upstart.template.conf --- USERNAME & SITENAME을 맞게 설정

실행
sudo start 