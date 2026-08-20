import csv
import helpers
import json
import math
import pathlib
from typing import Iterable
from models import CloseApproach

def write_to_csv(results: Iterable[CloseApproach], filename: pathlib.Path):
    """
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')

    with open(filename, 'w') as file: 
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        row = {}
        for result in results: 
            
            row['datetime_utc'] = helpers.datetime_to_str(result.time)
            row['distance_au'] = result.distance
            row['velocity_km_s'] = result.velocity
            row['designation'] = result.neo.designation
            row['name'] = result.neo.name if result.neo.name else ''
            row['diameter_km'] = result.neo.diameter if not math.isnan(result.neo.diameter) else 'nan'
            row['potentially_hazardous'] = result.neo.hazardous
            writer.writerow(row)



def write_to_json(results: Iterable[CloseApproach], filename: pathlib.Path):
    """
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    
    with open(filename, 'w') as file: 
        approaches = []
        for result in results: 
            approach = {} 
            neo = {}
            approach['datetime_utc'] = helpers.datetime_to_str(result.time)
            approach['distance_au'] = result.distance
            approach['velocity_km_s'] = result.velocity

            neo['designation'] = result.neo.designation
            neo['name'] = result.neo.name if result.neo.name else ''
            neo['diameter_km'] = result.neo.diameter if not math.isnan(result.neo.diameter) else float('nan')
            neo['potentially_hazardous'] = result.neo.hazardous
            approach["neo"] = neo
            approaches.append(approach)

        json.dump(approaches, file, indent = 2)