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




###---------------------------------- FUNCTIONS ----------------------------------###

def submit():
    #connect to DB 
    conn = sqlite3.connect('hospital.db')

    #create cursor 
    c = conn.cursor()

    #Insert data into table 
    c.execute("INSERT INTO hospitals VALUES (:hospital_id, :hospital_name, :address, :city, :province, :postal_code)",
        {
            'hospital_id': hospital_id.get(),
            'hospital_name': hospital_name.get(),
            'address':  address.get(),
            'city': city.get(), 
            'province': province.get(),
            'postal_code': postal_code.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    hospital_id.delete(0,END)
    hospital_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    province.delete(0,END)
    postal_code.delete(0,END)

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
        c.execute("SELECT * FROM hospitals")
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
        print_result += "\n\n"

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
    c.execute("DELETE FROM hospitals WHERE hospital_id =" + selector.get())

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
    hospital_id = selector.get()

    #update 
    c.execute("""
        UPDATE hospitals SET
        hospital_name = :hospital_name,
        address = :address,
        city = :city,
        province = :province,
        postal_code = :postal_code
        WHERE hospital_id = :hospital_id
        """,
        {
            'hospital_id': hospital_id,
            'address': address_editor.get(),
            'hospital_name': hospital_name_editor.get(),
            'city': city_editor.get(),
            'province': province_editor.get(),
            'postal_code': postal_code_editor.get()
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
    c.execute("SELECT * FROM hospitals WHERE hospital_id=" + entity_id)
    results = c.fetchall()

    #globals 
    global hospital_name_editor
    global address_editor
    global city_editor
    global province_editor
    global postal_code_editor


    #textboxes for editor 

    hospital_name_editor  = Entry(editor, width=30)
    hospital_name_editor.grid(row=1,column=1,padx=20) 

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2,column=1,padx=20) 

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3,column=1,padx=20) 

    province_editor = Entry(editor, width=30)
    province_editor.grid(row=4,column=1,padx=20) 

    postal_code_editor = Entry(editor, width=30)
    postal_code_editor.grid(row=5,column=1,padx=20) 

    #create text box labels 

    hospital_name_editor_label = Label(editor, text="Hospital Name")
    hospital_name_editor_label.grid(row=1, column=0)

    address_editor_label = Label(editor, text="Address")
    address_editor_label.grid(row=2, column=0)

    city_editor_label = Label(editor, text="City")
    city_editor_label.grid(row=3,column=0)

    province_editor_label = Label(editor, text="Province")
    province_editor_label.grid(row=4,column=0)

    postal_code_editor_label = Label(editor, text="Postal Code")
    postal_code_editor_label.grid(row=5,column=0)

    #loop thru results 
    for elem in results:
        hospital_name_editor.insert(0,elem[1])
        address_editor.insert(0,elem[2])
        city_editor.insert(0,elem[3])
        province_editor.insert(0,elem[4])
        postal_code_editor.insert(0,elem[5])

    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
hospital_id = Entry(root, width=50)
hospital_id.grid(row=0,column=1,padx=40,pady=(20,0)) 

hospital_name = Entry(root, width=50)
hospital_name.grid(row=1,column=1,padx=40) 

address = Entry(root, width=50)
address.grid(row=2,column=1,padx=40) 

city = Entry(root, width=50)
city.grid(row=3,column=1,padx=40) 

province = Entry(root, width=50)
province.grid(row=4,column=1,padx=40) 

postal_code = Entry(root, width=50)
postal_code.grid(row=5,column=1,padx=40) 

#create text box labels 
hospital_id_label = Label(root, text="Hospital ID")
hospital_id_label.grid(row=0, column=0,padx=20,pady=(20,0))

hospital_name_label = Label(root, text="Hospital Name")
hospital_name_label.grid(row=1,padx=20,column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2,padx=20,column=0)

city_label = Label(root, text="City")
city_label.grid(row=3,padx=20,column=0)

province_label = Label(root, text="Province")
province_label.grid(row=4,padx=20,column=0)

postal_code_label = Label(root, text="Postal Code")
postal_code_label.grid(row=5,padx=20,column=0)

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
query_button.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=110)

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