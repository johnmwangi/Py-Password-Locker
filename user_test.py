import unittest # Importing the unittest module
import pyperclip#helps in copy and paste functions

from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = User('John','Mwangi','jonesmwas23@gamail.com', 'locker')

    def test_init_(self):
        '''
        Test to check creation of new user instance
        '''
        self.assertEqual(self.new_user.first_name,'John')
        self.assertEqual(self.new_user.last_name,'Mwangi')
        self.assertEqual(self.new_user.email,'jonesmwas23@gamail.com')
        self.assertEqual(self.new_user.password,'locker')

if __name__ == '__main__':
    unittest.main()

#
#      def test_save_user(self):
#          '''
# #         Test to check if New user information is saved into the users_list
# #         '''
#          self.new_user.save_user()
#          self.assertEqual(len(User.users_list),1)
#
#  if __name__ == '__main__':
#      unittest.main()
