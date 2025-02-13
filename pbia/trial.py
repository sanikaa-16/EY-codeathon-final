import sqlite3

# Connect to SQLite Database (Creates it if not exists)
conn = sqlite3.connect("instance.db")
cursor = conn.cursor()

# Create Table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS bia_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    function TEXT,
    bci INTEGER,
    risk_exposure TEXT,
    probability_of_failure REAL,
    downtime_cost REAL,
    wrt REAL,
    mtd REAL,
    rpo REAL,
    rto REAL,
    financial_impact REAL,
    recovery_cost REAL
)
""")

# Dummy Data (Matching Provided Table)
bia_records = [
    ("Customer Support", 85, "Medium", 30, 25000, 1, 8, 1, 2, 50000, 5000),
    ("Payment Processing", 95, "High", 60, 75000, 0.5, 2, 0.5, 1, 150000, 15000),
    ("Order Management", 80, "High", 50, 50000, 2, 6, 2, 4, 100000, 8000),
    ("Inventory Management", 75, "Medium", 40, 35000, 3, 10, 3, 6, 80000, 7500),
    ("HR & Payroll", 70, "Low", 20, 15000, 4, 24, 6, 12, 40000, 4000),
    ("Marketing & Analytics", 65, "Low", 10, 5000, 6, 48, 12, 24, 20000, 2500)
]

# Insert Data into the Table
cursor.executemany("""
INSERT INTO bia_data (function, bci, risk_exposure, probability_of_failure, downtime_cost, wrt, mtd, rpo, rto, financial_impact, recovery_cost) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", bia_records)

# Commit and Close
conn.commit()

# Fetch and Display the Data
cursor.execute("SELECT * FROM bia_data")
rows = cursor.fetchall()
print("\nStored Data in SQLite Database:")
for row in rows:
    print(row)

# Close Connection
conn.close()
