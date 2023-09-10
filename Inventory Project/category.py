from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By David Kamundi")
        self.root.config(bg="white")
        self.root.focus_force()
        ####Variables=======
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #=======title=======
        lbl_title=Label(self.root,text="Manage Product Category",font=("Segoe UI",30),bg="#00008B",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text="Enter Category Name",font=("Segoe UI",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Segoe UI",18),bg="lightyellow").place(x=50,y=170, width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("Segoe UI",18),bg="white",fg="black",cursor="hand").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("Segoe UI",18),bg="white",fg="black",cursor="hand").place(x=520,y=170,width=150,height=30)

        #=====Category Details==========

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=250)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        self.categoryTable.heading("cid",text="C ID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("cid",width=100)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        # #===images=====
        # self.im1=Image.open("Pictures/dairy.jpg")
        # self.im1=self.im1.resize((500,200),Image.LANCZOS)
        # self.im1=ImageTk.PhotoImage(self.im1)

        # self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        # self.lbl_im1.place(x=80,y=270)

        # self.show()
#==========Functions=============

    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           if self.var_name.get()=="":
               messagebox.showerror("Error","Category name is REQUIRED!",parent=self.root)
           else:
               cur.execute("Select * from category where name=?",(self.var_name.get(),))
               row=cur.fetchone()
               if row !=None:
                   messagebox.showerror("Error","Category is already taken, try a different one",parent=self.root)
               else:
                   cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                   con.commit()
                   messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                   self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content["values"]
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Kindly select a category",parent=root)
            else:
               cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
               row=cur.fetchone()
               if row ==None:
                   messagebox.showerror("Error","Invalid cid",parent=self.root)
               else:
                   op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                   if op==True:
                       cur.execute("delete from category where cid=?",(self.var_cat_id.get()))
                       con.commit()
                       messagebox.showinfo("delete","Category Deleted Successfuly",parent=self.root)
                       self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()