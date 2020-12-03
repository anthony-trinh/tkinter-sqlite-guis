from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


###---------------------------------- GLOBAL VARIABLES ----------------------------------###


#some variables
root=Tk()
root.title("Appointments")

#create DB or connect to one 
conn = sqlite3.connect('hospital.db') 

#create cursor 
c = conn.cursor()



###---------------------------------- FUNCTIONS ----------------------------------###

def submit():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #Insert data into table 
    c.execute("INSERT INTO appointments VALUES (:appointment_id, :appointment_date, :appointment_time, :room_number, :hospital_id, :healthcard_number, :doctor_id)",
        {
            "appointment_id": appointment_id.get(), 
            "appointment_date": appointment_date.get(),
            "appointment_time": appointment_time.get(),
            "room_number": room_number.get(),
            "hospital_id": hospital_id.get(),
            "healthcard_number": healthcard_number.get(),
            "doctor_id": doctor_id.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    appointment_id.delete(0,END)
    appointment_date.delete(0,END)
    appointment_time.delete(0,END)
    room_number.delete(0,END)
    hospital_id.delete(0,END)
    healthcard_number.delete(0,END)
    doctor_id.delete(0,END)

def query():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #delete previous query 
    

    #get the query
    q = query_text.get()

    #query 
    if q=='':
        c.execute("SELECT * FROM appointments")
    else:
        c.execute(q)
    results = c.fetchall()
    print(results)
    print_result = ''

    #iterate thru results
    for elem in results:
        for i in range(len(results[0])):
            if len(results[0]) == 1:
                print_result += str(elem[i]) 
            else:
                if i==len(results[0])-1:
                    print_result += str(elem[i])
                else:
                    print_result += str(elem[i]) + "\t" 
        print_result += "\n"

    query_label["text"] = print_result


    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

def delete():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    # deleting 
    c.execute("DELETE FROM appointments WHERE appointment_id =" + selector.get())

    #clear the box 
    selector.delete(0,END)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

def save():

    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #get hospital ID 
    appointment_id = selector.get()

    #update 
    c.execute("""
        UPDATE appointments SET
        appointment_date = :appointment_date,
        appointment_time = :appointment_time,
        room_number = :room_number ,
        hospital_id = :hospital_id,
        healthcard_number = :healthcard_number,
        doctor_id = :doctor_id
        WHERE appointment_id = :appointment_id
        """,
        {
            'appointment_date': appointment_date_editor.get(),
            'appointment_time': appointment_time_editor.get(),
            'room_number': room_number_editor.get(),
            'hospital_id': hospital_id_editor.get(),
            'healthcard_number': healthcard_number_editor.get(),
            'doctor_id': doctor_id_editor.get(),
            'appointment_id': appointment_id
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




def edit():
    editor = Tk() 
    editor.title=('Editing an Entry')

    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #get entity ID 
    entity_id = selector.get() 

    #query 
    c.execute("SELECT * FROM appointments WHERE appointment_id=" + entity_id)
    results = c.fetchall()

    #globals 
    global appointment_date_editor
    global appointment_time_editor
    global room_number_editor
    global hospital_id_editor
    global healthcard_number_editor
    global doctor_id_editor



    #textboxes for editor 

    appointment_date_editor = Entry(editor, width=60)
    appointment_date_editor.grid(row=1,column=1,padx=20) 

    appointment_time_editor = Entry(editor, width=60)
    appointment_time_editor.grid(row=2,column=1,padx=20) 

    room_number_editor = Entry(editor, width=60)
    room_number_editor.grid(row=3,column=1,padx=20) 

    hospital_id_editor = Entry(editor, width=60)
    hospital_id_editor.grid(row=4,column=1,padx=20) 

    healthcard_number_editor = Entry(editor, width=60)
    healthcard_number_editor.grid(row=5,column=1,padx=20) 

    doctor_id_editor = Entry(editor, width=60)
    doctor_id_editor.grid(row=6,column=1,padx=20) 

    #create text box labels 

    appointment_date_editor_label = Label(editor, text="Appointment Date")
    appointment_date_editor_label.grid(row=1, column=0)

    appointment_time_editor_label = Label(editor, text="Appointment Time")
    appointment_time_editor_label.grid(row=2, column=0)

    room_number_editor_label = Label(editor, text="Room Number")
    room_number_editor_label.grid(row=3, column=0)

    hospital_id_editor_label = Label(editor, text="Hospital ID")
    hospital_id_editor_label.grid(row=4, column=0)

    healthcard_number_editor_label = Label(editor, text="Healthcard Number")
    healthcard_number_editor_label.grid(row=5, column=0)

    doctor_id_editor_label = Label(editor, text="Doctor ID")
    doctor_id_editor_label.grid(row=6, column=0)


    #loop thru results 
    for elem in results:
        appointment_date_editor.insert(0,elem[1])
        appointment_time_editor.insert(0,elem[2])
        room_number_editor.insert(0,elem[3])
        hospital_id_editor.insert(0,elem[4])
        healthcard_number_editor.insert(0,elem[5])
        doctor_id_editor.insert(0,elem[6])

    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
appointment_id = Entry(root, width=60)
appointment_id.grid(row=0,column=1,padx=20,pady=(20,0)) 

appointment_date = Entry(root, width=60)
appointment_date .grid(row=1,column=1,padx=20) 

appointment_time  = Entry(root,width=60)
appointment_time.grid(row=2,column=1,padx=20)

room_number = Entry(root,width=60)
room_number.grid(row=3,column=1,padx=20)

hospital_id = Entry(root,width=60)
hospital_id.grid(row=4,column=1,padx=20)

healthcard_number = Entry(root, width=60)
healthcard_number.grid(row=5,column=1,padx=20)

doctor_id = Entry(root, width=60)
doctor_id.grid(row=6,column=1,padx=20) 


#create text box labels 
appointment_id_label = Label(root, text="Appointment ID")
appointment_id_label.grid(row=0, column=0,pady=(20,0))

appointment_date_label = Label(root, text="Appointment Date")
appointment_date_label.grid(row=1, column=0)

appointment_time_label = Label(root, text="Appointment Time")
appointment_time_label.grid(row=2, column=0)

room_number_label = Label(root, text="Room Number")
room_number_label.grid(row=3, column=0)

hospital_id_label = Label(root,text="Hospital ID")
hospital_id_label.grid(row=4, column=0)

healthcard_number_label = Label(root,text="Healthcard Number")
healthcard_number_label.grid(row=5,column=0)

doctor_id_label = Label(root, text="Doctor ID")
doctor_id_label.grid(row=6, column=0)


# results field 
query_label = Label(root, text='')
query_label.grid(row=20, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=14,column=0,padx=0)
query_text = Entry(root, width=60)
query_text.grid(row=14,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=17,column=0)
selector = Entry(root, width=60)
selector.grid(row=17,column=1) 

# delete button
delete_button = Button(root, text="Delete this entry", command=delete)
delete_button.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
 
# edit button
edit_button = Button(root, text="Edit this entry", command=edit)
edit_button.grid(row=19, column=0, columnspan=2, pady=10, padx=10, ipadx=108)




###---------------------------------- MISC. ----------------------------------###


#commit changes
conn.commit() 

#close connection 
conn.close() 


root.mainloop()
