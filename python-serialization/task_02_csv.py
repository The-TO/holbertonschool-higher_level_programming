#!/usr/bin/env python3
"""Module  for convert CSV file into json"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        with open("data.json", "w") as f:
            json.dump(data, f)
            return True
    except FileNotFoundError:
        return False
