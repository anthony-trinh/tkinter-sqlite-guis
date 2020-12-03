from tkinter import * 
from PIL import ImageTk,Image
import sqlite3


###---------------------------------- GLOBAL VARIABLES ----------------------------------###


#some variables
root=Tk()
root.title("Employees")

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
    c.execute("INSERT INTO employees VALUES (:employee_id, :f_name, :l_name, :dob, :gender, :age, :address, :city, :province, :postal_code, :phone, :email, :hospital_id)",
        {
            'employee_id': employee_id.get(),
            'f_name': f_name.get(),
            'l_name': l_name.get(), 
            'dob': dob.get(),
            'gender': gender.get(),
            'age': age.get(),
            'address':  address.get(),
            'city': city.get(), 
            'province': province.get(),
            'postal_code': postal_code.get(),
            'phone': phone.get(),
            'email': email.get(),
            'hospital_id': hospital_id.get()
        })

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 

    #clear textboxes 
    employee_id.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    dob.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    province.delete(0,END)
    postal_code.delete(0,END)
    phone.delete(0,END)
    email.delete(0,END)
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
        c.execute("SELECT * FROM employees")
    else:
        c.execute(q)
    results = c.fetchall()
    print(results)
    print_result = ''

    #iterate thru results
    for elem in results:
        for i in range(len(results[0])):
            if i == 1:
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
    c.execute("DELETE FROM employees WHERE employee_id =" + selector.get())

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
    employee_id = selector.get()

    #update 
    c.execute("""
        UPDATE employees SET
        f_name = :f_name,
        l_name = :l_name,
        dob = :dob,
        gender = :gender,
        age = :age,
        address = :address,
        city = :city,
        province = :province,
        postal_code = :postal_code,
        phone = :phone,
        email = :email,
        hospital_id = :hospital_id
        WHERE employee_id = :employee_id
        """,
        {
            'f_name': f_name_editor.get(),
            'l_name': l_name_editor.get(),
            'dob': dob_editor.get(),
            'gender': gender_editor.get(),
            'age': age_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'province': province_editor.get(),
            'postal_code': postal_code_editor.get(),
            'phone': phone_editor.get(),
            'email': email_editor.get(),
            'hospital_id': hospital_id_editor.get(),
            'employee_id': employee_id
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
    c.execute("SELECT * FROM employees WHERE employee_id=" + entity_id)
    results = c.fetchall()

    #globals 
    global f_name_editor
    global l_name_editor
    global dob_editor
    global gender_editor
    global age_editor
    global address_editor
    global city_editor
    global province_editor
    global postal_code_editor
    global phone_editor
    global email_editor
    global hospital_id_editor 


    #textboxes for editor 

    f_name_editor  = Entry(editor, width=30)
    f_name_editor.grid(row=1,column=1,padx=20) 

    l_name_editor  = Entry(editor, width=30)
    l_name_editor.grid(row=2,column=1,padx=20) 

    dob_editor  = Entry(editor, width=30)
    dob_editor.grid(row=3,column=1,padx=20) 

    gender_editor  = Entry(editor, width=30)
    gender_editor.grid(row=4,column=1,padx=20) 

    age_editor = Entry(editor, width=30)
    age_editor.grid(row=5,column=1,padx=20) 

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=6,column=1,padx=20) 

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=7,column=1,padx=20) 

    province_editor = Entry(editor, width=30)
    province_editor.grid(row=8,column=1,padx=20) 

    postal_code_editor = Entry(editor, width=30)
    postal_code_editor.grid(row=9,column=1,padx=20) 

    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=10,column=1,padx=20) 

    email_editor = Entry(editor, width=30)
    email_editor.grid(row=11,column=1,padx=20) 

    hospital_id_editor = Entry(editor, width=30)
    hospital_id_editor.grid(row=12,column=1,padx=20) 

    #create text box labels 

    f_name_editor_label = Label(editor, text="First Name")
    f_name_editor_label.grid(row=1, column=0)

    l_name_editor_label = Label(editor, text="Last Name")
    l_name_editor_label.grid(row=2, column=0)

    dob_editor_label = Label(editor, text="Date of Birth")
    dob_editor_label.grid(row=3, column=0)

    gender_editor_label = Label(editor, text="Gender")
    gender_editor_label.grid(row=4, column=0)

    age_editor_label = Label(editor, text="Age")
    age_editor_label.grid(row=5, column=0)

    address_editor_label = Label(editor, text="Address")
    address_editor_label.grid(row=6, column=0)

    city_editor_label = Label(editor, text="City")
    city_editor_label.grid(row=7,column=0)

    province_editor_label = Label(editor, text="Province")
    province_editor_label.grid(row=8,column=0)

    postal_code_editor_label = Label(editor, text="Postal Code")
    postal_code_editor_label.grid(row=9,column=0)

    phone_editor_label = Label(editor, text="Phone Number")
    phone_editor_label.grid(row=10,column=0)

    email_editor_label = Label(editor, text="Email Address")
    email_editor_label.grid(row=11,column=0)

    hospital_id_editor_label = Label(editor, text="Hospital ID")
    hospital_id_editor_label.grid(row=12,column=0)

    

    #loop thru results 
    for elem in results:
        f_name_editor.insert(0,elem[1])
        l_name_editor.insert(0,elem[2])
        dob_editor.insert(0,elem[3])
        gender_editor.insert(0,elem[4])
        age_editor.insert(0,elem[5])
        address_editor.insert(0,elem[6])
        city_editor.insert(0,elem[7])
        province_editor.insert(0,elem[8])
        postal_code_editor.insert(0,elem[9])
        phone_editor.insert(0,elem[10])
        email_editor.insert(0,elem[11])
        hospital_id_editor.insert(0,elem[12])

    #save button
    save_button = Button(editor, text="Save Attributes", command=save)
    save_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    #close connection to db 
    conn.close() 




###---------------------------------- GUI RELATED CODE ----------------------------------###

#create textboxes 
employee_id = Entry(root, width=120)
employee_id.grid(row=0,column=1,padx=40,pady=(20,0)) 

f_name = Entry(root, width=120)
f_name.grid(row=1,column=1,padx=40) 

l_name = Entry(root,width=120)
l_name.grid(row=2,column=1,padx=40)

dob = Entry(root,width=120)
dob.grid(row=3,column=1,padx=40)

gender = Entry(root,width=120)
gender.grid(row=4,column=1,padx=40)

age = Entry(root, width=120)
age.grid(row=5,column=1,padx=40)

address = Entry(root, width=120)
address.grid(row=6,column=1,padx=40) 

city = Entry(root, width=120)
city.grid(row=7,column=1,padx=40) 

province = Entry(root, width=120)
province.grid(row=8,column=1,padx=40) 

postal_code = Entry(root, width=120)
postal_code.grid(row=9,column=1,padx=40) 

phone = Entry(root, width=120)
phone.grid(row=10,column=1,padx=40)

email = Entry(root, width=120)
email.grid(row=11,column=1,padx=40)

hospital_id = Entry(root, width=120)
hospital_id.grid(row=12,column=1,padx=40)


#create text box labels 
employee_id_label = Label(root, text="Employee ID")
employee_id_label.grid(row=0, column=0,padx=20,pady=(20,0))

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1,padx=20,column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2,padx=20,column=0)

dob_label = Label(root, text="Date of birth")
dob_label.grid(row=3,padx=20,column=0)

gender_label = Label(root,text="Gender")
gender_label.grid(row=4,padx=20,column=0)

age_label = Label(root,text="Age")
age_label.grid(row=5,padx=20,column=0)

address_label = Label(root, text="Address")
address_label.grid(row=6,padx=20,column=0)

city_label = Label(root, text="City")
city_label.grid(row=7,padx=20,column=0)

province_label = Label(root, text="Province")
province_label.grid(row=8,padx=20,column=0)

postal_code_label = Label(root, text="Postal Code")
postal_code_label.grid(row=9,padx=20,column=0)

phone_label = Label(root, text="Phone Number")
phone_label.grid(row=10,padx=20,column=0)

email_label = Label(root, text="Email address")
email_label.grid(row=11,padx=20,column=0)

hospital_id_label = Label(root, text="Hospital ID")
hospital_id_label.grid(row=12,padx=20,column=0)

# results field 
query_label = Label(root, text='')
query_label.grid(row=20, column=0, columnspan=2)
    

# submit button
submit_button = Button(root, text="Add Entry to DB", command=submit)
submit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_text_label = Label(root, text="Enter a query")
query_text_label.grid(row=14,column=0,padx=0)
query_text = Entry(root, width=120)
query_text.grid(row=14,column=1,padx=20)
query_button = Button(root, text="Show Results", command=query)
query_button.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# selector 
selector_label = Label(root, text="Select ID")
selector_label.grid(row=17,column=0)
selector = Entry(root, width=120)
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
