from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


###---------------------------------- GLOBAL VARIABLES ----------------------------------###


#some variables
root=Tk()

#create DB or connect to one 
conn = sqlite3.connect('hospital.db') 

#create cursor 
c = conn.cursor()

c.execute("""
	CREATE TABLE nurses(
	nurse_id int, 
	nurse_license_expiry text,
	employee_id int
	)
	""")

###---------------------------------- FUNCTIONS ----------------------------------###

def submit():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #Insert data into table 
    c.execute("INSERT INTO nurses VALUES (:nurse_id, :nurse_license_expiry, :employee_id)",
        {
            "nurse_id": nurse_id.get(),
            "nurse_license_expiry": nurse_license_expiry.get(),
            "employee_id": employee_id.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    nurse_id.delete(0,END)
    nurse_license_expiry.delete(0,END)
    employee_id.delete(0,END)


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
        c.execute("SELECT * FROM nurses")
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
    c.execute("DELETE FROM nurses WHERE nurse_id =" + selector.get())

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
    nurse_id = selector.get()

    #update 
    c.execute("""
        UPDATE nurses SET
        nurse_license_expiry = :nurse_license_expiry
        WHERE nurse_id = :nurse_id
        """,
        {
            'nurse_license_expiry': nurse_license_expiry_editor.get(),
            'nurse_id': nurse_id
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
    nurse_id = selector.get() 

    #query 
    c.execute("SELECT * FROM nurses WHERE nurse_id=" + nurse_id)
    results = c.fetchall()

    #globals 
    global nurse_license_expiry_editor

    #textboxes for editor 

    nurse_license_expiry_editor  = Entry(editor, width=30)
    nurse_license_expiry_editor.grid(row=1,column=1,padx=20) 


    #create text box labels 

    hospital_name_editor_label = Label(editor, text="nurse License Expiry Date")
    hospital_name_editor_label.grid(row=1, column=0)


    #loop thru results 
    for elem in results:
        nurse_license_expiry_editor.insert(0,elem[1])

    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
nurse_id = Entry(root, width=30)
nurse_id.grid(row=0,column=1,padx=20,pady=(20,0))

nurse_license_expiry = Entry(root, width=30)
nurse_license_expiry.grid(row=1,column=1,padx=20)

employee_id = Entry(root, width=30)
employee_id.grid(row=2,column=1,padx=20)


#create text box labels 
nurse_id_label = Label(root,text="Nurse ID")
nurse_id_label.grid(row=0,column=0,pady=(20,0))

nurse_license_expiry_label = Label(root,text="License Expiry Date")
nurse_license_expiry_label.grid(row=1,column=0)

employee_id_label = Label(root,text="Employee ID")
employee_id_label.grid(row=2,column=0)




# results field 
query_label = Label(root, text='')
query_label.grid(row=15, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=7,column=0,padx=0)
query_text = Entry(root, width=30)
query_text.grid(row=7,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=11,column=0)
selector = Entry(root, width=30)
selector.grid(row=11,column=1) 

# delete button
delete_button = Button(root, text="Delete this entry", command=delete)
delete_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
 
# edit button
edit_button = Button(root, text="Edit this entry", command=edit)
edit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=108)




###---------------------------------- MISC. ----------------------------------###


#commit changes
conn.commit() 

#close connection 
conn.close() 


root.mainloop()