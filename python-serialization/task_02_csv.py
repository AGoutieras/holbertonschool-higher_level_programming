#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):

    data_list = []

    with open(filename, "r") as f:
        for row in csv.DictReader(f):
            data_list.append(row)

    try:
        with open("data.json", "w") as f:
            json.dump(data_list, f)
        return True

    except Exception:
        return False
