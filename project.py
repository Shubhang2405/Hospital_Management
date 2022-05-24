from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql



def insert():
    id=e_id.get()
    name=e_name.get();
    phone=e_phone.get();
    disease=e_disease.get();
    

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="saurabh2014",database="info")
        cursor=con.cursor()
        cursor.execute("insert into patient values('"+ id +"','"+ name +"','"+ phone +"','"+ disease +"')")
        cursor.execute("commit");

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        e_disease.delete(0,'end')


        MessageBox.showinfo("Insert Status","Inserted Successfully");
        con.close();

def delete():
    if (e_id.get() == ""):
        MessageBox.showinfo("Delete Status","ID is compolsary for delete")
    else:
         con=mysql.connect(host="localhost",user="root",password="saurabh2014",database="info")
         cursor=con.cursor()
         cursor.execute("delete from patient where id='"+ e_id.get() +"'")
         cursor.execute("commit");

         e_id.delete(0,'end')
         e_name.delete(0,'end')
         e_phone.delete(0,'end')
         e_disease.delete(0,'end')

         MessageBox.showinfo("Delete Status","Deleted Successfully");
         con.close();


def update():
    id=e_id.get()
    name=e_name.get();
    phone=e_phone.get();
    disease=e_disease.get();

    if (id=="" or name=="" or phone==""  or disease=="" ):
        MessageBox.showinfo("Update Status","All Fields are required")
    else:
         con=mysql.connect(host="localhost",user="root",password="saurabh2014",database="info")
         cursor=con.cursor()
         cursor.execute("update  patient set name='"+ name +"',phone='"+ phone +"',disease='"+ disease +"' where id='"+ id +"'")
         cursor.execute("commit");

         e_id.delete(0,'end')
         e_name.delete(0,'end')
         e_phone.delete(0,'end')
         e_disease.delete(0,'end')
         

         MessageBox.showinfo("Update Status","Updated Successfully");
         con.close();

def get():
    if (e_id.get() == ""):
        MessageBox.showinfo("Fetch Status","ID is compolsary for get")
    else:
         con=mysql.connect(host="localhost",user="root",password="saurabh2014",database="info")
         cursor=con.cursor()
         cursor.execute("select * from  patient where id='"+ e_id.get() +"'")
         rows=cursor.fetchall()

         for row in rows:
             e_name.insert(0, row[1])
             e_phone.insert(0, row[2])
             e_disease.insert(0, row[3])

         

         con.close();


def show():
         con=mysql.connect(host="localhost",user="root",password="saurabh2014",database="info")
         cursor=con.cursor()
         cursor.execute("select * from  patient")
         rows=cursor.fetchall()

         for row in rows:
             insertData=str(row[0])+'         '+row[1]
             list.insert(list.size()+1, insertData)

         con.close()

    




    

root=Tk()
root.geometry("800x400")
root.title("Hospital Management System")



id=Label(root,text='Enter Patient ID',font=('bold', 15))
id.place(x=20,y=30)

name=Label(root,text='Enter Patient Name',font=('bold',15))
name.place(x=20,y=60)


phone=Label(root,text='Enter Phone No ',font=('bold',15))
phone.place(x=20,y=90);


disease=Label(root,text='Enter Disease ',font=('bold',15))
disease.place(x=20,y=120);


e_id=Entry()
e_id.place(x=200,y=30)

e_name=Entry()
e_name.place(x=200,y=60)

e_phone=Entry()
e_phone.place(x=200,y=90)

e_disease=Entry()
e_disease.place(x=200,y=120)

insert=Button(root,text="Insert",font=("italic",15),bg="skyblue",command=insert)
insert.place(x=20,y=160)

delete=Button(root,text="Delete",font=("italic",15),bg="skyblue",command=delete)
delete.place(x=100,y=160)

update=Button(root,text="Update",font=("italic",15),bg="skyblue",command=update)
update.place(x=185,y=160)

get=Button(root,text="Get",font=("italic",15),bg="skyblue",command=get)
get.place(x=278,y=160)


list=Listbox(root)
list.place(x=350,y=30)
show()

root.mainloop()
