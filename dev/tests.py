import unittest
import os
from system import *
from werkzeug.security import generate_password_hash

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def tearDown(self):
        os.remove("crash_course.db")

    def test_add_single_user(self):
        user = self.system.user_manager.add_user("Khu",
                                                 "password",
                                                 "Kent",
                                                 "Hu",
                                                 "khu.1998@icloud.com",
                                                 "17/06/1998")
        self.assertEqual(user.get_id(), 1)
        self.assertEqual(user.get_username(), "Khu")
        self.assertEqual(user.get_hash_pw(),
                         generate_password_hash("password"))
        self.assertEqual(user.get_fname(), "Kent")
        self.assertEqual(user.get_lname(), "Hu")
        self.assertEqual(user.get_email(), "khu.1998@icloud.com")
        self.assertEqual(user.get_dob(), "17/06/1998")

if __name__ == '__main__':
    unittest.main()
