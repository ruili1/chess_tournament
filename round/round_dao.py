from round.round import Round
from base_dao import BaseDao
import mysql.connector

class RoundDao(BaseDao):
    def read_round(self, roundId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_round =  ("SELECT round_id, tournament_id, date_format(start_time, '%m/%d/%Y %H:%i'), rating_level "
                           "FROM  chess_tournament.round WHERE round_id = %s")
            data_round = (roundId, )

            cursor.execute(read_round, data_round)
            
            record = cursor.fetchone()
            round = Round(record[0], record[1], record[2], record[3])

            cursor.close()
            connection.close()
            return round
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_rounds(self, tournamentId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_round =  ("SELECT round_id, tournament_id, date_format(start_time, '%m/%d/%Y %H:%i'), rating_level "
                            "FROM  chess_tournament.round "
                            "WHERE tournament_id = %s")
            data_round = (tournamentId,)
            
            cursor.execute(read_round, data_round)
            records = cursor.fetchall()
            rounds = []

            for record in records:
                round = Round(record[0], record[1], record[2], record[3])
                rounds.append(round)

            cursor.close()
            connection.close()
            return rounds
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_round(self, round):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_round =  ("INSERT INTO chess_tournament.round "
                          "(tournament_id, start_time, rating_level) "
                          "VALUES (%s, str_to_date(%s, '%m/%d/%Y %H:%i'), %s)")
            data_round = (round.tournamentId, round.startTime, round.ratingLevel, )

            cursor.execute(add_round, data_round)
            id = cursor.lastrowid
            round.roundId = id

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_round(self, round):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_round =  ("UPDATE chess_tournament.round "
                             "SET tournament_id = %s, start_time = str_to_date(%s, '%m/%d/%Y %H:%i'), rating_level = %s "
                             "WHERE round_id = %s")
            data_round = (round.tournamentId, round.startTime, round.ratingLevel, round.roundId, )

            cursor.execute(update_round, data_round)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_round(self, roundId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_round =  ("DELETE FROM chess_tournament.round "
                                  "WHERE round_id = %s")
            data_round = (roundId, )

            cursor.execute(delete_round, data_round)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        