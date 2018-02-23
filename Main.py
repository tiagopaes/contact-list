
import os
from ContactList import ContactList


class Main(object):
    ContactsList = ContactList()

    def __init__(self):
        self.menu()

    def menu(self):
        print('Contact List')
        print('------------')
        print('(1) - List contacts')
        print('(2) - Add a new contact')
        print('(3) - Edit a contact')
        print('(4) - Remove a contact')
        print('(5) - Exit')
        self.chooseMainMenu(
            raw_input('Choose an option: ')
        )

    def chooseMainMenu(self, option):
        self.clear()

        if option == '1':
            self.listContacts()

        elif option == '2':
            self.add()

        elif option == '3':
            self.update()

        elif option == '4':
            self.remove()

        elif option == '5':
            print('bye')

        else:
            print('Invalid input. Try again...\n')
            self.menu()

    def chooseBack(self, option):
        self.clear()

        if option == '1':
            self.menu()
        elif option == '2':
            print('bye')
        else:
            print('Invalid input. Try again...\n')
            print('(1) Menu - (2) Exit')
            self.chooseBack(
                raw_input('Choose an option: ')
            )

    def clear(self):
        os.system('clear')

    def listContacts(self):
        print('Contacts List')
        print('------------')
        self.ContactsList.listContacts()
        print('------------')
        print('(1) Menu - (2) Exit')
        self.chooseBack(
            raw_input('Choose an option: ')
        )

    def add(self):
        print('Add Contact')
        print('------------')
        name = raw_input('Name: ')
        phone = raw_input('Phone: ')
        self.ContactsList.add(name, phone)
        self.clear()
        print('Contact added!\n')
        self.menu()

    def update(self):
        print('Edit Contact')
        print('------------')
        _id = raw_input('Enter the contact id: ')
        name = raw_input('Name: ')
        phone = raw_input('Phone: ')
        contact = {
            "name": name,
            "phone": phone
        }
        self.ContactsList.update((int(_id) - 1), contact)
        self.clear()
        print('Contact updated!\n')
        self.menu()

    def remove(self):
        print('Remove Contact')
        print('------------')
        _id = raw_input('Enter the contact id: ')
        self.ContactsList.remove((int(_id) - 1))
        self.clear()
        print('Contact deleted!\n')
        self.menu()


app = Main()
