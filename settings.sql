drop database greats;
drop user greatsuser;

create database soundspreader;
create user soundspreaderuser with password 'soundspreader';
grant all privileges on database soundspreader to soundspreaderuser;