#!/usr/bin/python3
""" State test"""
import unittest
import pep8
from models.state import State

class State_testing(unittest.TestCase):
    """BaseModel check"""
    def testpep8(self):
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/state.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
