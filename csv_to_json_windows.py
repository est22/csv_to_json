import csv
import json

csv_file = "고객사_거래상대방_Dict_test_real2.csv"
json_path = './고객사_거래상대방_Dict_test_real2.json'

data = []

with open(csv_file,"r", encoding="cp949") as data_csv:
    csv_reader = csv.DictReader(data_csv)
    for csvrows in csv_reader:
        data.append(csvrows)
with open(json_path, 'w', encoding="cp949") as data_json:
    data_json.write(json.dumps(data, ensure_ascii=False, indent=4))