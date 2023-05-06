from game.game import Game
from game.game_view import GameView
from base_dao import BaseDao
import mysql.connector

class GameDao(BaseDao):

    def generate_games(self, roundId, teamId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            args = [roundId, teamId]
            cursor.callproc("prc_generate_games", args)
            
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_games(self, roundId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_game =  ("SELECT game_id, white_player, black_player, winner, round, status, arbiter "
                           "FROM  chess_tournament.game_view WHERE round_id = %s")
            data_game = (roundId, )

            cursor.execute(read_game, data_game)
            records = cursor.fetchall()
            games = []

            for record in records:
                game = GameView(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
                games.append(game)

            cursor.close()
            connection.close()
            return games
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def read_game(self, gameId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_game =  ("SELECT game_id, white_player_id, black_player_id, winner_id, round_id, status_cd, arbiter_id "
                           "FROM  chess_tournament.game WHERE game_id = %s")
            data_game = (gameId, )

            cursor.execute(read_game, data_game)
            
            record = cursor.fetchone()
            game = Game(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

            cursor.close()
            connection.close()
            return game
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_game(self, game):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_game =  ("INSERT INTO chess_tournament.game "
                          "(white_player_id, black_player_id, winner_id, round_id, status_cd, arbiter_id) "
                          "VALUES (%s, %s, %s, %s, %s, %s)")
            data_game = (game.whitePlayerId, game.blackPlayerId, None if game.winnerId == 0 else game.winnerId, game.roundId, game.statusCd, game.arbiterId)

            cursor.execute(add_game, data_game)
            id = cursor.lastrowid
            game.gameId = id

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_game(self, game):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_game =  ("UPDATE chess_tournament.game "
                             "SET white_player_id = %s, black_player_id = %s, winner_id = %s, round_id = %s, status_cd = %s, arbiter_id = %s "
                             "WHERE game_id = %s")
            data_game = (game.whitePlayerId, game.blackPlayerId, None if game.winnerId == 0 else game.winnerId, game.roundId, game.statusCd, game.arbiterId, game.gameId, )

            cursor.execute(update_game, data_game)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_game(self, gameId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_game =  ("DELETE FROM chess_tournament.game "
                                  "WHERE game_id = %s")
            data_game = (gameId, )

            cursor.execute(delete_game, data_game)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        