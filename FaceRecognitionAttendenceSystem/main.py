from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
from trainDataset import TrainDataSet
from face_recognition import Face_Recognition
from attendence import Attendence

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face Recognition System")

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

###################################################################################################################################

        #background image
        img3=Image.open(r"Images\bgimg.jpeg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #title label
        title_lbl=Label(bg_img,text="ADVANCED  FACE  RECOGNITION  SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

###################################################################################################################################

        #upper 4 Buttons 1.student 2.face detector 3.attendence 4.helpdesk

        #Student button
        img4=Image.open(r"Images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40) 

        #Face Detection button
        img5=Image.open(r"Images\Face-detector.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=Face_Recognition.face_recognizer)
        b1.place(x=500,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=Face_Recognition.face_recognizer,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40) 

        #Attendence button
        img6=Image.open(r"Images\attendence.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence)
        b1.place(x=800,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40) 

        #HelpDesk button
        img7=Image.open(r"Images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40) 

###################################################################################################################################

        #Lower 4 Buttons 1.trainNetwork  2.Photos 3.Developer 4.helpdesk

        #Train Neural Network button
        img8=Image.open(r"Images\neural-network.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=TrainDataSet.train_classifier)
        b1.place(x=200,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Train Dataset",cursor="hand2",command=TrainDataSet.train_classifier,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=580,width=220,height=40) 

        #Photos button
        img9=Image.open(r"Images\photos.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=580,width=220,height=40) 

        #Developer button
        img10=Image.open(r"Images\Developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220) 
        
        b1_1=Button(bg_img,text="Developed By",cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=580,width=220,height=40) 

        #Exit button
        img11=Image.open(r"Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.quit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.quit,font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=580,width=220,height=40) 

###################################################################################################################################

    def open_img(self):
        os.startfile("DataSet")

#=====================================  Function for Buttons  ===========================================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendence(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def quit(self):
        update=messagebox.askyesno("WARNING!","Are you sure?",parent=self.root)
        if update>0:
                self.root.destroy()
                exit()
        else:
                return



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()