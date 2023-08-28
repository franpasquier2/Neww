from game.nuevo import suma 
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(suma(1,1),2)