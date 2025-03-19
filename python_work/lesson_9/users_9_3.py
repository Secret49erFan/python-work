# practice 2/3/25
# chapter 9
# users
from datetime import datetime

class User:
    '''
    A class to model a user profile.

    Attributes
    ----------
    first_name: str
        The first name of the user.
    last_name: str
        The last name of the user.
    email_address: str
        The e-mail address of the user.
    username:
        A unique identifier that user choose for themselves.
    date_of_birth:
        The date of birth of the user. Need to import datetime.
        Date format: %m-%d-%Y
    login_attempts: int
        The total of login attempts by the user.
    
    Methods
    -------
    describe_user():
        Output a neatly formated description of the user info to console. 
    greet_user():
        Output a personlized greeting to the user to console.
    convert_date():
        Converts dob_str to a datetime object.
        Date format: %m-%d-%Y
    increment_login_attempts():
        Increment the value of login_attempts by 1
    '''
    def __init__(self, 
                 first_name,
                 last_name, 
                 email_address,
                 username,
                 date_of_birth):
        '''Initiating all necessary attributes for the User class.'''
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.username = username
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def convert_date(self):
        '''Converts date_of_birth to a datetime object.'''
        return datetime.strptime(self.date_of_birth, '%m-%d-%Y')
        # date_of_birth = datetime.strptime(self.date_of_birth, '%m-%d-%Y')
        # return date_of_birth

    def describe_user(self):
        '''Output a neatly formated description of the user info.'''
        dob_datetime = self.convert_date()
        print('\nThank you for creating a new profile.')
        print('Here is a list of your information:')
        print(f'\tFirst Name: {self.first_name.title()}')
        print(f'\tLast Name: {self.last_name.title()}')
        print(f'\tE-mail Address: {self.email_address}')
        print(f'\tUsername: {self.username}')
        print(f'\tDate of Birth: {dob_datetime}')

    def greet_user(self):
        '''Output a personalized greeting to the user.'''
        print(f'Thank you for joining, {self.first_name.title()} {self.last_name.title()}!')
        print(f'You shall henceforth be known as {self.username}. Welcome to Euphoric Pixel.')

    def increment_login_attempts(self):
        '''Increment the value of login_attempts by 1'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Warning! Reset login_attempts to 0.'''
        self.login_attempts = 0


first_user = User('alex',
                  'flores',
                  'noemail@thistime.com',
                  'Secret49erFan',
                  '5-15-1990')
second_user = User('mikey',
                   'snodgrass',
                   'this@that.com',
                   'username',
                   '5-16-1990')
first_user.describe_user()
first_user.greet_user()
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.reset_login_attempts()
print(first_user.login_attempts)
second_user.describe_user()
second_user.greet_user()
second_user.increment_login_attempts()
second_user.increment_login_attempts()
print(second_user.login_attempts)
second_user.reset_login_attempts()
print(second_user.login_attempts)


class Privileges:
    '''
    A class to hold admin-level privileges.
    
    Attributes
    ----------
    privileges: lst
        A list of admin-level privileges.
    Methods
    -------
    show_privileges():
        Displays a list of admin-level privileges.
    '''

    def __init__(self):
        self.privileges = [
            'view logs',
            'edit settings',
            'manage users',
            'access confidential data',
            'override permissions',
            'generate reports',
            'perform system updates'
        ]
    def show_privileges(self):
        print('This user is granted these privileges:')
        for privilege in self.privileges:
            print(f'\t{privilege.title()}')


class Admin(User):
    '''A class to model admin level privileges inherited from User'''
    
    def __init__(self, 
                 first_name,
                 last_name, 
                 email_address,
                 username,
                 date_of_birth):
        super().__init__(first_name,
                         last_name, 
                         email_address,
                         username,
                         date_of_birth)
        self.permissions = Privileges()

super_user = Admin('foo',
                   'bar',
                   'foo@bar.net',
                   'foobar',
                   '5-5-1990')

super_user.describe_user()
#super_user.show_privileges()
super_user.permissions.show_privileges()