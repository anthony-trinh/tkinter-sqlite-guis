from tkinter import * 
from PIL import ImageTk,Image
import os


# initialize root
root = Tk()




###---------------------------------- FUNCTIONS ----------------------------------###
def hospital():
    os.system('~/modules/hospitals.py')

def employees():
    os.system('~/modules/employees.py')

def doctors():
    os.system('~/modules/doctors.py')

def nurses():
    os.system('~/modules/nurses.py')

def patients():
    os.system('~/modules/patients.py')

def appointments():
    os.system('~/modules/appointments.py')

def invoices():
    os.system('~/modules/invoices.py')

def medicines():
    os.system('~/modules/medicines.py') 

def diagnoses (): 
    os.system('~/modules/diagnoses.py')

def prescriptions():
    os.system('~/modules/prescriptions.py')

def medical_history():
    os.system('~/modules/medical_history.py')

def create_tables():
    os.system('~/modules/create_tables.py')

def drop_tables():
    os.system('~/modules/drop_tables.py')




###---------------------------------- GUI ----------------------------------###

title = Label(root, text="Select a table")
title.grid(row=0,column=0,columnspan=4,pady=(20,0))

hospital_button = Button(root, text="Hospitals", command=hospital)
hospital_button.grid(row=1,column=0,padx=100,pady=(20,0))

employees_button = Button(root, text="Employees", command=employees)
employees_button.grid(row=2,column=0,padx=100,pady=(20,0))

doctors_button = Button(root,text="Doctors",command=doctors)
doctors_button.grid(row=3,column=0,padx=100,pady=(20,0))

nurses_button = Button(root,text="Nurses",command=nurses)
nurses_button.grid(row=4,column=0,padx=100,pady=(20,0))

patients_button = Button(root,text="Patients",command=patients)
patients_button.grid(row=5,column=0,padx=100,pady=(20,0))

appointments_button = Button(root,text="Appointments",command=appointments)
appointments_button.grid(row=6,column=0,padx=100,pady=(20,0))

invoices_button = Button(root,text="Invoices",command=invoices)
invoices_button.grid(row=7,column=0,padx=100,pady=(20,0))

medicines_button = Button(root,text="Medicines",command=medicines)
medicines_button.grid(row=8,column=0,padx=100,pady=(20,0))

diagnoses_button = Button(root,text="Diagnoses",command=diagnoses)
diagnoses_button.grid(row=9,column=0,padx=100,pady=(20,0))

prescriptions_button = Button(root,text="Prescriptions",command=prescriptions)
prescriptions_button.grid(row=10,column=0,padx=100,pady=(20,0))

medical_history_button = Button(root,text="Medical History",command=medical_history)
medical_history_button.grid(row=11,column=0,padx=100,pady=(20,0))

options = Label(root, text="Table Options")
options.grid(row=12,column=0,columnspan=4,pady=(20,0))

make_tables_button = Button(root, text="Create Tables",command=create_tables)
make_tables_button.grid(row=13,column=0,pady=(20,0))

drop_tables_button = Button(root, text="Drop Tables",command=drop_tables)
drop_tables_button.grid(row=14,column=0,pady=20)

#mainloop line
root.mainloop()
