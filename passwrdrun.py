#! /usr/bin/env python3
import pyperclip
from smaccounts import User, Credential

def create_user(firstname,lastname,password):
    '''
    Function to create user ac
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
