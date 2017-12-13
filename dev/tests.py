import unittest
import os
from system import *

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def tearDown(self):
        os.remove("crash_course.db")
