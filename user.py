import pyperclip
import string
import random

class User:
    """
    Class that generates new instances of users
    """

    def __init__(self,first_name,last_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name:User first name.
            last_name :User last name.
            password:User password.

        '''
        ...
    def __init__(self,first_name,last_name,phone_number,email):
        ...

    def __init__(self,first_name,last_name,phone_number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

class user:
    """
    Class that generates new instances of users.
    """

    users_list = [] # Empty users list

    def __init__(self,first_name,last_name,password):
        '''
        Method to define the properties of the object
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save user details method into users_list
        '''
        User.users_list.append(self)
