"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import pathlib
from typing import List
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path: pathlib.Path) -> List[NearEarthObject]:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.

    """
    neos = [] 

    with open(neo_csv_path, 'r') as csv_file: 
        reader = csv.DictReader(csv_file)
        for row in reader: 
            designation = row['pdes']
            hazardous = True if row['pha'] == 'Y' else False
            if row['name']: 
                name = row['name']
            else: 
                name = None
            if row['diameter']: 
                diameter = float(row['diameter'])
            else: 
                diameter = float('nan')
            neos.append(NearEarthObject(designation, hazardous, name, diameter))

    return neos


def load_approaches(cad_json_path: pathlib.Path) -> List[CloseApproach]:
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.

    with open('listings.json', 'r') as infile:
        contents = json.load(infile)  # Parse JSON data into a Python object. (A)

    # Filter out all unavailable job listings.
    available = [job for job in contents if job["available"]]

    {
  "count": 4700,
  "data": [
    [
      "2020 AY1",
      "18",
      "2458849.537524496",
      "2020-Jan-01 00:54",
      "0.0211660525256395",
      "0.0211628345552616",
      "0.0211692704882042",
      "5.62203195551878",
      "5.59959589405614",
      "< 00:01",
      "25.1"
    ],
    [
      "2019 YK",
      "10",
      "2458849.587205145",
      "2020-Jan-01 02:06",
      "0.0361009669651545",
      "0.0360768281418277",
      "0.036125105699654",
      "7.35926323695148",
      "7.34922735808709",
      "< 00:01",
      "24.0"
    ],

    
     "fields": [
    "des",
    "orbit_id",
    "jd",
    "cd",
    "dist",
    "dist_min",
    "dist_max",
    "v_rel",
    "v_inf",
    "t_sigma_f",
    "h"
  ],
    """
    cas = []

    with open(cad_json_path, 'r') as file:
        contents = json.load(file)
        for  
    # TODO: Load close approach data from the given JSON file.
    return cas
