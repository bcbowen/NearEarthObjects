from filters import DesignationFilter, NameFilter, DiameterFilter, HazardousFilter, TimeFilter, DistanceFilter, VelocityFilter
from models import NearEarthObject, CloseApproach
from datetime import datetime, timedelta
import helpers
import operator
import unittest


class FilterTests(unittest.TestCase):

    def init_neo(self) -> NearEarthObject: 
        designation = 'n1'
        name = 'HugeRock'
        diameter = 2.3
        hazardous = True
        return NearEarthObject(designation, hazardous, name=name, diameter=diameter)

    def init_close_approach(self) -> CloseApproach: 
        time = datetime(2020, 9, 8, 14, 20)
        utc_date = helpers.datetime_to_cd(time)
        distance = 1.2
        velocity = 4.5
        n = self.init_neo()
        return CloseApproach(utc_date, distance, velocity, n)

    def test_designation_filter_match(self): 
        a = self.init_close_approach()
        
        f = DesignationFilter(operator.eq, a.neo.designation)
        expected = True
        result = f(a) 
        self.assertEqual(expected, result)

    def test_designation_filter_mismatch(self): 
        a = self.init_close_approach()
        
        f = DesignationFilter(operator.eq, 'nope')
        expected = False
        result = f(a)  
        self.assertEqual(expected, result)

    def test_name_filter_match(self): 
        a = self.init_close_approach()
        a.neo.name = 'HugeRock'
        
        f = NameFilter(operator.eq, a.neo.name)
        expected = True
        result = f(a) 
        self.assertEqual(expected, result)
    
    def test_name_filter_mismatch(self): 
        a = self.init_close_approach()
        a.neo.name = 'HugeRock'
        bad_names = ['TinyRock', '', None]
        
        expected = False
        for bad_name in bad_names: 
            f = NameFilter(operator.eq, bad_name) 
            result = f(a)  
            self.assertEqual(expected, result)

    def test_diameter_filter_match(self): 
        a = self.init_close_approach()
        a.neo.diameter = 2.0
        # cases: op, criteria diameter: all expected to match
        expected = True
        cases = [
            (operator.eq, 2.0), 
            (operator.ge, 2.0), 
            (operator.le, 2.0),
            (operator.lt, 2.1), 
            (operator.ge, 1.9), 
            (operator.gt, 1.9),
        ]
        for op, criteria in cases: 
            f = DiameterFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)
        
    def test_diameter_filter_mismatch(self): 
        a = self.init_close_approach()
        # cases: op, criteria diameter: all expected to match
        expected = False
        cases = [
            (operator.eq, 3.0), 
            (operator.ge, 3.0), 
            (operator.le, 1.0),
            (operator.lt, 1.9), 
            (operator.ge, 3.0), 
            (operator.gt, 3.0),
        ]
        for op, criteria in cases: 
            f = DiameterFilter(op, criteria)
            result = f(a) 
            self.assertEqual(expected, result)

    def test_hazardous_filter_match(self): 

        a = self.init_close_approach()
        values = [True, False]
        for value in values:
            a.neo.hazardous = value
            f = HazardousFilter(operator.eq, value)

            # When the value matches the criteria, we expect a match
            expected = True
            result = f(a) 
            self.assertEqual(expected, result)

    def test_hazardous_filter_mismatch(self): 
        
        a = self.init_close_approach()
        values = [True, False]
        for value in values:
            a.neo.hazardous = value
            f = HazardousFilter(operator.eq, not value)

            # When the value does not match the criteria, we expect a mismatch
            expected = False
            result = f(a) 
            self.assertEqual(expected, result)


    def test_time_filter_match(self): 
        a = self.init_close_approach()
                
        # cases: op, criteria time: all expected to match
        expected = True
        cases = [
            (operator.eq, a.time.date()),
            (operator.ge, a.time.date()), 
            (operator.ge, (a.time + timedelta(days = -1)).date()),
            (operator.le, a.time.date()),  
            (operator.le, (a.time + timedelta(days = 1)).date()),
            (operator.lt, (a.time + timedelta(days = 1)).date()), 
            (operator.gt, (a.time + timedelta(days = -1)).date()),
        ]
        for op, criteria in cases: 
            f = TimeFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)

    def test_time_filter_mismatch(self): 
        a = self.init_close_approach()
                        
        # cases: op, criteria time: all expected not to match
        expected = False
        cases = [
            (operator.ge, (a.time + timedelta(days = +1)).date()), 
            (operator.le, (a.time + timedelta(days = -1)).date()),
            (operator.lt, (a.time + timedelta(days = -1)).date()), 
            (operator.gt, (a.time + timedelta(days = +1)).date()),
        ]
        for op, criteria in cases: 
            f = TimeFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)
    
    def test_distance_filter_match(self): 
        a = self.init_close_approach()
                
        # cases: op, criteria time: all expected to match
        expected = True
        cases = [
            (operator.eq, a.distance),
            (operator.ge, a.distance), 
            (operator.ge, a.distance - .5),
            (operator.le, a.distance),  
            (operator.le, a.distance + .5),
            (operator.lt, a.distance + .5), 
            (operator.gt, a.distance - .5),
        ]
        for op, criteria in cases: 
            f = DistanceFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)

    def test_distance_filter_mismatch(self): 
        a = self.init_close_approach()
                        
        # cases: op, criteria time: all expected to match
        expected = False
        cases = [
            (operator.eq, a.distance + 2),
            (operator.ge, a.distance + .5),  
            (operator.le, a.distance - .5),
            (operator.lt, a.distance - .5), 
            (operator.gt, a.distance + .5),
        ]
        for op, criteria in cases: 
            f = DistanceFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)              

    def test_velocity_filter_match(self): 
        a = self.init_close_approach()
                
        # cases: op, criteria time: all expected to match
        expected = True
        cases = [
            (operator.eq, a.velocity),
            (operator.ge, a.velocity), 
            (operator.ge, a.velocity - .5),
            (operator.le, a.velocity),  
            (operator.le, a.velocity + .5),
            (operator.lt, a.velocity + .5), 
            (operator.gt, a.velocity - .5),
        ]
        for op, criteria in cases: 
            f = VelocityFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)

    def test_velocity_filter_mismatch(self): 
        a = self.init_close_approach()
                        
        # cases: op, criteria time: all expected to match
        expected = False
        cases = [
            (operator.eq, a.velocity + 2),
            (operator.ge, a.velocity + .5),  
            (operator.le, a.velocity - .5),
            (operator.lt, a.velocity - .5), 
            (operator.gt, a.velocity + .5),
        ]
        for op, criteria in cases: 
            f = VelocityFilter(op, criteria)

            result = f(a) 
            self.assertEqual(expected, result)              
