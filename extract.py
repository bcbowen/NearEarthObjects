"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

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
    """
    cas = []
    designation_index = 0
    date_index = 3
    distance_index = 4
    velocity_index = 7


    with open(cad_json_path, 'r') as file:
        contents = json.load(file)
        for row in contents["data"]:
            try: 
                n = NearEarthObject(row[designation_index], True) 
                ca = CloseApproach(row[date_index], float(row[distance_index]), float(row[velocity_index]), n)
                cas.append(ca)
            except: 
                print(row)
    return cas
