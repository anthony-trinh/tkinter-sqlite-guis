from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


###---------------------------------- GLOBAL VARIABLES ----------------------------------###


#some variables
root=Tk()
root.title("Medical History")

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
    c.execute("INSERT INTO medical_history VALUES (:healthcard_number, :appointment_id, :diagnosis_id, :medical_desc)",
        {
            "healthcard_number": healthcard_number.get(), 
            "appointment_id": appointment_id.get(),
            "diagnosis_id": diagnosis_id.get(),
            "medical_desc": medical_desc.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    healthcard_number.delete(0,END)
    appointment_id.delete(0,END)
    diagnosis_id.delete(0,END)
    medical_desc.delete(0,END)


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
        c.execute("SELECT * FROM medical_history")
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
    c.execute("DELETE FROM medical_history WHERE healthcard_number =" + selector.get())

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
    healthcard_number = selector.get()

    #update 
    c.execute("""
        UPDATE medical_history SET
        appointment_id  = :appointment_id ,
        diagnosis_id  = :diagnosis_id ,
        medical_desc  = :medical_desc 
        WHERE healthcard_number  = :healthcard_number 
        """,
        {
            'appointment_id': appointment_id_editor.get(),
            'diagnosis_id': diagnosis_id_editor.get(),
            'medical_desc': medical_desc_editor.get(),
            'healthcard_number': healthcard_number
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
    c.execute("SELECT * FROM medical_history WHERE healthcard_number=" + entity_id)
    results = c.fetchall()

    #globals 
    global appointment_id_editor
    global diagnosis_id_editor
    global medical_desc_editor

    #textboxes for editor 
    appointment_id_editor = Entry(editor, width= 60)
    appointment_id_editor.grid(row=1,column=1,padx=20) 

    diagnosis_id_editor = Entry(editor, width= 60)
    diagnosis_id_editor.grid(row=2,column=1,padx=20) 

    medical_desc_editor = Entry(editor, width= 60)
    medical_desc_editor.grid(row=3,column=1,padx=20) 

    #create text box labels 
    appointment_id_editor_label = Label(editor, text="Appointment ID")
    appointment_id_editor_label.grid(row=1, column=0)

    diagnosis_id_editor_label = Label(editor, text="Diagnosis ID")
    diagnosis_id_editor_label.grid(row=2, column=0)

    medical_desc_editor_label = Label(editor, text="Medical")
    medical_desc_editor_label.grid(row=3, column=0)

    #loop thru results 
    for elem in results:
        appointment_id_editor.insert(0,elem[1])
        diagnosis_id_editor.insert(0,elem[2])
        medical_desc_editor.insert(0,elem[3])


    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
healthcard_number = Entry(root, width= 60)
healthcard_number.grid(row=0,column=1,padx=20,pady=(20,0)) 

appointment_id = Entry(root, width= 60)
appointment_id.grid(row=1,column=1,padx=20) 

diagnosis_id = Entry(root,width= 60)
diagnosis_id.grid(row=2,column=1,padx=20)

medical_desc = Entry(root,width= 60)
medical_desc.grid(row=3,column=1,padx=20)



#create text box labels 
healthcard_number_label = Label(root, text="Healthcard Number")
healthcard_number_label.grid(row=0, column=0,pady=(20,0))

appointment_id_label = Label(root, text="Appointment ID")
appointment_id_label.grid(row=1, column=0)

diagnosis_id_label = Label(root, text="Diagnosis ID")
diagnosis_id_label.grid(row=2, column=0)

medical_desc_label = Label(root, text="Medical Description")
medical_desc_label.grid(row=3, column=0)


# results field 
query_label = Label(root, text='')
query_label.grid(row=20, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=14,column=0,padx=0)
query_text = Entry(root, width= 60)
query_text.grid(row=14,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=17,column=0)
selector = Entry(root, width= 60)
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
