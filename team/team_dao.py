from team.team import Team
from base_dao import BaseDao
import mysql.connector

class TeamDao(BaseDao):
    def read_team(self, teamId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_team =  ("SELECT team_id, team_name, team_desc "
                            "FROM  chess_tournament.team WHERE team_id = %s")
            data_team = (teamId, )

            cursor.execute(read_team, data_team)
            
            record = cursor.fetchone()
            team = Team(record[0], record[1], record[2])

            cursor.close()
            connection.close()
            return team
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_teams(self):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_team =  ("SELECT team_id, team_name, team_desc "
                           "FROM  chess_tournament.team")
            cursor.execute(read_team)
            records = cursor.fetchall()
            teams = []

            for record in records:
                team = Team(record[0], record[1], record[2])
                teams.append(team)

            cursor.close()
            connection.close()
            return teams
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_team(self, team):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_team =  ("INSERT INTO chess_tournament.team "
                        "(team_name, team_desc)"
                        "VALUES (%s, %s)")
            data_team = (team.teamName, team.teamDesc, )

            cursor.execute(add_team, data_team)
            team_id = cursor.lastrowid
            team.teamId = team_id

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_team(self, team):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_team =  ("UPDATE chess_tournament.team "
                            "SET team_name = %s, team_desc = %s "
                            "WHERE team_id = %s")
            data_team = (team.teamName, team.teamDesc, team.teamId, )

            cursor.execute(update_team, data_team)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_team(self, teamId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_team =  ("DELETE FROM chess_tournament.team "
                            "WHERE team_id = %s")
            data_team = (teamId, )

            cursor.execute(delete_team, data_team)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        