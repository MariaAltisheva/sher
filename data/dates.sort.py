import csv
import json


def convert_categories_csv_to_json():
    with open('dates.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        rows = list(csv_reader)

    with open('dates.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)


convert_categories_csv_to_json()
