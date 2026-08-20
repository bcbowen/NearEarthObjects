from models import NearEarthObject, CloseApproach
from datetime import datetime
import math
import unittest

"""
To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_models

"""

class NearEarthObjectTests(unittest.TestCase):

    def test_ctor_defaults(self): 
        n = NearEarthObject("n1", True)
        self.assertEqual(n.designation, 'n1')
        self.assertTrue(n.hazardous)
        self.assertTrue(math.isnan(n.diameter))
        self.assertEqual(n.name, None)

    def test_ctor_full(self): 
            n = NearEarthObject("n1", False, diameter = 2.3, name = "Hendricks")
            self.assertEqual(n.designation, 'n1')
            self.assertFalse(n.hazardous)
            self.assertEqual(2.3, n.diameter)
            self.assertEqual(n.name, "Hendricks")


    def test_fullname(self): 
        cases = [
            ('n1', 'Skylab', 'n1 (Skylab)'), 
            ('n1', None, 'n1')] 

        for designation, name, expected in cases: 
            n = NearEarthObject(designation, True, name=name)
            result = n.fullname
            self.assertEqual(result, expected)


    def test_to_string(self): 
        cases = [
            ('n1', True, 2.1, 'Hendricks', 'NEO n1 (Hendricks) has a diameter of 2.100 km and is potentially hazardous.'),
            ('n1', True, 2.1, None, 'NEO n1 has a diameter of 2.100 km and is potentially hazardous.'), 
            ('n1', True, float('nan'), None, 'NEO n1 is potentially hazardous.'),
            ('n1', False, float('nan'), None, 'NEO n1 is not potentially hazardous.'),

        ]

        for designation, is_hazardous, diameter, name, expected in cases: 
            n = NearEarthObject(designation, is_hazardous, diameter=diameter, name=name)
            result = str(n)
            self.assertEqual(result, expected) 
            

class CloseApproachTests(unittest.TestCase):
     # On 1910-05-20 12:49, '1P (Halley)' approaches Earth at a distance of 0.15 au and a velocity of 70.56 km/s.
     def test_to_string(self): 
            d = 'n1'
            n = "Skylab"
            n = NearEarthObject(d, True, name=n)
            time = '2026-Aug-02 14:34' #datetime(2026, 8, 2)
            distance = 3.4
            velocity = 4.5
            c = CloseApproach(time, distance, velocity, n)

            expected = "At 2026-08-02 14:34, 'n1 (Skylab)' approaches Earth at a distance of 3.40 au and a velocity of 4.50 km/s."
            result = str(c)
            self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main() 
