import sqlite3

con = sqlite3.connect("SupportCenter.db")
cursor = con.cursor()

cursor.execute("""
        CREATE TABLE Tickets (
                    ID INTEGER PRIMARY KEY, 
                    Title TEXT NOT NULL, 
                    Type TEXT NOT NULL, 
                    Priority TEXT NOT NULL,  
                    Description TEXT, 
                    State TEXT NOT NULL,
                    Agent TEXT NOT NULL,
                    CreatedDate DATE DEFAULT CURRENT_DATE 
            );
    """)

tickets = [
    ("Mac cannot start", "Hardware", "P1", "The Mac cannot start.", "New", "Mike"),
    (
        "PC cannot connect to WIFI",
        "Hardware",
        "P2",
        "The PC cannot connect to WIFI.",
        "Assigned",
        "Jack",
    ),
    (
        "Office subcription expires",
        "Hardware",
        "P1",
        "My office subscription exprires, I cannot use Word any more.",
        "Resolved",
        "Annie",
    ),
]

for ticket in tickets:
    cursor.execute(
        """
        INSERT INTO Tickets (Title, Type, Priority, Description, State, Agent)
        VALUES (?,?,?,?,?,?);
""",
        ticket,
    )

con.commit()

con.close()
