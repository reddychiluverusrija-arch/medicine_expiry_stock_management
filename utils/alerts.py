from tkinter import messagebox
from app.inventory import low_stock_alert
from app.expiry import expiry_alert
from utils.data_handler import load_medicines,load_settings
from datetime import datetime
def show_automatic_alerts():
    load=load_medicines()
    settings=load_settings()
    alerts=[]
    date=datetime.today().date()
    for medicine in load:
        quantity=int(medicine["quantity"])
        if quantity <=settings["low_stock_limit"]:
            alerts.append(f"{medicine['name']}-{quantity} is left!")
        expiry_date=datetime.strptime(medicine["expiry_date"],"%d-%m-%Y").date()
        subtract=expiry_date-date
        days_left=subtract.days
        if days_left<0:
            alerts.append(f"{medicine['name']}- Expired {-days_left } days ago")
        elif days_left==0:
             alerts.append(f"{medicine['name']}- Expires today")
        elif days_left<=settings["expiry_alert_days"]:
            alerts.append(f"{medicine['name']}-expiring in {days_left} days")
    if not alerts:
        return
    else:
        pop=messagebox.showwarning("Medicine Alert","\n".join(alerts))

