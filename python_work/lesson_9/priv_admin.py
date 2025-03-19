from user_class import User

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
    def __init__(self, username):
        self.privileges = [
            'view logs',
            'edit settings',
            'manage users',
            'access confidential data',
            'override permissions',
            'generate reports',
            'perform system updates'
        ]
        self.username = username
    
    def show_privileges(self):
        print(f'{self.username} is granted these privileges:')
        for privilege in self.privileges:
            print(f'\t{privilege.title()}')


class Admin(User):
    '''A class to model admin level privileges inherited from User
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
    permissions: cls
        A class to model user permissions. See class Privileges.
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
        super().__init__(first_name,
                         last_name, 
                         email_address,
                         username,
                         date_of_birth)
        self.permissions = Privileges(self.username)