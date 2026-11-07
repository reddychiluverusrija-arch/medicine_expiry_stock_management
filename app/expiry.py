from utils.data_handler import load_medicines,load_settings
from datetime import datetime
def expiry_alert():
    load=load_medicines()
    settings=load_settings()
    alert_days=settings["expiry_alert_days"]
    found=False
    print("================ MEDICINE EXPIRY ALERT ================")
    print("MEDICINE NAME".ljust(25) + "EXPIRY STATUS")
    print("-" * 50)
    for i in load:
        expiry_date=i["expiry_date"]
        expiry_date=datetime.strptime(expiry_date,"%d-%m-%Y").date()
        today=datetime.today().date()
        sub=expiry_date-today
        differences=sub.days
        # print("Today:", today)
        # print("Expiry date:", expiry_date)  
        # print("Days:",differences)
        if differences <0:
            found=True
            print(i["name"].ljust(25) + f"Expired {-differences} days ago")
        elif differences==0:     
            found=True
            print(i["name"].ljust(25) + "Expires Today")
        elif differences<=alert_days:
            found=True
            print(i["name"].ljust(25) + f"Expiring in {differences} days")
    if not found:
        print("No medicines are expiring soon.")
# expiry_alert()
