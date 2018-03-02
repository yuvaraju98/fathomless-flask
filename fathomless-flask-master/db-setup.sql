create database if not exists fathomless;
use fathomless;

CREATE TABLE user96 (
	name varchar(32) NOT NULL,
	email varchar(32) PRIMARY KEY NOT NULL,
	sub varchar(32) NOT NULL,
	descr text NOT NULL
);
