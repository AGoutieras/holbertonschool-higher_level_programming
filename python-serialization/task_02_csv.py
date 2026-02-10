#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):

    data_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f)
        return True

    except Exception:
        return False
