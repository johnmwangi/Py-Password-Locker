import pyperclip
import string
import random
from user import User

class Credentials:
    '''
    Class that holds and saves user login details, social media a/c credentials, passwords
    '''
    # Class Variables
    credentials_list =[]

    @classmethod
    def confirm_user(cls,first_name,password):
        '''
		Method that checks if the name and password entered match entries in the users_list
		'''
        active_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user

    def __init__(self,user_name,social_media,account_name,password):
        '''
        Method defining the properties each object will hold
        '''

        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save new user credentials
        '''
        Credentials.credentials_list.append(self)

    def generate_password():
        '''
        Function to generate random passwords for social media accounts
        '''
        pwchar = string.printable
        length = int(input('Enter password length desired: '))
        gen_pwd= ''
        for char in range(length):
            gen_pwd += random.choice(pwchar)
        return gen_pwd


    @classmethod
    def display_credentials(cls):
        '''
        Class method to display the list of saved credentials
        '''
        return cls.credentials_list

    @classmethod
    def search_social_media(cls, social_media):
        '''
        Method that acccepts social media name and returns credentials matching the social media name
        '''
        for credential in cls.credentials_list:
            if credential.social_media == social_media:
                return credential

    @classmethod
    def copy_password(cls,social_media):
        '''
		Class method that copies a credential's password of a specific social media site after the credential's social media name is entered
		'''
        collect_pass = Credentials.search_social_media(social_media)
        return pyperclip.copy(collect_pass.password)
