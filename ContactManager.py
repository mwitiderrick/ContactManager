class NewContact:
    def __init__(self):
        self.name = ''
        self.number = ''
        self.email = ''
        self.website = ''
        self.birth_day = ''

    def create_contact(self):
        self.name = input('Enter contacts name: ')
        self.number = input('Enter contacts number: ')
        self.email = input('Enter contacts email: ')
        self.website = input('Enter contacts website: ')
        self.birth_day = input('Enter contacts birthday: ')
        new_contact = {'name': self.name, 'number': self.number, 'website': self.website, 'birthday': self.birth_day}
        # print(new_contact)


derrick = NewContact()
derrick.create_contact()


