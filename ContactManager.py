# Contact manager with the ability to add, delete,search
import sys


class Contact:
    def __init__(self, name, number, email, website, birth_day):
        self.name = name
        self.number = number
        self.email = email
        self.website = website
        self.birth_day = birth_day

    def __repr__(self):
        return """
        Name:       {}
        Number:     {}
        Email:      {}
        Website:    {}
        birthday:   {}

        """.format(self.name, self.number, self.email, self.website, self.birth_day)


class PhoneBook:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def delete_contact(self):
        contact_to_delete = input('Enter name of contact to delete: ')
        for contact in self.contacts:
            if contact.name == contact_to_delete:
                self.contacts.remove(contact)
        self.display_all_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self):
        contact_to_search = input('Enter name of the contact to search: ')
        for contact in self.contacts:
            if contact.name == contact_to_search:
                print(contact)
        return 'Contact not found in phone book'

    def display_all_contacts(self):
        for contact in self.contacts:
            print(contact)


my_phone_book = PhoneBook()

while True:
    print('Type 1 to Add new contact,2 to delete contact, 3 to search,contact, 4 to display all contact or q to exit: ')
    choice = input()
    if choice == '1':
        name = input('Enter contacts name: ')
        number = input('Enter contacts number: ')
        email = input('Enter contacts email: ')
        website = input('Enter contacts website: ')
        birth_day = input('Enter contacts birthday: ')
        my_phone_book.add_contact(Contact(name=name, number=number, email=email, website=website, birth_day=birth_day))
        for a_contact in my_phone_book.contacts:
            print(a_contact)
    elif choice == '2':
        my_phone_book.delete_contact()
    elif choice == '3':
        my_phone_book.search_contact()
    elif choice == '4':
        my_phone_book.display_all_contacts()
    elif choice == 'q':
        sys.exit()
    else:
        print('Please choose the correct input')
