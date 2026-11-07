# project Title

Medicine Expiry & Stock Management System

## Project overview
The Medicine Expiry & Stock Management System is a Python-based application designed to manage medicine inventory efficiently. It helps users maintain medicine records, track stock quantities, monitor expiry dates, and record sales. The system also provides low-stock alerts, expiry alerts, and inventory and sales reports to make medicine management easier.

## Features
- Add new medicines
- View all medicines
- Search medicines by ID
- Update medicine details
- Delete medicine records
- Low stock alerts
- Medicine expiry alerts
- Inventory report
- Record medicine sales
- View sales records
- Sales report

## Technologies Used
- Python 3
- CSV (for storing medicine and sales records)
- JSON (for storing application settings)
- VS Code
- Git & GitHub (if you used them for this project)

## Project Structure
medicine_management/
│
├── app/
│   ├── medicine.py
│   ├── inventory.py
│   ├── expiry.py
│   ├── sales.py
│   └── reports.py
│
├── data/
│   ├── medicines.csv
│   ├── sales.csv
│   └── settings.json
│
├── utils/
│   ├── data_handler.py
│   └── file_handler.py
│
├── main.py
├── README.md
└── test_file_handler.py

## How to Run the Project
### 1. Clone the repository
git clone <your-github-repository-link>

### 2. Navigate to the project folder
cd medicine_management

### 3. Create a virtual environment
python -m venv .venv

### 4. Activate the virtual environment (Windows)
.venv\Scripts\activate

### 5. Run the application
python main.py

## Future Enhancements
- Integrate a database such as MySQL or SQLite.
- Add a user login and authentication system.
- Develop a web-based interface using FastAPI or Flask.
- Generate downloadable inventory and sales reports.
- Add barcode scanning for medicine identification.