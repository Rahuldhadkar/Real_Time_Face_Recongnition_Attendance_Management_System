from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector 
import cv2

class Student:        
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

        #===========  variables ===============================


        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar() 
        self.var_id=StringVar() 
        self.var_name=StringVar() 
        self.var_sec=StringVar() 
        self.var_roll=StringVar() 
        self.var_gender=StringVar() 
        self.var_dob=StringVar() 
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_address=StringVar() 
        self.var_category=StringVar() 
        self.var_search_by=StringVar() 



        ###############################################################################################################################################
        


        #1st label image
        img=Image.open(r"Images\label1.jpg")
        img=img.resize((520,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=520,height=130)

        #2nd label image
        img1=Image.open(r"Images\label2.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=520,y=0,width=520,height=130)

        #3rd label image
        img2=Image.open(r"Images\label1.jpg")
        img2=img2.resize((520,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1040,y=0,width=520,height=130)

        #background image
        img3=Image.open(r"Images\bgimg.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1520,height=710)

        #title label
        title_lbl=Label(bg_img,text="MANAGE  STUDENT  DATABASE",font=("times new roman",20,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)




        #################################################################################################################################################



        #main frame for entering student details
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=50,width=1480,height=600)



        #################################################################################################################################################




        #left label frame


        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=660,height=580)

        #upper image in the left frame
        img_left=Image.open(r"Images\students.jpg")
        img_left=img_left.resize((635,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=0,width=635,height=130)

        #current course details frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=635,height=115)

        #department label inside current course 
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,),width=18,state="readonly")
        dep_combo["values"]=("Select Department","BCA","MCA","B.Sc","M.Sc","CS","IT","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #course label inside current course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13),width=18,state="readonly")
        course_combo["values"]=("Select Course","Computer Applications","CS","IT","Civil")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)


        #Year label inside current course 
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13),width=18,state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        #Semester label inside current course 
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13),width=18,state="readonly")
        sem_combo["values"]=("Select Semester","1st-sem","2nd-sem","3rd-sem","4th-sem","5th-sem","6th-sem","7th-sem","8th-sem")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        
        ###############################################################################################################################################################


        #Student Information frame
        student_information_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        student_information_frame.place(x=10,y=250,width=635,height=300)

        #student id Label
        studentid_label=Label(student_information_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(student_information_frame,textvariable=self.var_id,width=20,font=("Calibri",13,))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #student name Label
        studentname_label=Label(student_information_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        studentname_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(student_information_frame,textvariable=self.var_name,width=20,font=("Calibri",13,))
        studentname_entry.grid(row=0,column=4,padx=10,pady=5,sticky=W)


        #section Label
        section_label=Label(student_information_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        section_combo=ttk.Combobox(student_information_frame,textvariable=self.var_sec,font=("times new roman",13),width=18,state="readonly")
        section_combo["values"]=("Select Section","A","B","C")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No Label
        rollno_label=Label(student_information_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(student_information_frame,textvariable=self.var_roll,width=20,font=("Calibri",13,))
        rollno_entry.grid(row=1,column=4,padx=10,pady=5,sticky=W)



        #gender Label
        gender_label=Label(student_information_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(student_information_frame,textvariable=self.var_gender,font=("times new roman",13),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","male","female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob Label
        dob_label=Label(student_information_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(student_information_frame,textvariable=self.var_dob,width=20,font=("Calibri",13,))
        dob_entry.grid(row=2,column=4,padx=10,pady=5,sticky=W)



        #email Label
        email_label=Label(student_information_frame,text="Email-Id:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(student_information_frame,textvariable=self.var_email,width=20,font=("Calibri",13,))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #Phone No Label
        phone_label=Label(student_information_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(student_information_frame,textvariable=self.var_phone,width=20,font=("Calibri",13,))
        phone_entry.grid(row=3,column=4,padx=10,pady=5,sticky=W)



        #address Label
        address_label=Label(student_information_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(student_information_frame,textvariable=self.var_address,width=20,font=("Calibri",13,))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #category Label
        category_label=Label(student_information_frame,text="Category:",font=("times new roman",13,"bold"),bg="white")
        category_label.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        category_combo=ttk.Combobox(student_information_frame,textvariable=self.var_category,font=("times new roman",13),width=18,state="readonly")
        category_combo["values"]=("Select Category","General","SC/ST","OBC","EWS","Other")
        category_combo.current(0)
        category_combo.grid(row=4,column=4,padx=10,pady=5,sticky=W)




        #######################################################################################################################################################


        #add photo radio buttons
        self.var_radio=StringVar()
        radioButton1 = ttk.Radiobutton(student_information_frame,variable=self.var_radio,text="Add Photo Sample",value="Yes")
        radioButton1.grid(row=6,column=0)

        #add photo sample later radio buttons
        radioButton2 = ttk.Radiobutton(student_information_frame,variable=self.var_radio,text="Add Photo Sample Later",value="No")
        radioButton2.grid(row=6,column=1)


        #######################################################################################################################################################


        #button frame for add update delete & reset button
        btn_frame=Frame(student_information_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=630,height=35)

        save_btn=Button(btn_frame,command=self.add_data,width=15,text="Save",font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update_data,width=15,text="Update",font=("times new roman",13,"bold"),bg="orange",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,width=15,text="Delete",font=("times new roman",13,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,width=15,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        ##################################################################################################################################################################


        #button frame for add photo & update photo button
        btn_frame1=Frame(student_information_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=245,width=630,height=35)

        take_photo_btn=Button(btn_frame1,command=self.Generate_dataset,width=31,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,width=31,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)



        ############################################################################################################################################################



        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=5,width=783,height=580)

        #upper image in the left frame
        img_right=Image.open(r"Images\childrenreading.jpg")
        img_right=img_right.resize((760,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=10,y=0,width=760,height=130)

        #search frame
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search Details",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=760,height=70)

        search_label=Label(search_frame,text=" Search  By: ",font=("times new roman",15),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13),width=12,state="readonly")
        search_combo["values"]=("Select","ID","Roll No","Name","Year","Department")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=0,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("Calibri",15))
        search_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        search_btn=Button(search_frame,command=self.search_by,width=8,text="Search",font=("times new roman",12,"bold"),bg="orange",fg="black")
        search_btn.grid(row=0,column=4,padx=10,pady=10)

        showall_btn=Button(search_frame,command=self.fetch_data,width=8,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=5,padx=10,pady=10)

        #table of data frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=760,height=340)

        #scroll bars
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        style=ttk.Style()
        #style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        style.map('Treeview',background=[('selected','green')])

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","roll","gender","dob","email","phone","address","category","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email-Id")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("category",text="Category")
        self.student_table.heading("photo",text="Photo Sample Status")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=150)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=200)
        self.student_table.column("category",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    #=====================================  Function to add data in database  =======================================================



    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="Select Section" or self.var_roll.get()==""  or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()==""  or self.var_category.get()=="Select Category":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_id.get(),self.var_name.get(),self.var_sec.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_category.get(),self.var_radio.get()))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Data inserted Successfully.",parent=self.root)
                except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




    #========================= fun to fetch data from database and display in student table ====================




    def fetch_data(self):
        conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()


    def search_by(self):
        conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                        self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()




    #========================= get cursor function write the selected data from table to fields ====================





    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]) 
        self.var_course.set(data[1]) 
        self.var_year.set(data[2]) 
        self.var_semester.set(data[3]) 
        self.var_id.set(data[4]) 
        self.var_name.set(data[5]) 
        self.var_sec.set(data[6]) 
        self.var_roll.set(data[7]) 
        self.var_gender.set(data[8]) 
        self.var_dob.set(data[9]) 
        self.var_email.set(data[10]) 
        self.var_phone.set(data[11]) 
        self.var_address.set(data[12]) 
        self.var_category.set(data[13])
        self.var_radio.set(data[14]) 



        
    #============================================= function to update data ============================================




    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="Select Section" or self.var_roll.get()==""  or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()==""  or self.var_category.get()=="Select Category":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
                try:
                        update=messagebox.askyesno("Update","Do you want to update this data?",parent=self.root)
                        if update>0:
                                conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
                                my_cursor=conn.cursor()
                                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,sec=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,category=%s,photo=%s where student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_sec.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_category.get(),self.var_radio.get(),self.var_id.get()))                                                                                                              
                        else:
                                if not update:
                                        return
                        messagebox.showinfo("Success","Data Updated successfully",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    #####################################################  FUN TO DELETE DATA FROM DATABASE  #################################################################################




    def delete_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="Select Section" or self.var_roll.get()==""  or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()==""  or self.var_category.get()=="Select Category":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("WARNING","Do you want to delete this data?",parent=self.root)
                        if delete>0:
                                conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
                                my_cursor=conn.cursor()
                                sql="delete from student where student_id=%s"
                                val=(self.var_id.get(),)
                                my_cursor.execute(sql,val)                                                                                                              
                        else:
                                if not delete:
                                        return
                        messagebox.showinfo("Success","Data Deleted successfully",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




    #========================= function to reset all fields ====================



    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year") 
        self.var_semester.set("Select Semester") 
        self.var_id.set("") 
        self.var_name.set("") 
        self.var_sec.set("Select Section") 
        self.var_roll.set("") 
        self.var_gender.set("Select Gender") 
        self.var_dob.set("") 
        self.var_email.set("") 
        self.var_phone.set("") 
        self.var_address.set("") 
        self.var_category.set("Select Category")
        self.var_radio.set("") 


    #==================================  function to Generate Dataset or Take Smaple  =================================


    def Generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_sec.get()=="Select Section" or self.var_roll.get()==""  or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()==""  or self.var_category.get()=="Select Category":
                messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
                try:
                        conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,sec=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,category=%s,photo=%s where student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_sec.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_category.get(),self.var_radio.get(),self.var_id.get()==id+1))                                                                                                              
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                        #=========== loading predefined data on facefrontals from opencv  =============#
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                # scaling factor = 1.3
                                # Minimum Neighbour = 5

                                for (x,y,w,h) in faces:
                                        face_cropped=img[y:y+h,x:x+w]
                                        return face_cropped

                        #cap = camera capture
                        cap = cv2.VideoCapture(0)
                        img_id=0

                        while True:
                                ret,my_frame=cap.read()
                                if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face=cv2.resize(face_cropped(my_frame),(450,450))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                        file_name_path="DataSet/user_"+str(id)+"_"+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                                        cv2.imshow("Croped Face",face)

                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break

                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Dataset Created Successfully!!!")

                except Exception as e:
                        messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    


############################################################################################################################################################



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()