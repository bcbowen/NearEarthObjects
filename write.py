"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import helpers
import json
import math
import pathlib
from typing import Iterable
from models import CloseApproach

def write_to_csv(results: Iterable[CloseApproach], filename: pathlib.Path):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    #if not filename: 
    #    return
    #if not filename.parent.exists(): 
    #    raise FileNotFoundError(f"Invalid path: {filename}")

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
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    {
    "datetime_utc": "2025-11-30 02:18",
    "distance_au": 0.397647483265833,
    "velocity_km_s": 3.72885069167641,
    "neo": {
      "designation": "433",
      "name": "Eros",
      "diameter_km": 16.84,
      "potentially_hazardous": false
    }
  },

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    

    """
    with open('available-listings.json', 'w') as outfile:
    json.dump(available, outfile, indent=2)
    """

    #if not filename: 
    #    return
    #if not filename.parent.exists(): 
    #    raise FileNotFoundError(f"Invalid path: {filename}")

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