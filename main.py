# from utils.file_handler import read_csv,write_csv,read_json,write_json 
from app.medicine import add_medicine,view_medicines,search_medicine,update_medicine,delete_medicine
from app.inventory import low_stock_alert
from app.expiry import expiry_alert
from app.reports import inventory_report,sales_report
from app.sales import record_sales,view_sales
from utils.alerts import show_automatic_alerts
def main_menu():
    print("===========================================")
    print("MEDICINE EXPIRY & STOCK MANAGEMENT SYSTEM")
    print("===========================================")
    show_automatic_alerts()
    while True:
        print("-----------------MAIN MENU--------------")
        print(" 1. Add Medicine")
        print(" 2. View Medicine")
        print(" 3. Search Medicine")
        print(" 4. Update Medicine")
        print(" 5. Delete Medicine")
        print(" 6. Low Stock Alert")
        print(" 7. Expiry Alert")
        print(" 8. Inventory Report")
        print(" 9. Record Sales")
        print("10. View Sales")
        print("11. Sales Report")
        print("12. EXIT")
        print("-----------------------------------------------")
        
        choice=input("Enter your choice:")
   
        if choice=="1":
            add_medicine()
            show_automatic_alerts()
        elif choice=="2":
            view_medicines()
        elif choice=="3":
            search_medicine()
        elif choice=="4":
            update_medicine()
            show_automatic_alerts()
        elif choice=="5":
            delete_medicine()
        elif choice=="6":
            low_stock_alert()
        elif choice=="7":
            expiry_alert()
        elif choice=="8":
            inventory_report()
        elif choice=="9":
            record_sales()
            show_automatic_alerts()
        elif choice=="10":
            view_sales()
        elif choice=="11":
            sales_report()
        elif choice=="12":
            print("Thank you")
            break
        else:
            print("Invalid choice. Please enter a number between 1 to 12")
main_menu()