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
    c.execute("INSERT INTO medicines VALUES (:medicine_id, :dosage, :iupac_name, :generic_name, :inventory, :price, :expiration_date, :manufacturer, :hospital_id)",
        {
            "medicine_id": medicine_id.get(), 
            "dosage": dosage.get(),
            "iupac_name": iupac_name.get(),
            "generic_name": generic_name.get(),
            "inventory": inventory.get(),
            "price": price.get(), 
            "expiration_date": expiration_date.get(),
            "manufacturer": manufacturer.get(),
            "hospital_id": hospital_id.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    medicine_id.delete(0,END)
    dosage.delete(0,END)
    iupac_name.delete(0,END)
    generic_name.delete(0,END)
    inventory.delete(0,END)
    price.delete(0,END)
    expiration_date.delete(0,END)
    manufacturer.delete(0,END)
    hospital_id.delete(0,END)



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
        c.execute("SELECT * FROM medicines")
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
    c.execute("DELETE FROM medicines WHERE medicine_id =" + selector.get())

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
    medicine_id = selector.get()

    #update 
    c.execute("""
        UPDATE invoices SET
        dosage = :dosage_id,
        iupac_name = :iupac_name,
        generic_name = :generic_name,
        inventory = :inventory,
        price = :price, 
        expiration_date = :expiration_date,
        manufacturer = :manufacturer,
        hospital_id = :hospital_id
        WHERE medicine_id = :medicine_id
        """,
        {
            'dosage': dosage.get(),
            'iupac_name': iupac_name.get(),
            'generic_name': generic_name.get(),
            'inventory': inventory.get(),
            'price': price.get(),
            'expiration_date': expiration_date.get(),
            'manufacturer': manufacturer.get(), 
            'hospital_id': hospital_id.get(),
            'medicine_id': medicine_id
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
    c.execute("SELECT * FROM medicines WHERE medicine_id=" + entity_id)
    results = c.fetchall()

    #globals 
    global dosage_editor
    global iupac_name_editor
    global generic_name_editor
    global inventory_editor
    global price_editor
    global expiration_date_editor
    global manufacturer_editor
    global hospital_id_editor

    #textboxes for editor 
    dosage_editor = Entry(editor, width=75)
    dosage_editor.grid(row=1,column=1,padx=20) 

    iupac_name_editor = Entry(editor, width=75)
    iupac_name_editor.grid(row=2,column=1,padx=20) 

    generic_name_editor = Entry(editor, width=75)
    generic_name_editor.grid(row=3,column=1,padx=20) 

    inventory_editor = Entry(editor, width=75)
    inventory_editor.grid(row=4,column=1,padx=20) 

    price_editor = Entry(editor, width=75)
    price_editor.grid(row=5,column=1,padx=20) 

    expiration_date_editor = Entry(editor, width=75)
    expiration_date_editor.grid(row=6,column=1,padx=20) 

    manufacturer_editor = Entry(editor, width=75)
    manufacturer_editor.grid(row=7,column=1,padx=20) 

    hospital_id_editor = Entry(editor, width=75)
    hospital_id_editor.grid(row=8,column=1,padx=20) 


    #create text box labels 
    dosage_editor_label = Label(editor, text="Dosage")
    dosage_editor_label.grid(row=1, column=0)

    iupac_name_editor_label = Label(editor, text="IUPAC Name")
    iupac_name_editor_label.grid(row=2, column=0)

    generic_name_editor_label = Label(editor, text="Generic Name")
    generic_name_editor_label.grid(row=3, column=0)

    inventory_editor_label = Label(editor, text="Inventory")
    inventory_editor_label.grid(row=4, column=0)

    price_editor_label = Label(editor, text="Price")
    price_editor_label.grid(row=5, column=0)

    expiration_date_editor_label = Label(editor, text="Expiration Date")
    expiration_date_editor_label .grid(row=6, column=0)

    manufacturer_editor_label = Label(editor, text="Manufacturer")
    manufacturer_editor_label.grid(row=7, column=0)

    hospital_id_label = Label(editor, text="Hospital ID")
    hospital_id_label.grid(row=8, column=0)

    #loop thru results 
    for elem in results:
        dosage_editor.insert(0,elem[1])
        iupac_name_editor.insert(0,elem[2])
        generic_name_editor.insert(0,elem[3])
        inventory_editor.insert(0,elem[4])
        price_editor.insert(0,elem[5])
        expiration_date_editor.insert(0,elem[6])
        manufacturer_editor.insert(0,elem[7])
        hospital_id_editor.insert(0,elem[8])


    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
medicine_id = Entry(root, width=75)
medicine_id.grid(row=0,column=1,padx=20,pady=(20,0)) 

dosage = Entry(root, width=75)
dosage.grid(row=1,column=1,padx=20) 

iupac_name = Entry(root, width=75)
iupac_name.grid(row=2,column=1,padx=20) 

generic_name = Entry(root, width=75)
generic_name.grid(row=3,column=1,padx=20) 

inventory = Entry(root, width=75)
inventory.grid(row=4,column=1,padx=20) 

price = Entry(root, width=75)
price.grid(row=5,column=1,padx=20) 

expiration_date = Entry(root, width=75)
expiration_date.grid(row=6,column=1,padx=20) 

manufacturer = Entry(root, width=75)
manufacturer.grid(row=7,column=1,padx=20) 

hospital_id = Entry(root, width=75)
hospital_id.grid(row=8,column=1,padx=20) 


#create text box labels 
medicine_id_label = Label(root, text="Medicine ID")
medicine_id_label.grid(row=0,column=0,pady=(20,0))

dosage_label = Label(root, text="Dosage")
dosage_label.grid(row=1, column=0)

iupac_name_label = Label(root, text="IUPAC Name")
iupac_name_label.grid(row=2, column=0)

generic_name_label = Label(root, text="Generic Name")
generic_name_label.grid(row=3, column=0)

inventory_label = Label(root, text="Inventory")
inventory_label.grid(row=4, column=0)

price_label = Label(root, text="Price")
price_label.grid(row=5, column=0)

expiration_date_label = Label(root,text="Expiration Date")
expiration_date_label.grid(row=6, column=0)

manufacturer_label = Label(root,text="Manufacturer")
manufacturer_label.grid(row=7, column=0)

hospital_id_label = Label(root,text="Hospital ID")
hospital_id_label.grid(row=8, column=0)


# results field 
query_label = Label(root, text='')
query_label.grid(row=20, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=14,column=0,padx=0)
query_text = Entry(root, width=75)
query_text.grid(row=14,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=17,column=0)
selector = Entry(root, width=75)
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