from utils.file_handler import read_csv,write_csv,read_json,write_json
from utils.data_handler import save_medicines
from utils.data_handler import save_settings
from utils.data_handler import load_settings
fieldnames=["medicine_id","name","quantity"]#coloums
medicines=[            # medicine records
    {"medicine_id":101,
    "name":"paracetamol",
    "quantity":500},
    {"medicine_id":102,
     "name":"dolo",
     "quantity":250}
]
write_csv("test_medicines.csv",fieldnames,medicines)

result=read_csv("test_medicines.csv")
print(result)
settings={
    'low_stock_limit':10,
    'expiry_alert_days':30
}
updated_settings={
    "low_stock_limit":15,
    "expiry_alert_days":45
}
save_settings(updated_settings)
load=load_settings()
print(load)

write_json("test_settings.json",settings)
result_json=read_json("test_settings.json")
print(result_json)
from utils.data_handler import load_medicines
save=save_medicines(medicines)
medicines=load_medicines()
print("load medicines:",medicines)
