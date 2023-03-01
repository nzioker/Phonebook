import sqlite3


class PhonebookDB:
    def __init__(self):
        self.connection = sqlite3.connect("phonebook.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def insert_to_db(self, id, name, phone_number, email_address, fax):
        self.cursor.execute(
            """
        INSERT INTO Contacts VALUES (?,?,?,?,?)
        """,
            (id, name, phone_number, email_address, fax),
        )
        self.connection.commit()

    def fetch_all_contacts(self):
        self.cursor.execute(""" SELECT * from Contacts""")
        all_contacts = [x for x in self.cursor.fetchall()]
        return all_contacts

    def fetch_one_contact(self, Id):
        self.cursor.execute("SELECT * FROM Contacts WHERE Id = (?)", (Id,))
        res = [x for x in self.cursor.fetchall()]
        return res

    def update_db(self, Id, name, phone, email, fax):
        self.cursor.execute(
            f"UPDATE Contacts SET Name={name}, Phone={phone}, Email={email}, Fax={fax} WHERE Id = ?",
            (Id,),
        )
        self.connection.commit()

    def delete_one_contact(self, Id):
        self.cursor.execute("DELETE FROM Contacts WHERE Id = ?", (Id,))
        self.connection.commit()
