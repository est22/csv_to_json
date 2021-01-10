import csv
import json

csv_file = "counterparty_dict.csv"
json_path = './counterparty_dict.json'

data = []

with open(csv_file,"r", encoding="utf-8") as data_csv:
    csv_reader = csv.DictReader(data_csv)
    for csvrows in csv_reader:
        data.append(csvrows)
with open(json_path, 'w', encoding="utf-8") as data_json:
    data_json.write(json.dumps(data,ensure_ascii=False, indent=4))
