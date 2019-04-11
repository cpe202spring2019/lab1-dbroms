import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_repr2(self):
        loc = Location("LJ", -41.4, 37.9)
        self.assertEqual(repr(loc),"Location('LJ', -41.4, 37.9)")
    def test_repr3(self):
        loc = Location("LA", 35.8, 84.4)
        self.assertEqual(repr(loc),"Location('LA', 35.8, 84.4)")
    def test_repr4(self):
        loc = Location("Bend", -31.7, -91.5)
        self.assertEqual(repr(loc),"Location('Bend', -31.7, -91.5)")

if __name__ == "__main__":
        unittest.main()
