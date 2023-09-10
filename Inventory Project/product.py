from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By David Kamundi")
        self.root.config(bg="white")
        self.root.focus_force()

        #=======================
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()

        self.var_pid=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.category_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()


        product_frame=Frame(self.root,bd=3,relief=RIDGE, bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)


         #===title====
        title=Label(product_frame,text="Product Details Management",font=("goudy old style",18),bg="#010c48",fg="white").pack(side=TOP, fill=X)
        lbl_category=Label(product_frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=160)
        lbl_price=Label(product_frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=210)
        lbl_qty=Label(product_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=260)
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)
       
        txt_category=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=310)
        #===options====
        cmb_cat=ttk.Combobox(self.root,textvariable=self.var_category, values=self.category_list,state='readonly',justify=CENTER,)
        cmb_cat.place(x=150, y=80, width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(self.root,textvariable=self.var_supplier, values=self.sup_list,state='readonly',justify=CENTER,)
        cmb_sup.place(x=150, y=130, width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",18),bg="white").place(x=137,y=160, width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",18),bg="white").place(x=137,y=210, width=200)
        txt_qty=Entry(product_frame,textvariable=self.var_qty,font=("goudy old style",18),bg="white").place(x=137,y=260, width=200)

        cmb_status=ttk.Combobox(self.root,textvariable=self.var_status, values=("Active","Inactive"),state='readonly',justify=CENTER,)
        cmb_status.place(x=150, y=330, width=200)
        cmb_status.current(0)     

        
        #====buttons======
        btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="black",cursor="hand").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="black",cursor="hand").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="black",cursor="hand").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="black",cursor="hand").place(x=340,y=400,width=100,height=40)   

         #===searchFrame===
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,)
        cmb_search.place(x=0,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext, font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="black",cursor="hand").place(x=410,y=10,width=150,height=30)

        #===Product Details=====

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_table=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=X)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid",text="P ID")
        self.product_table.heading("Category",text="Category")
        self.product_table.heading("Supplier",text="Supplier")
        self.product_table.heading("name",text="Name")
        self.product_table.heading("price",text="Price")
        self.product_table.heading("qty",text="Qty")
        self.product_table.heading("status",text="Status")
        
        
        self.product_table["show"]="headings"

        self.product_table.column("pid",width=90)
        self.product_table.column("Category",width=100)
        self.product_table.column("Supplier",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
#==============================================================
    def fetch_cat_sup(self):
        self.category_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
             cur.execute("Select name from category")
             cat=cur.fetchall()
             self.category_list.append("Empty")
             if len(cat)>0:
                del self.category_list[:]
                self.category_list.append("Select")
                for i in cat:
                    self.category_list.append(i[0])
             
             cur.execute("Select name from supplier")
             sup=cur.fetchall()
             if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           if self.var_category.get()=="Select" or self.var_category.get()=="Empty" or self.var_supplier.get()=="Select" or self.var_name.get()=="":
               messagebox.showerror("Error","All fields are required",parent=root)
           else:
               cur.execute("Select * from product where name=?",(self.var_name.get(),))
               row=cur.fetchone()
               if row !=None:
                   messagebox.showerror("Error","Product already present, try a different one",parent=self.root)
               else:
                   cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                    self.var_category.get(),
                                    self.var_supplier.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                   ))
                   con.commit()
                   messagebox.showinfo("Success","Product Added Successfully",parent=self.root)
                   self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content["values"]
        self.var_pid.set(row[0])
        self.var_supplier.set(row[1])
        self.var_category.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

        
    def update(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
           if self.var_pid.get()=="" :
               messagebox.showerror("Error","Please select product from list",parent=root)
           else:
               cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
               row=cur.fetchone()
               if row ==None:
                   messagebox.showerror("Error","Invalid Product",parent=self.root)
               else:
                   cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=? where pid=?",(
                                    self.var_category.get(),
                                    self.var_supplier.get(),
                                    self.var_name.get(),
                                    self.var_price.get(),
                                    self.var_qty.get(),
                                    self.var_status.get(),
                                    self.var_pid.get(),
                   ))
                   con.commit()
                   messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                   self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" :
                messagebox.showerror("Error","Select Product From the List",parent=root)
            else:
               cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
               row=cur.fetchone()
               if row ==None:
                   messagebox.showerror("Error","Invalid Product",parent=self.root)
               else:
                   op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                   if op==True:
                       cur.execute("delete from product where pid=?",(self.pid.get(),))
                       con.commit()
                       messagebox.showinfo("Delete","Product Deleted Successfuly",parent=self.root)
                       self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_category.set("")
        self.var_supplier.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("")
        self.var_pid.set("")

        self.var_searchtext.set("")
        self.var_searchby.set("Select")
        self.show()
    
    def search(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtext.get()=="":  
                messagebox.showerror("Error","Search input required",parent=self.root)
           
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()

                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert("",END,values=row)
                else:
                    messagebox.showerror("Error","No record found!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error","Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()