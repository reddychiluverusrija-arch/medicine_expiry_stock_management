from utils.data_handler import load_medicines,save_medicines,save_sales,load_sales
from datetime import datetime
def record_sales():
    medicines=load_medicines()
    # print(medicines)
    medicine_id=input("Enter medicine Id:")
    sales=load_sales()
    found=False
    for i in medicines:
        if medicine_id==i["medicine_id"]:
            found=True
            quantity=int(input("enter Quantity:"))
            sale_id=input("Enter Sale ID:")
            sale_found=False
            for sale in sales:
                if sale_id==sale["sale_id"]:
                    sale_found=True
                    print("Sale ID already Exist")
                    break
            if sale_found:
                return
        
            In_Quantity=int(i["quantity"])
            if quantity>0:
                if In_Quantity>=quantity:
                    sub=In_Quantity-quantity
                    i["quantity"]=sub
                    sale_record={
                        "sale_id":sale_id,
                        "medicine_id":medicine_id,
                        "medicine_name":i["name"] ,
                        "quantity_sold":quantity,
                        "sale_date":datetime.today().strftime("%d-%m-%Y")
                        }
                    sales.append(sale_record)
                    save_medicines(medicines)
                    # print("Successful sale")
                    save_sales(sales)
                    print("-------------------------------------------")
                    print("          SALE RECORDED SUCCESSFULLY!")
                    print("-------------------------------------------")
                    print(f"Sale ID       : {sale_id}")
                    print(f"Medicine ID   : {medicine_id}")
                    print(f"Medicine Name : {i['name']}")
                    print(f"Quantity Sold : {quantity}")
                    print(f"Sale Date     : {sale_record['sale_date']}")
                    print("-------------------------------------------")
                    break
                    
                else:
                    print("Insufficient Stock ")
            else:
                print("Quantity must be greater than zero")
    if found==False:
        print("Medicine Not found")
        
# record_sales()
def view_sales():
    sales=load_sales()
    if not sales:
        print("No sales found")
        return
    print("=" * 90)
    print("                         SALES RECORDS")
    print("=" * 90)
    print("SALE ID".ljust(12) + "MEDICINE ID".ljust(15) + "MEDICINE NAME".ljust(20) + "QUANTITY".ljust(15) + "SALE DATE")
    print("-" * 90) 
    for i in sales:
        print(
            i["sale_id"].ljust(12) +
            i["medicine_id"].ljust(15) +
            i["medicine_name"].ljust(20) +
            i["quantity_sold"].ljust(15) +
            i["sale_date"]
        )
    print("-" * 90)
    print("Total Sales Records:", len(sales))
    print("=" * 90)
# # view_sales()
