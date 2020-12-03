import sqlite3

conn = sqlite3.connect('hospital.db') 

c = conn.cursor()

c.execute("""
    DROP TABLE hospitals ;
    """)

c.execute("""
    DROP TABLE employees ;
    """)

c.execute("""
    DROP TABLE doctors ;
    """)

c.execute("""
    DROP TABLE nurses ;
    """)

c.execute("""
    DROP TABLE patients ;
    """)

c.execute("""
    DROP TABLE appointments ;
    """)

c.execute("""
    DROP TABLE invoices ;
    """)

c.execute("""
    DROP TABLE medicines
    """)

c.execute("""
    DROP TABLE diagnoses
    """)

c.execute("""
    DROP TABLE prescriptions
    """)

c.execute("""
    DROP TABLE medical_history
    """)

conn.commit()

conn.close()
