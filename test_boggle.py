#Importing the module unittest and boggle
import unittest
import boggle
from string import ascii_uppercase


"""
#Set a class called boggle_test then call a function with self parameter for testing
#Self represents or points the instance which it was called, self is the first thing that
#is passed to a function in a class, the object itself is passed as an argument
class boggle_test(unittest.TestCase):
#Calling the function for testing if two values are equal
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)
""" 

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
       """
       Test to see if we can create an empty grid
       """
       grid = boggle.make_grid(0, 0)
       self.assertEqual(len(grid), 0)
       
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equal to width * height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates inside
        of the grid can be accessed
        """
        grid = boggle.make_grid(2,2)
        #check if {0,0},  {0,1},  {1,0},  {1,1} are in the grid
        self.assertIn((0,0), grid)
        self.assertIn((0,1), grid)
        self.assertIn((1,0), grid)
        self.assertIn((1,1), grid)
        self.assertNotIn((1,2), grid)
        self.assertNotIn((2,1), grid)
        self.assertNotIn((2,2), grid)
        
    def test_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid contains letters
        """
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
            
    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours
        """
        coords = (2,2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((1,1), neighbours)
        self.assertIn((1,2), neighbours)
        self.assertIn((1,3), neighbours)
        self.assertIn((2,1), neighbours)
        self.assertIn((2,3), neighbours)
        self.assertIn((3,1), neighbours)
        self.assertIn((3,2), neighbours)
        self.assertIn((3,3), neighbours)
        
    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2,2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(grid), len(neighbours))
        for pos in grid:
            others = list(grid) #create a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
        