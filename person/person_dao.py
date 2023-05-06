from person.person import Person
from base_dao import BaseDao
import mysql.connector

class PersonDao(BaseDao):
    def get_persons(self):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_person =  ("SELECT person_id, first_name, last_name, gender, email_address, phone_number, "
                          "address_line_1, address_line_2, city, state, zip "
                           "FROM  chess_tournament.person")
            cursor.execute(read_person)
            records = cursor.fetchall()
            persons = []

            for record in records:
                person = Person(record[0], record[1], record[2], record[3], record[4], 
                                record[5], record[6], record[7], record[8], record[9], record[10])
                persons.append(person)

            cursor.close()
            connection.close()
            return persons
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def get_persons_by_name(self, name):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            
            read_person =  ("SELECT person_id, first_name, last_name, gender, email_address, "
                            "phone_number, address_line_1, address_line_2, city, state, zip "
                            "FROM chess_tournament.person "
                            "WHERE lower(first_name) LIKE %s OR lower(last_name) LIKE %s")
            data_person = ("%"+name.lower()+"%", "%"+name.lower()+"%",)
            cursor.execute(read_person, data_person)
            records = cursor.fetchall()
            persons = []

            for record in records:
                person = Person(record[0], record[1], record[2], record[3], record[4], 
                                record[5], record[6], record[7], record[8], record[9], record[10])
                persons.append(person)

            cursor.close()
            connection.close()
            return persons
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def read_person(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            read_person =  ("SELECT person_id, first_name, last_name, gender, email_address, "
                            "phone_number, address_line_1, address_line_2, city, state, zip "
                            "FROM  chess_tournament.person WHERE person_id = %s")
            data_person = (personId,)

            cursor.execute(read_person, data_person)
            
            record = cursor.fetchone()
            person = Person(record[0], record[1], record[2], record[3], record[4], record[5], 
                            record[6], record[7], record[8], record[9], record[10])

            cursor.close()
            connection.close()
            return person
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()   

    def insert_person(self, person):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            add_person =  ("INSERT INTO chess_tournament.person "
                        "(first_name, last_name, gender, email_address, phone_number, address_line_1, address_line_2, city, state, zip)"
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data_person = (person.firstName, person.lastName, person.gender, person.emailAddress, person.phoneNumber, 
                           person.addressLine1, person.addressLine2, person.city, person.state, person.zip)

            cursor.execute(add_person, data_person)
            person_id = cursor.lastrowid
            person.personId = person_id

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def update_person(self, person):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            update_person =  ("UPDATE chess_tournament.person "
                            "SET first_name = %s, last_name = %s, gender = %s, email_address = %s, "
                            "phone_number = %s, address_line_1 = %s, address_line_2 = %s, city = %s, state = %s, zip = %s "
                            "WHERE person_id = %s")
            data_person = (person.firstName, person.lastName, person.gender, person.emailAddress, 
                            person.phoneNumber, person.addressLine1, person.addressLine2, 
                            person.city, person.state, person.zip, person.personId)

            cursor.execute(update_person, data_person)

            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()

    def delete_person(self, personId):
        try: 
            connection = self.get_connection()
            cursor = connection.cursor()
            delete_person =  ("DELETE FROM chess_tournament.person "
                            "WHERE person_id = %s")
            data_person = (personId,)

            cursor.execute(delete_person, data_person)
            
            connection.commit()

            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print(err)
            cursor.close()
            connection.close()        