from filters import DesignationFilter, NameFilter
from models import NearEarthObject, CloseApproach
from datetime import datetime
import math
import operator
import unittest

class FilterTests(unittest.TestCase):

    def test_designation_filter_match(self): 
        designation = 'n1'
        n = NearEarthObject(designation, True)
        a = CloseApproach("2026-Aug-02 14:34", 1.2, 1.2, n)
        
        f = DesignationFilter(operator.eq, designation)
        expected = True
        result = f(a) 
        self.assertEqual(expected, result)

    def test_designation_filter_mismatch(self): 
        designation = 'n1'
        n = NearEarthObject(designation, True)
        a = CloseApproach("2026-Aug-02 14:34", 1.2, 1.2, n)
        
        f = DesignationFilter(operator.eq, 'nope')
        expected = False
        result = f(a)  
        self.assertEqual(expected, result)

    def test_name_filter_match(self): 
        designation = 'n1'
        name = 'HugeRock'
        n = NearEarthObject(designation, True, name=name)
        a = CloseApproach("2026-Aug-02 14:34", 1.2, 1.2, n)
        
        f = NameFilter(operator.eq, name)
        expected = True
        result = f(a) 
        self.assertEqual(expected, result)
    
    def test_name_filter_mismatch(self): 
        designation = 'n1'
        name = 'HugeRock'
        bad_names = ['TinyRock', '', None]
        
        f = NameFilter(operator.eq, name)

        expected = False
        for bad_name in bad_names: 
            n = NearEarthObject(designation, True, name=bad_name)
            a = CloseApproach("2026-Aug-02 14:34", 1.2, 1.2, n)
            result = f(a)  
            self.assertEqual(expected, result)