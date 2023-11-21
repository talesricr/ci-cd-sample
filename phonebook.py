class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            return(f"Contact {name} successfully added!")
        else:
            return(f"Contact {name} already exists.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return(f"Contact {name} successfully removed!")
        else:
            return(f"Contact {name} was not found.")

    def find_contact(self, name):
        if name in self.contacts:
            return(f"Name: {name}, Phone: {self.contacts[name]}")
        else:
            return(f"Contact {name} was not found.")

    def list_contacts(self):
        if len(self.contacts) == 0:
            return("The phonebook is empty.")
        else:
            contactList = {}
            for name, phone in self.contacts.items():
                contactList[name] = phone
            return contactList

