create database chess_tournament;

create table chess_tournament.person (
	person_id int not null auto_increment,
    first_name varchar(200) not null,
    last_name varchar(200) not null,
    gender varchar(20),
    email_address varchar(500) not null,
    phone_number varchar(100) not null,
    address_line_1 varchar(200) not null,
    address_line_2 varchar(200),
    city varchar(100) not null,
    state varchar(50) not null,
    zip varchar(10) not null,
    primary key (person_id)
);

create table chess_tournament.player (
	person_id int not null,
    rating int not null,
    rating_level int not null,
    primary key (person_id),
    foreign key (person_id) references person(person_id)
);

delimiter $$
create trigger chess_tournament.cal_rating_level_on_insert before INSERT on chess_tournament.player
for each row
begin
	if new.rating < 1200 then
		set new.rating_level = 1200;
	elseif new.rating < 1400 then
		set new.rating_level = 1400;
	elseif new.rating < 1700 then
		set new.rating_level = 1700;
	elseif new.rating < 2100 then
		set new.rating_level = 2100;
	elseif new.rating < 2700 then
		set new.rating_level = 2700;
	else
		set new.rating_level = 10000;
	end if;        
end$$

create trigger chess_tournament.cal_rating_level_on_update before UPDATE on chess_tournament.player
for each row
begin
	if new.rating < 1200 then
		set new.rating_level = 1200;
	elseif new.rating < 1400 then
		set new.rating_level = 1400;
	elseif new.rating < 1700 then
		set new.rating_level = 1700;
	elseif new.rating < 2100 then
		set new.rating_level = 2100;
	elseif new.rating < 2700 then
		set new.rating_level = 2700;
	else
		set new.rating_level = 10000;
	end if;        
end$$

delimiter ;

create table chess_tournament.team (
	team_id int not null auto_increment,
    team_name varchar(100) not null,
    team_desc varchar(500),
    primary key (team_id)
);

create table chess_tournament.worker (
	person_id int not null,
    skill_desc varchar(300),
    primary key (person_id),
    foreign key (person_id) references person(person_id)
);

create table chess_tournament.team_member (
	team_id int not null,
    person_id int not null,
    role_cd varchar(20) not null,
    primary key (team_id, person_id),
    foreign key (team_id) references team(team_id),
    foreign key (person_id) references worker(person_id)
);

create table chess_tournament.tournament (
	tournament_id int not null auto_increment,
    tournament_name varchar(100) not null,
    address_line_1 varchar(200) not null,
    address_line_2 varchar(200),
    city varchar(100) not null,
    state varchar(50) not null,
    zip varchar(10) not null,
    primary key (tournament_id)
);

create table chess_tournament.round (
	round_id int not null auto_increment,
    tournament_id int not null,
    start_time datetime not null,
    rating_level int not null,
    primary key (round_id),
    foreign key (tournament_id) references tournament(tournament_id)
);

create table chess_tournament.game_status (
	status_cd varchar(15) not null,
    status_desc varchar(100) not null,
    primary key (status_cd)
);

create table chess_tournament.game (
	game_id int not null auto_increment,
    white_player_id int not null,
    black_player_id int,
    winner_id int,
    round_id int not null,
    status_cd varchar(5) not null,
    arbiter_id int,
	primary key (game_id),
    foreign key (white_player_id) references player(person_id),
    foreign key (black_player_id) references player(person_id),
    foreign key (winner_id) references player(person_id),
    foreign key (round_id) references round(round_id),
    foreign key (status_cd) references game_status(status_cd),
    foreign key (arbiter_id) references worker(person_id)
);

create view chess_tournament.game_view as
select g.game_id, g.round_id, 
concat(wp.first_name, ', ', wp.last_name) as white_player, concat(bp.first_name, ', ', bp.last_name) as black_player, 
concat(w.first_name, ', ', w.last_name) as winner, date_format(r.start_time, '%m/%d/%Y %H:%i') as round, 
g.status_cd as status, concat(ap.first_name, ', ', ap.last_name) as arbiter
from chess_tournament.game g
join chess_tournament.round r
on g.round_id = r.round_id
join chess_tournament.person wp
on g.white_player_id = wp.person_id
left join chess_tournament.person bp
on g.black_player_id = bp.person_id
left join chess_tournament.person w
on g.winner_id = w.person_id
join chess_tournament.person ap
on g.arbiter_id = ap.person_id;

insert into chess_tournament.game_status
(status_cd, status_desc)
values ('NEW', 'New game arranged but not played');

insert into chess_tournament.game_status
(status_cd, status_desc)
values ('IN_PROGRESS', 'Game in progress');

insert into chess_tournament.game_status
(status_cd, status_desc)
values ('COMPLETE_DRAW', 'Game completed in draw');

insert into chess_tournament.game_status
(status_cd, status_desc)
values ('COMPLETE_BYE', 'Game completed with bye');

insert into chess_tournament.game_status
(status_cd, status_desc)
values ('COMPLETE', 'Game completed with winner');

commit;

