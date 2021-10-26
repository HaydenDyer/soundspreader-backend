drop database greats;
drop user greatsuser;

create database greats;
create user greatsuser with password 'greats';
grant all privileges on database greats to greatsuser;