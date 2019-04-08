import unittest # Importing the unittest module
import pyperclip#helps in copy and paste functions

from credentials import Credentials
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''



    def setUp(self):
         '''
         Function to create social media account credentials before each test
         '''
         self.new_credentials = Credentials('iyaz', 'facebook','iyaz2','account')
    def tearDown(self):
         '''
         tearDown method that executes a set of instructions after every test
         '''
         #User.users_list = []
         Credentials.credentials_list = []

    def test__init__(self):
         '''
         Confirm that instance of credentials creation is as expected
         '''
         self.assertEqual(self.new_credentials.user_name,'iyaz')
         self.assertEqual(self.new_credentials.social_media,'facebook')    #     self.assertEqual(self.new_credentials.password,'account')


    # def test_confirm_user(self):
    #     '''
    #     Function to confirm login details to active user
    #     '''
    #     # self.assertEqual(self.new_credentials.,"John")
    #     # self.assertEqual(self.new_credentials.second_name,"Mwangi")
    #     self.new_user = User('John','Mwangi','locker')
    #     self.new_user.save_user()
    #     userX= User('John','Mwangi', 'locker')
    #     userX.save_user()
    #     #active_from credentials import Credentials
    #     user = Credential.confirm_user('John','locker')
    #     self.assertTrue(active_user)

    def test_save_credentials(self):
         '''
         Test and confirm that the new credential information is being saved
         '''
         self.new_credentials.save_credentials()
         self.assertEqual(len(Credentials.credentials_list),1)



    def test_display_credentials(self):
         '''
         Test to confirm user can view the correct credential details
         '''
         self.new_credentials.save_credentials()
         facebook = Credentials('iyaz','facebook','iyaz2','pwdhappy')
         facebook.save_credentials()
         self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_search_social_media(self):
         '''
         Test to confirm if the method returns the correct social media credential
         '''
         self.new_credentials.save_credentials()
         facebook = Credentials('iyaz','Facebook','iyaz2','account')
         facebook.save_credentials()
         credential_exists = Credentials.search_social_media('Facebook')
         self.assertEqual(credential_exists,facebook)

    def test_copy_password(self):#uses pyperclip
         '''
         Test to check if the copy password method will copy the correct password from social media site specified
         '''
         self.new_credentials.save_credentials()
         facebook = Credentials('iyaz','facebook','iyaz2','account')
         facebook.save_credentials()
         Credentials.copy_password('facebook')
         self.assertEqual(self.new_credentials.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
