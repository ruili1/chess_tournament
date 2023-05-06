from team.team_member import TeamMember
from team.team_member_view import TeamMemberView
from base_dao import BaseDao
import mysql.connector

class TeamMemberDao(BaseDao):
    def read_team_member(self, teamId, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_team_member =  ("SELECT team_id, person_id, role_cd "
                                 "FROM  chess_tournament.team_member WHERE team_id = %s AND person_id = %s")
            data_team_member = (teamId, personId, )

            cursor.execute(read_team_member, data_team_member)
            
            record = cursor.fetchone()
            teamMember = TeamMember(record[0], record[1])

            cursor.close()
            connection.close()
            return teamMember
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_team_members(self, teamId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_member =  ("SELECT tm.team_id, tm.person_id, p.first_name, p.last_name, tm.role_cd, w.skill_desc "
                            "FROM chess_tournament.team_member tm "
                            "JOIN chess_tournament.person p "
                            "ON tm.person_id = p.person_id "
                            "JOIN chess_tournament.worker w "
                            "ON tm.person_id = w.person_id "
                            "WHERE tm.team_id = %s")
            data_member = (teamId,)
            cursor.execute(read_member, data_member)
            records = cursor.fetchall()
            members = []

            for record in records:
                member = TeamMemberView(record[0], record[1], record[2], record[3], record[4], record[5])
                members.append(member)

            cursor.close()
            connection.close()
            return members
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()           

    def insert_team_member(self, teamMember):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_team_member =  ("INSERT INTO chess_tournament.team_member "
                                "(team_id, person_id, role_cd) "
                                "VALUES (%s, %s, %s)")
            data_team_member = (teamMember.teamId, teamMember.personId, teamMember.roleCd, )

            cursor.execute(add_team_member, data_team_member)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_team_member(self, teamMember):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_team_member =  ("UPDATE chess_tournament.team_member "
                                   "SET role_cd = %s "
                                   "WHERE team_id = %s AND person_id = %s")
            data_team_member = (teamMember.roleCd, teamMember.teamId, teamMember.personId, )

            cursor.execute(update_team_member, data_team_member)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_team_member(self, teamId, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_team_member =  ("DELETE FROM chess_tournament.team_member "
                                   "WHERE team_id = %s AND person_id = %s")
            data_team_member = (teamId, personId, )

            cursor.execute(delete_team_member, data_team_member)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        