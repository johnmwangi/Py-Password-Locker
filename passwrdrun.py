#! /usr/bin/env python3
import pyperclip
from user  import User

def create_user(firstname,lastname,password):
    '''
    Function to create user account
    '''
    new_user = User(firstname,lastname,password)
    return new_user

def save_user(user):
    '''
    Function to save new users
    '''
    User.save_user(user)

def authenticate_user(first_name,password):
    '''
    Function to verify user is enabled before launching the credentials
    '''
    confirm_user = Credential.confirm_user(first_name,password)
    return confirm_user

def generate_password():
    '''
    Function to automatically gen password
    '''
    gen_pwd = Credential.generate_password()
    return gen_pwd

    def create_credential(user_name,social_media,account_name,password):
    '''
    Function creating new credentials
    '''
    new_credential = Credential(user_name,social_media,account_name,password)
    return new_credential

def save_credential(credential):
    '''
    Saves new credentials
    '''
    Credential.save_credentials(credential)

def display_credentials():
    '''
    Function to display_credentials saved by user
    '''
    return Credential.display_credentials()

def copy_password(social_media):
    '''
    Function to copy credential details and paste then in clipboard
    '''
    return Credential.copy_password(social_media)

    def main():
	print(' ')
	print('checkout! Password Locker.')
	while True:
		print(' ')
		print("-"*70)
		print('Use these codes to navigate: \n ca-Create Password Locker Account \n li-Log Into Password Locker to access your credentials \n ex-Exit')
		short_code = input('Enter an option: ').lower().strip()
		if short_code == 'ex':
			break

            elif short_code == 'ca':
			print("-"*70)
			print(' ')
			print('To create a new password locker account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Password Locker Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'li':
			print("-"*70)
			print(' ')
			print('To login, enter your password locker account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = authenticate_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*70)
					print('Navigation codes: \n cc-Create Social Media credentials\n dc-Display Credentials \n copy-Copy Social Media Password \n ex-Exit')
					short_code = input('Choose an option: ').lower().strip()
					print("-"*70)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break

                        elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						social_media = input('Enter the social media name- ').strip()
						account_name = input('Enter your social media handle - ').strip()
