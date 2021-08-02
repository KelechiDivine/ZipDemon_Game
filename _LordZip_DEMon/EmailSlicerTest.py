import unittest
import EmailSlicer as es

class Email_Slicer(unittest.TestCase):
    
    def test_email_slicer(self):
        user_email= es.email_slicer(nonso@gmail)
        # self.assertEqual(nonso@gmail.com, user_email)
        self.assertTrue(nonso, True)


if __name__ == '__main__':
    unittest.main()
