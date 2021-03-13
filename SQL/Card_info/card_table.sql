CREATE DATABASE train;
USE train;

CREATE TABLE Customer
(
	customer_id INT UNSIGNED,
    customer_name VARCHAR(30) NOT NULL,
    PRIMARY KEY (customer_id)
) ENGINE = INNODB;

CREATE TABLE Card
(
	card_id INT UNSIGNED,
    balance INT NOT NULL,
    PRIMARY KEY(card_id)
) ENGINE = INNODB;

create table Station
(
	station_id int unsigned,
    station_name varchar(30),
    primary key(station_id)
) ENGINE = INNODB;

CREATE TABLE CardUsage
(
	customer_id INT UNSIGNED,
    card_id INT UNSIGNED,
    station_id INT UNSIGNED,
    latest_expense int,
    latest_date date,
    foreign key(customer_id) references Customer(customer_id),
    foreign key(card_id) references Card(card_id),
    foreign key(station_id) references Station(station_id)
) engine = INNODB;

create table CardOwner
(
	customer_id int unsigned,
    card_id int unsigned,
    primary key(customer_id, card_id),
    foreign key(customer_id) references Customer(customer_id),
    foreign key(card_id) references Card(card_id)
) engine = INNODB;

insert into customer values ('1','Alan');
insert into customer values ('2','Bob');
insert into customer values ('3','Cindy');
insert into customer values ('4','David');

insert into card values ('1','-10');
insert into card values ('2','-4');
insert into card values ('3','30');
insert into card values ('4','-2');
insert into card values ('5','-1');
insert into card values ('6','10');

insert into station values ('1','Wan Chai');
insert into station values ('2','Central');
insert into station values ('3','Admiralty');

insert into cardusage values ('1','1','2','12','2020-02-25');
insert into cardusage values ('1','2','2','8','2020-02-25');
insert into cardusage values ('2','3','3','4','2020-02-26');
insert into cardusage values ('2','4','3','6','2020-02-24');
insert into cardusage values ('3','6','3','4','2020-02-24');
insert into cardusage values ('4','5','2','12','2020-02-24');
insert into cardusage values ('4','5','1','10','2020-02-24');
insert into cardusage values ('4','5','1','12','2020-02-24');

insert into cardowner values ('1','1');
insert into cardowner values ('1','2');
insert into cardowner values ('2','3');
insert into cardowner values ('2','4');
insert into cardowner values ('3','6');
insert into cardowner values ('4','5');
