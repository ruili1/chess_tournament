from worker.worker import Worker
from worker.worker_view import WorkerView
from base_dao import BaseDao
import mysql.connector

class WorkerDao(BaseDao):
    def read_worker(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_worker =  ("SELECT person_id, skill_desc "
                            "FROM  chess_tournament.worker WHERE person_id = %s")
            data_worker = (personId, )

            cursor.execute(read_worker, data_worker)
            
            record = cursor.fetchone()
            worker = Worker(record[0], record[1])

            cursor.close()
            connection.close()
            return worker
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_worker_by_skill(self, skill):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_worker =  ("SELECT w.person_id, p.first_name, p.last_name, w.skill_desc "
                            "FROM chess_tournament.worker w "
                            "JOIN chess_tournament.person p "
                            "ON w.person_id = p.person_id "
                            "WHERE lower(w.skill_desc) LIKE %s")
            data_worker = ("%"+skill.lower()+"%", )
            cursor.execute(read_worker, data_worker)
            records = cursor.fetchall()
            workers = []

            for record in records:
                worker = WorkerView(record[0], record[1], record[2], record[3])
                workers.append(worker)

            cursor.close()
            connection.close()
            return workers
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   
            
    def get_workers(self):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_worker =  ("SELECT person_id, skill_desc "
                            "FROM  chess_tournament.worker")
            cursor.execute(read_worker)
            records = cursor.fetchall()
            workers = []

            for record in records:
                worker = Worker(record[0], record[1])
                workers.append(worker)

            cursor.close()
            connection.close()
            return workers
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_worker(self, worker):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_worker =  ("INSERT INTO chess_tournament.worker "
                        "(person_id, skill_desc)"
                        "VALUES (%s, %s)")
            data_worker = (worker.personId, worker.skillDesc, )

            cursor.execute(add_worker, data_worker)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_worker(self, worker):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_worker =  ("UPDATE chess_tournament.worker "
                              "SET skill_desc = %s "
                              "WHERE person_id = %s")
            data_worker = (worker.skillDesc, worker.personId, )

            cursor.execute(update_worker, data_worker)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_worker(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_worker =  ("DELETE FROM chess_tournament.worker "
                            "WHERE person_id = %s")
            data_worker = (personId, )

            cursor.execute(delete_worker, data_worker)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        