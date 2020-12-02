import sqlite3

conn = sqlite3.connect('hospital.db') 

c = conn.cursor()

#create tables 
#create table 
c.execute("""
    CREATE TABLE hospitals ( 
        hospital_id int, 
        hospital_name text, 
        address text,
        city text,
        province text,
        postal_code text
    )
    """)



c.execute("""
	CREATE TABLE employees ( 
	employee_id int, 
	f_name text,
	l_name text,
	dob text,
	gender text,
	age int, 
	address text,
	city text,
	province text, 
	postal_code text,
	phone int, 
	email text,
	hospital_id
	)
	""")

c.execute("""
	CREATE TABLE doctors(
	doctor_id int,
	doctor_license_expiry text,
	employee_id int
	)
	""")


c.execute("""
	CREATE TABLE nurses(
	nurse_id int, 
	nurse_license_expiry text,
	employee_id int
	)
	""")

c.execute("""
	CREATE TABLE patients(
	healthcard_number int, 
	f_name text,
	l_name text,
	dob text,
	gender text,
	age int, 
	address text,
	city text,
	province text,
	postal_code text,
	phone int, 
	email text
	)	
	""")


c.execute("""
	CREATE TABLE appointments(
	appointment_id int, 
	appointment_date text,
	appointment_time int, 
	room_number int,
	hospital_id int,
	healthcard_number int,
	doctor_id int
	)
	""")

c.execute("""
	CREATE TABLE invoices(
	invoice_number int, 
	medicine_id text, 
	date_issued text,
	amount_owed real,
	appointment_id int
	)
	""")

c.execute("""
	CREATE TABLE medicines(
	medicine_id int,
	dosage real, 
	iupac_name text,
	generic_name text,
	inventory int,
	price real,
	expiration_date text,
	manufacturer text,
	hospital_id int
	)
	""")

c.execute("""
	CREATE TABLE diagnosises(
	diagnosis_id int, 
	results text,
	appointment_id int
	)	
	""")

c.execute("""
	CREATE TABLE prescriptions(
	prescription_id int, 
	date_issued text,
	appointment_id int,
	medicine_id int, 
	diagnosis_id int
	)
	""")

c.execute("""
	CREATE TABLE medical_history(
	healthcard_number int, 
	appointment_id int, 
	diagnosis_id int, 
	medical_desc text
	)
	""")

conn.commit()

conn.close()