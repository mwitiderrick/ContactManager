# Contact manager with the ability to add, delete,search
import sys
import csv


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
        line = 0
        with open('contacts.csv', 'r') as contact_file:
            for each_line in contact_file:
                if line == 0:
                    line += 1
                    continue
                # if len(each_line) > 1:
                contact = each_line.strip('\n').split(',')
                contact = {'Name': contact[0], 'Number': contact[1], 'Email': contact[2], 'Website': contact[3],
                           'Birthday': contact[4]}
                self.contacts.append(contact)

        print(self.contacts)

    def delete_contact(self):
        contact_to_delete = input('Enter name of contact to delete: ')
        for contact in self.contacts:
            if contact['Name'] == contact_to_delete:
                self.contacts.remove(contact)
        self.display_all_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self):
        contact_to_search = input('Enter name of the contact to search: ')
        for contact in self.contacts:
            if contact['Name'] == contact_to_search:
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
        my_phone_book.add_contact({'Name': name, 'Number': number, 'Email': email, 'Website': website,
                           'Birthday': birth_day})
        for a_contact in my_phone_book.contacts:
            print(a_contact)
    elif choice == '2':
        my_phone_book.delete_contact()
    elif choice == '3':
        my_phone_book.search_contact()
    elif choice == '4':
        my_phone_book.display_all_contacts()
    elif choice == 'q':
        with open('contacts.csv', 'w') as contact_file:
            contact_file.write('Name,Number,Email,Website,Birthday\n')
            for contact in my_phone_book.contacts:
                print(contact)
                name = contact['Name']
                number = contact['Number']
                email = contact['Email']
                website = contact['Website']
                birth_day = contact['Birthday']
                comma_separated_contacts = name+','+number+','+email+','+website+','+birth_day+'\n'
                contact_file.write(comma_separated_contacts)
            sys.exit()
    else:
        print('Please choose the correct input')
