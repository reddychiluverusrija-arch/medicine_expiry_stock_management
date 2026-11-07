from utils.data_handler import load_medicines,save_medicines
def add_medicine():
    existing_medicine=load_medicines()
    duplicate=False
    

    medicine_id=input("Enter Medicine Id:")
    for i in existing_medicine:
        if medicine_id==i["medicine_id"]:
            duplicate=True
            print("--------------------------------------------")
            print("MEDICINE ALREADY EXIST!")
            print("--------------------------------------------")
            print("Medicine with the ID already registered.")
            print("please enter a different ID")
            print()
            return
    if not duplicate:
       

        name=input("Enter Medicine Name:")
        quantity=input("Enter quantity:")
        expiry_date=input("expiry_date:")

        medicine_records={
            "medicine_id":medicine_id,
            "name":name,
            "quantity":quantity,
            "expiry_date":expiry_date
        }
        existing_medicine.append(medicine_records)
        # print("existing:",existing_medicine)
        save_medicines(existing_medicine)
        print("-------------------------------------")
        print("MEDICINE ADDED SUCCESSFULLY!")
        print("-------------------------------------")
        print(f"Medicine ID : {medicine_id}")
        print(f"Medicine    : {name}")
        print(f"Quantity    : {quantity} units")
        print(f"Expiry Date : {expiry_date}")
        print("-------------------------------------")
# add_medicine()
def  view_medicines():
    load=load_medicines()
    if not load:
        print("No medicine found")
        return
    print("========================= MEDICINE INVENTORY ===============================")
    print("ID".ljust(10)+"MEDICINE NAME".ljust(20) + "QUANTITY".ljust(15) +"EXPIRY DATE")
    print("----------------------------------------------------------------------------")
   
    for i in load:
        # print("========================= MEDICINE INVENTORY ===============================")
        # print("ID".ljust(10)+"MEDICINE NAME".ljust(20) + "QUANTITY".ljust(15) +"EXPIRY DATE")
        # print("------------------------------------------------------------------------------------------")
        print(i["medicine_id"].ljust(10)+i["name"].ljust(20)+i["quantity"].ljust(15)+i["expiry_date"])
    print("Total Medicines:",len(load))

        # print("medicine:",i)
# view_medicines()
def search_medicine():
    load_all=load_medicines()
    medicine_id=input("Enter Id to search:")
    for i in load_all:
        if i["medicine_id"]==medicine_id:
            print("=========== MEDICINE FOUND===========")
            print("ID".ljust(10)+"NAME".ljust(20)+"QUANTITY".ljust(20)+"EXPIRY DATE")
            print(i["medicine_id"].ljust(10)+i["name"].ljust(20)+i["quantity"].ljust(15)+ i["expiry_date"])
            print("-"*75)
            # print("medicine found:",i)
            return
        
    print("medicine not found")
# search_medicine()
def update_medicine():
    update=load_medicines()
    medicine_id=input("Enter medicine to update:")
    found=False
    for i in update:
        if i["medicine_id"]==medicine_id:
            found=True
            new_name=input("Enter new medicine name:")
            new_quantity=input("Enter quantity of new medicine:")
            i["name"]=new_name
            i["quantity"]=new_quantity
            save_medicines(update)
            print("-------------------------------------------")
            print("       MEDICINE UPDATED SUCCESSFULLY!")
            print("-------------------------------------------")
            print(f"Medicine ID   : {i['medicine_id']}")
            print(f"Medicine Name : {i['name']}")
            print(f"Quantity      : {i['quantity']}")
            print("-------------------------------------------")
            break

    if not found:
        print("Id not found")
    
# update_medicine()
def delete_medicine():
    delete=load_medicines()
    medicine_id=input("Enter Id to delete:")
    found=False
    for i in delete:
        if i["medicine_id"]==medicine_id:
            found=True
            delete.remove(i)
            print("-------------------------------------------")
            print("       MEDICINE DELETED SUCCESSFULLY!")
            print("-------------------------------------------")
            print(f"Deleted Medicine ID : {medicine_id}")
            print("-------------------------------------------")
            break
    if not found:
        print("Medicine not found")
    save_medicines(delete)
# delete_medicine()

