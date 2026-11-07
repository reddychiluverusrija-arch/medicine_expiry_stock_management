from utils.data_handler import load_medicines,load_sales
def inventory_report():
    medicines=load_medicines()
    print("=" * 50)
    print("             INVENTORY REPORT")
    print("=" * 50)
    total_quantity=0
    in_stock=0
    out_of_stock=0
    for i in medicines:
        quantity=int(i["quantity"])
        total_quantity+=quantity
        if quantity>0:
            in_stock+=1
        elif quantity==0:
            out_of_stock+=1

    print("Total Medicine Records :", len(medicines))
    print("Total Stock Quantity    :", total_quantity)
    print("In Stock Medicines      :", in_stock)
    print("Out of Stock Medicines  :", out_of_stock)
    print("-" * 50)
    print("MEDICINE NAME".ljust(25) + "QUANTITY")
    print("-" * 40)
    for i in medicines:
        print(i["name"].ljust(25) + i["quantity"])
    if not medicines:
        print("No medicine available in inventory")
    print("-" * 40)
    print("          END OF INVENTORY REPORT")
    print("=" * 50)
# inventory_report() 
def sales_report():
    sales=load_sales()
    medicine_sales={}
    for medicine in sales:
        medicine_sold=int(medicine["quantity_sold"])
        # print(medicine["medicine_name"], medicine["quantity_sold"])
        if medicine["medicine_name"] in medicine_sales:
            medicine_sales[medicine["medicine_name"]]+=medicine_sold
        else:
            medicine_sales[medicine["medicine_name"]]=medicine_sold
    print("=" * 50)
    print("                 SALES REPORT")
    print("=" * 50)
    print("MEDICINE NAME".ljust(30) + "QUANTITY SOLD")
    print("-" * 50)
    for k,v in medicine_sales.items():
        print(k.ljust(30)+str(v))

    total_sales=len(sales)
    total_quantity=0 
    for i in sales:
        quantity_sold=int(i["quantity_sold"])
        total_quantity+=quantity_sold
    print("-" * 50)
    print("Total Sales Records      :", total_sales)
    print("Total Quantity Sold      :", total_quantity)
    print("-" * 50)
    print("              END OF SALES REPORT")
    print("=" * 50)
# sales_report()

