import csv
import codecs


def load_csv_data(url, delimiter=',') -> list:
    reader = csv.DictReader(codecs.open(url))

    return list(reader)


def parse_csv(url):
    data = load_csv_data(url)

    ax = []
    ay = []
    az = []

    for row in data[1:]:
        ax.append(row['ax'])
        ay.append(row['ay'])
        az.append(row['az'])

    return {'ax': ax, 'ay': ay, 'az': az}


def load_json(url):
    import json

    json_data = json.load(open(url))

    result = {}

    for key in json_data.keys():
        result[key] = json_data[key]['name']

    return result
