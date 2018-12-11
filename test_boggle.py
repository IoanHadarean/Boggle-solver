#Importing the module unittest
import unittest

#Set a class called boggle_test then call a function with self parameter for testing
#Self represents or points the instance which it was called, self is the first thing that
#is passed to a function in a class, the object itself is passed as an argument
class boggle_test(unittest.TestCase):
#Calling the function for testing if two values are equal
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
        