from player.player import Player
from base_dao import BaseDao
import mysql.connector

class PlayerDao(BaseDao):
    def read_player(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_player =  ("SELECT person_id, rating, rating_level "
                            "FROM  chess_tournament.player WHERE person_id = %s")
            data_player = (personId, )

            cursor.execute(read_player, data_player)
            
            record = cursor.fetchone()
            player = Player(record[0], record[1], record[2])

            cursor.close()
            connection.close()
            return player
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_players(self):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_person =  ("SELECT person_id, rating, rating_level "
                            "FROM  chess_tournament.player")
            cursor.execute(read_person)
            records = cursor.fetchall()
            players = []

            for record in records:
                player = Player(record[0], record[1], record[2])
                players.append(player)

            cursor.close()
            connection.close()
            return players
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_player(self, player):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_player =  ("INSERT INTO chess_tournament.player "
                        "(person_id, rating)"
                        "VALUES (%s, %s)")
            data_player = (player.personId, player.rating, )

            cursor.execute(add_player, data_player)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_player(self, player):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_player =  ("UPDATE chess_tournament.player "
                            "SET rating = %s "
                            "WHERE person_id = %s")
            data_player = (player.rating, player.personId, )

            cursor.execute(update_player, data_player)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_player(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_player =  ("DELETE FROM chess_tournament.player "
                            "WHERE person_id = %s")
            data_player = (personId, )

            cursor.execute(delete_player, data_player)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        