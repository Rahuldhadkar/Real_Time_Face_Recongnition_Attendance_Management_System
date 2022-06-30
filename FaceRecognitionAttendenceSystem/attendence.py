from tkinter import*
from tkinter import ttk
import csv


mydata=[]

class Attendence:        
    def __init__(self,root):
        self.root=root
        self.root.geometry("770x600+300+100")
        self.root.title("Attendence")

        main_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="",font=("times new roman",12,"bold"))
        main_frame.place(x=10,y=5,width=750,height=580)

        #scroll bars
        scroll_x=ttk.Scrollbar(main_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        style=ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white"
                        )
        style.map('Treeview',background=[('selected','lightblue')],foreground=[('selected','black')])

        self.attendence_table=ttk.Treeview(main_frame,column=("id","section","roll","name","dep","phone","time","date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendence_table.xview)
        scroll_y.config(command=self.attendence_table.yview)

        self.attendence_table.heading("id",text="ID")
        self.attendence_table.heading("section",text="Section")
        self.attendence_table.heading("roll",text="Roll No")
        self.attendence_table.heading("name",text="Name")
        self.attendence_table.heading("dep",text="Department")
        self.attendence_table.heading("phone",text="Contact No")
        self.attendence_table.heading("time",text="Time")
        self.attendence_table.heading("date",text="Date")

        self.attendence_table["show"]="headings"

        self.attendence_table.column("id",width=20)
        self.attendence_table.column("section",width=40)
        self.attendence_table.column("roll",width=50)
        self.attendence_table.column("name",width=200)
        self.attendence_table.column("dep",width=60)
        self.attendence_table.column("phone",width=65)
        self.attendence_table.column("time",width=50)
        self.attendence_table.column("date",width=50)

        self.attendence_table.pack(fill=BOTH,expand=1)
        self.attendence_table.bind("<ButtonRelease>",self.importCSV())
    
    def fetch_data(self,rows):
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata=[]
        fln=open("attendence.csv")
        #fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with fln as myfile:
            csvread=csv.reader(myfile,delimiter=",")

            for i in csvread:
                mydata.append(i)

            self.fetch_data(mydata)


if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()