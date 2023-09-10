from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from billing import billing
import time
#  pip install pillow
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed By David Kamundi")
        self.root.config(bg="white")
        #===title===
        # self.icon_title=PhotoImage(file="logo.jpg")
        title=Label(self.root,text="Inventory Management System",font=("Bradley Hand", 40,"bold"),bg="#010c48",fg="White").place(x=0,y=0,relwidth=1,height=70)
 
        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand").place(x=1100,y= 10,height=30,width=150)
        
        #===clock===
        self.lbl_clock=Label(self.root,text="Welcome to UEAB-Dairy Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS" ,font=("Bradley Hand",15),bg="#010c48",fg="White")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left Menu===
        # self.left_MenuLogo=Image.open("")
        # self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        # self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftMenu.place(x=0,y=102,width=200,height=565)

        # lbl_menuLogo=Label(leftMenu,image=self.MenuLogo)
        # lbl_menuLogo.pack(side=TOP,fill=X)

        # self.icon_title=PhotoImage(file=" ")
        self.update_date_time()
        lbl_menu=Label(leftMenu,text="Menu",font=("Bradley Hand",20),bg="#FFD700",bd=3,cursor="hand").pack(side=TOP,fill=X)
        
        btn_employee=Button(leftMenu,text="Employee",command=self.employee,compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)
        btn_supplier=Button(leftMenu,text="Supplier",command=self.supplier,compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)
        btn_category=Button(leftMenu,text="Category", command=self.category,compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)
        btn_product=Button(leftMenu,text="Product",command=self.product,compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)
        btn_sales=Button(leftMenu,text="Billing",command=self.billing,compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)
        btn_exit=Button(leftMenu,text="Exit",compound=LEFT,padx=5,anchor="w",font=("Bradley Hand",20,"bold"),bg="white",bd=3,cursor="hand").pack(side=TOP,fill=X)

        #===contend===

        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="green",font=("times new roman",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="green",font=("times new roman",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="Category\n[ 0 ]",bd=5,relief=RIDGE,bg="green",font=("times new roman",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Product\n[ 0 ]",bd=5,relief=RIDGE,bg="green",font=("times new roman",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="green",font=("times new roman",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        #===footer===
        lbl_footer=Label(self.root,text="UEAB-Dairy Inventory Management System | Developed by David Kamundi\n Contact +254-7-06-211-261" ,font=("Bradley Hand",15),bg="#010c48",fg="White").pack(side=BOTTOM,fill=X)
        
        #=========
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billing(self.new_win)

    def update_date_time(self):
        time_=time.strftime("%I: %M: %S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to UEAB-Dairy Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

 

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()

    