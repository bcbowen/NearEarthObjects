from models import NearEarthObject, CloseApproach
import math
#import pathlib
import unittest

"""
To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_models

"""

class NearEarthObjectTests(unittest.TestCase):
    # The root of the project, containing `main.py`.
    #PROJECT_ROOT = pathlib.Path(__file__).parent.parent.resolve() 

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

    """
    result = [f"NEO {self.fullname} "]
            if self.diameter != float('nan'): 
                result.append(f"has a diameter of {self.diameter:.3f} km and ")
    
            if self.hazardous: 
                result.append("is potentially hazardous.")
            else: 
                result.append("is not potentially hazardous.")
    """
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
            

if __name__ == "__main__":
    unittest.main() 
