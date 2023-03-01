import db


class Phonebook:
    def __init__(self):
        self.all_contacts = {}

    def add_contact(self, name, phone_number):
        # should take contacts to a database somewhere
        self.name = name
        self.phone_number = phone_number
        self.all_contacts[self.name] = self.phone_number

    def check_duplicate_contact(self):
        pass

    def update_contact(self):
        pass

    def delete_contact(self):
        pass
