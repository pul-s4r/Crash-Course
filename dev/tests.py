"""Unit testing module"""
import unittest
import os
from system import *
from werkzeug.security import check_password_hash

"""Exception modules"""
from exception import EmptyFieldError, SpaceError
from sqlalchemy.exc import IntegrityError

class TestAddUser(unittest.TestCase):
    """Creates the database schema on initialization"""
    def setUp(self):
        self.system = System()

    """Removes the database schema once complete tests"""
    def tearDown(self):
        os.remove("crash_course.db")

    def test_add_single_user(self):
        self.system.user_manager.add_user("Khu",
                                          "password",
                                          "Kent",
                                          "Hu",
                                          "khu.1998@icloud.com",
                                          "17/06/1998",
                                          "Male")
        user = self.system.user_manager.query_user("Khu")
        self.assertEqual(user.get_id(), 1)
        self.assertEqual(user.get_username(), "Khu")
        self.assertTrue(check_password_hash(user.get_hash_pw(), "password"))
        self.assertEqual(user.get_fname(), "Kent")
        self.assertEqual(user.get_lname(), "Hu")
        self.assertEqual(user.get_email(), "khu.1998@icloud.com")
        self.assertEqual(user.get_dob(), "17/06/1998")
        self.assertEqual(user.get_gender(), "Male")

    def test_empty_username(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017",
                                              "Male")

    def test_empty_password(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("username",
                                              "",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017",
                                              "Male")

    def test_empty_fname(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("username",
                                              "password",
                                              "",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017",
                                              "Male")

    def test_empty_lnames(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "",
                                              "email@email.com",
                                              "01/01/2017",
                                              "Male")

    def test_empty_email(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "",
                                              "01/01/2017",
                                              "Male")

    def test_empty_dob(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "",
                                              "Male")

    def test_empty_gender(self):
        with self.assertRaises(EmptyFieldError):
            self.system.user_manager.add_user("username",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017",
                                              "")

    def test_space_in_username(self):
        with self.assertRaises(SpaceError):
            self.system.user_manager.add_user("user name",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email@email.com",
                                              "01/01/2017",
                                              "Male")

    def test_space_in_email(self):
        with self.assertRaises(SpaceError):
            self.system.user_manager.add_user("username",
                                              "password",
                                              "FirstName",
                                              "LastName",
                                              "email @email.com",
                                              "01/01/2017",
                                              "Male")

    def test_duplicate_username(self):
        self.system.user_manager.add_user("Khu",
                                          "password",
                                          "Kent",
                                          "Hu",
                                          "khu.1998@icloud.com",
                                          "17/06/1998",
                                          "Male")
        with self.assertRaises(IntegrityError):
            self.system.user_manager.add_user("Khu",
                                              "password1",
                                              "Kent1",
                                              "Hu1",
                                              "khu1.1998@icloud.com",
                                              "17/07/1998",
                                              "Male1")

    def test_duplicate_email(self):
        self.system.user_manager.add_user("Khu",
                                          "password",
                                          "Kent",
                                          "Hu",
                                          "khu.1998@icloud.com",
                                          "17/06/1998",
                                          "Male")
        with self.assertRaises(IntegrityError):
            self.system.user_manager.add_user("Khu1",
                                              "password1",
                                              "Kent1",
                                              "Hu1",
                                              "khu.1998@icloud.com",
                                              "17/07/1998",
                                              "Male1")

class TestSubscribe(unittest.TestCase):
    """Creates the database schema on initialization"""
    def setUp(self):
        self.system = System()

    """Removes the database schema once complete tests"""
    def tearDown(self):
        os.remove("crash_course.db")

    def test_subscribe(self):
        self.system.user_manager.add_user("Khu",
                                          "password",
                                          "Kent",
                                          "Hu",
                                          "khu.1998@icloud.com",
                                          "17/06/1998",
                                          "Male")
        self.system.user_manager.add_user("username",
                                          "password",
                                          "John",
                                          "Doe",
                                          "JohnDoe@icloud.com",
                                          "17/06/1998",
                                          "Male")

        user = self.system.user_manager.query_user("Khu")
        channel = self.system.user_manager.query_user("username")

        self.system.subscription_manager.subscribe(user.get_id(),
                                                   channel.get_id(),
                                                   date.today())

if __name__ == '__main__':
    unittest.main()
