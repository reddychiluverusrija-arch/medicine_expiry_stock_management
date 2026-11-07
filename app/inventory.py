from utils.data_handler import load_medicines ,load_settings
def low_stock_alert():
    medicine=load_medicines()
    setting=load_settings()
    limit=setting["low_stock_limit"]
    print("================ LOW STOCK ALERT ================")
    print("MEDICINE NAME".ljust(25) + "QUANTITY")
    print("-" * 40)
    found=False
    for i in medicine:
        quantity=int(i["quantity"])
        if quantity<=limit:
            found = True
            print(i["name"].ljust(25) + str(quantity))
    if not found:
        print("No medicines are currently in low stock")
            
# low_stock_alert()