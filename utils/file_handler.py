import csv
import json
def read_csv(file_path):
    with open(file_path, "r",newline="") as file:
        reader=csv.DictReader(file)
        return list(reader)
def write_csv(file_path,fieldnames,data):
    with open(file_path,"w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
def read_json(file_path):
    with open(file_path,"r") as file:
        return json.load(file)
def write_json(file_path,data):
    with open(file_path,"w") as file:
        json.dump(data,file,indent=4)
