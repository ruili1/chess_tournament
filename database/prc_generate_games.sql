delimiter //
create procedure chess_tournament.prc_generate_games(in n_round_id int, in n_team_id int)
begin
	declare sel_arbiter_id, white_id, black_id int;
    declare arbiter_cntr, arbiter_total, done int;
    declare order_num decimal;
	declare c_player cursor for
		select p.person_id, rand() order_num
		from chess_tournament.player p
		join chess_tournament.round r
		on p.rating_level = r.rating_level
		where r.round_id = n_round_id
        order by 2;
	declare c_arbiter cursor for
		select tm.person_id, rand() order_num
		from chess_tournament.team_member tm
		where tm.team_id = n_team_id
        order by 2;        
	declare continue handler for not found set done := 1;
    
    set done := 0;

	delete from chess_tournament.game
    where round_id = n_round_id;
    
    open c_player;
    player_loop: loop
		fetch c_player into white_id, order_num;
        if done = 1 then
			close c_player;
            leave player_loop;
		end if;
        fetch c_player into black_id, order_num;
		if done = 1 then
			set black_id := null;
		end if;
        insert into chess_tournament.game
        (white_player_id, black_player_id, winner_id, round_id, status_cd, arbiter_id)
        values 
        (white_id, black_id, null, n_round_id, 'NEW', null);        
    end loop player_loop;
    
    set done := 0;
    set arbiter_cntr := 0;
    select count(*) into arbiter_total from chess_tournament.team_member where team_id = n_team_id;
    
    open c_arbiter;
    arbiter_loop: loop
		fetch c_arbiter into sel_arbiter_id, order_num;
--         select concat('arbiter selected is ', sel_arbiter_id);
--         select concat('arbiter counter is ', arbiter_cntr);
--         select concat('arbiter total is ', arbiter_total);
--         select concat('round id is ', n_round_id);
--         select concat('team id is ', n_team_id);
--         select concat('total number of games to update: ', count(*))
--         from chess_tournament.game
--         where round_id = n_round_id
--         and game_id%arbiter_total = arbiter_cntr;
        if done = 1 then
			close c_arbiter;
            leave arbiter_loop;
		end if;
        
        update chess_tournament.game
        set arbiter_id = sel_arbiter_id
        where round_id = n_round_id
        and game_id%arbiter_total = arbiter_cntr;
        
        set arbiter_cntr := arbiter_cntr + 1;
    end loop arbiter_loop;
    
    commit;
end;//
delimiter ;