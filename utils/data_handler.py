from utils.file_handler import read_csv,write_csv,read_json,write_json
def load_medicines():
    medicines=read_csv("data/medicines.csv")
    return medicines
def  load_settings():
    records=read_json("data/settings.json")
    return records
def save_medicines(medicines):
    fieldnames=["medicine_id","name","quantity","expiry_date"]
    write_csv("data/medicines.csv",fieldnames,medicines)
def save_settings(settings):
    write_json("data/settings.json",settings)
def load_sales():
    sales=read_csv("data/sales.csv")
    return sales
def save_sales(sales):  
    fieldnames=["sale_id","medicine_id","medicine_name","quantity_sold","sale_date"]
    write_csv("data/sales.csv",fieldnames,sales)  


    