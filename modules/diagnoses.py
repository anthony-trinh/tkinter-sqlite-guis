from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


###---------------------------------- GLOBAL VARIABLES ----------------------------------###


#some variables
root=Tk()
root.title("Diagnoses")

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
    c.execute("INSERT INTO diagnosises VALUES (:diagnosis_id, :results, :appointment_id)",
        {
            "diagnosis_id": diagnosis_id.get(), 
            "results": results.get(),
            "appointment_id": appointment_id.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    diagnosis_id.delete(0,END)
    results.delete(0,END)
    appointment_id.delete(0,END)

def query():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #get the query
    q = query_text.get()

    #query 
    if q=='':
        c.execute("SELECT * FROM diagnosises")
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
    c.execute("DELETE FROM diagnosises WHERE diagnosis_id =" + selector.get())

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
    diagnosis_id  = selector.get()

    #update 
    c.execute("""
        UPDATE diagnosises SET
        diagnosis_id  = :diagnosis_id,
        results  = :results,
        appointment_id = :appointment_id
        WHERE diagnosis_id  = :diagnosis_id 
        """,
        {
            'results': results_editor.get(),
            'appointment_id': appointment_id_editor.get(),
            'diagnosis_id': diagnosis_id
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
    c.execute("SELECT * FROM diagnosises WHERE diagnosis_id=" + entity_id)
    results = c.fetchall()

    #globals 
    global results_editor
    global appointment_id_editor

    #textboxes for editor 
    results_editor = Entry(editor, width=30)
    results_editor.grid(row=0,column=1,padx=20) 

    appointment_id_editor = Entry(editor, width=30)
    appointment_id_editor.grid(row=1,column=1,padx=20) 

    #create text box labels 
    results_editor_label = Label(editor, text="Results")
    results_editor_label.grid(row=0, column=0)

    appointment_id_editor_label = Label(editor, text="Appointment ID")
    appointment_id_editor_label.grid(row=1, column=0)


    #loop thru results 
    for elem in results:
        results_editor.insert(0,elem[1])
        appointment_id_editor.insert(0,elem[2])


    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
diagnosis_id  = Entry(root, width=30)
diagnosis_id.grid(row=0,column=1,padx=20,pady=(20,0)) 

results = Entry(root, width=30)
results.grid(row=1,column=1,padx=20) 

appointment_id = Entry(root,width=30)
appointment_id.grid(row=2,column=1,padx=20)


#create text box labels 
diagnosis_id_label = Label(root, text="Diagnosis ID")
diagnosis_id_label.grid(row=0, column=0,pady=(20,0))

results_label = Label(root, text="Results")
results_label.grid(row=1, column=0)

appointment_id_label = Label(root, text="Appointment ID")
appointment_id_label.grid(row=2, column=0)


# results field 
query_label = Label(root, text='')
query_label.grid(row=20, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=14,column=0,padx=0)
query_text = Entry(root, width=30)
query_text.grid(row=14,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=17,column=0)
selector = Entry(root, width=30)
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
