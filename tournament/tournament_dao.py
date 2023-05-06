from tournament.tournament import Tournament
from base_dao import BaseDao
import mysql.connector

class TournamentDao(BaseDao):
    def read_tournament(self, tournamentId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_tournament =  ("SELECT tournament_id, tournament_name, "
                                "address_line_1, address_line_2, city, state, zip "
                                "FROM  chess_tournament.tournament WHERE tournament_id = %s")
            data_tournament = (tournamentId, )

            cursor.execute(read_tournament, data_tournament)
            
            record = cursor.fetchone()
            tournament = Tournament(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

            cursor.close()
            connection.close()
            return tournament
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_tournaments(self):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_tournament =  ("SELECT tournament_id, tournament_name, address_line_1, address_line_2, city, state, zip "
                                "FROM  chess_tournament.tournament")
            cursor.execute(read_tournament)
            records = cursor.fetchall()
            tournaments = []

            for record in records:
                tournament = Tournament(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
                tournaments.append(tournament)

            cursor.close()
            connection.close()
            return tournaments
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close() 

    def insert_tournament(self, tournament):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_tournament =  ("INSERT INTO chess_tournament.tournament "
                        "(tournament_name, address_line_1, address_line_2, city, state, zip)"
                        "VALUES (%s, %s, %s, %s, %s, %s)")
            data_tournament = (tournament.tournamentName, tournament.addressLine1, tournament.addressLine2, tournament.city, tournament.state, tournament.zip, )

            cursor.execute(add_tournament, data_tournament)
            id = cursor.lastrowid
            tournament.tournamentId = id

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_tournament(self, tournament):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_tournament =  ("UPDATE chess_tournament.tournament "
                                  "SET tournament_name = %s, address_line_1 = %s, address_line_2 = %s, city = %s, state = %s, zip = %s "
                                  "WHERE tournament_id = %s")
            data_tournament = (tournament.tournamentName, tournament.addressLine1, tournament.addressLine2, tournament.city, tournament.state, tournament.zip, tournament.tournamentId, )

            cursor.execute(update_tournament, data_tournament)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_tournament(self, tournamentId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_tournament =  ("DELETE FROM chess_tournament.tournament "
                                  "WHERE tournament_id = %s")
            data_tournament = (tournamentId, )

            cursor.execute(delete_tournament, data_tournament)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        