import unittest
from _User_SignUp import *

class TestEmailInRightFormat(unittest.TestCase):
    
    def test_email_field_is_valid(self):
        user_valid_email = UserSignUp()
        user_valid_email.set_email("Kelechi@gmail.com")
        self.assertEqual("Kelechi@gmail.com", user_valid_email.getEmail())
        
    def test_email_field_is_empty(self):
        user_wrong_email_format = UserSignUp()
        user_wrong_email_format.set_email("kelechi")
        self.assertEqual("kelechi", user_wrong_email_format.getEmail())
        
    def test_email_field_is_empty(self):
        user_empty_email = UserSignUp()
        user_empty_email.set_email("")
        self.assertEqual("", user_empty_email.getEmail())
        
    #
    # def test_mobile_number_is_valid(self):
    #     user_mobile = UserSignUp()
    #     user_mobile.setUserMobile(1234567890)
    #     self.assertEqual("08082167764", user_mobile.getUserMobile())
    #
    # def test_uuid_mobile_number_is_present_in_mobile(self):
    #     uuid_mobile = UserSignUp()
    #     uuid_mobile.setUserMobile("+234 80821 677 64")
    #     self.assertEqual("+234 80821 677 64", uuid_mobile.getUserMobile())
        
    def test_first_name_is_not_null(self):
        user_first_name = UserSignUp()
        user_first_name.setFirstName("")
        self.assertEqual("", user_first_name.getFirstName())
        
        
    # def test_mobile_doesnot_exit_11(self):
    #     exit_mobile_number = UserSignUp()
    #     exit_mobile_number.setUserMobile("08082167764111")
    #     self.assertEqual("08082167764111", exit_mobile_number.getUserMobile())
    
    
if __name__ == '__main__':
    unittest.main()
