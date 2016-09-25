create user 'simpleboard'@'localhost' identified by 'simpleboard';

grant all privileges on simpleboard.* to 'simpleboard'@'localhost';

create database simpleboard DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;