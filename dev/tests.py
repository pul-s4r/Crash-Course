import unittest
import os
from system import *
from werkzeug.security import check_password_hash
from exception import EmptyFieldError, SpaceError

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def tearDown(self):
        os.remove("crash_course.db")

    def test_add_single_user(self):
        self.system.user_manager.add_user("Khu",
                                          "password",
                                          "Kent",
                                          "Hu",
                                          "khu.1998@icloud.com",
                                          "17/06/1998")
        user = self.system.user_manager.query_user("Khu")
        self.assertEqual(user.get_id(), 1)
        self.assertEqual(user.get_username(), "Khu")
        self.assertTrue(check_password_hash(user.get_hash_pw(), "password"))
        self.assertEqual(user.get_fname(), "Kent")
        self.assertEqual(user.get_lname(), "Hu")
        self.assertEqual(user.get_email(), "khu.1998@icloud.com")
        self.assertEqual(user.get_dob(), "17/06/1998")

    def test_empty_username(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017")

    def test_empty_password(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("username",
                                              "",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017")

    def test_empty_fname(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("username",
                                              "password",
                                              "",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017")

    def test_empty_lnames(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "",
                                              "email@email.com",
                                              "01/01/2017")

    def test_empty_email(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "",
                                              "01/01/2017")

    def test_empty_dob(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "")

    def test_space_in_username(self):
        with self.assertRaises(SpaceError):
            self.system.user_manager.add_user("user name",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017")

    def test_space_in_email(self):
        with self.assertRaises(SpaceError):
            self.system.user_manager.add_user("username",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email @email.com",
                                              "01/01/2017")

if __name__ == '__main__':
    unittest.main()
