from PIL import Image
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime

class Face_Recognition:
    def face_recognizer():
        update=messagebox.askyesno("Warning","Do you open Face Detector Now?")
        if update>0:
                    
            #===== mark attendence function ==================

            def mark_attendence(i,r,n,d,p,s):
                with open("attendence.csv","r+",newline="\n") as f:
                    myDataList=f.readlines()
                    name_list=[]

                    for line in myDataList:
                        entry=line.split((","))
                        name_list.append(entry[0])
                    
                    if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%y")
                        dtstring=now.strftime("%H:%M:%S")
                        f.writelines(f"{i},{s},{r},{n},{d},{p},{dtstring},{d1}\n")

            #===== draw border around face function ============

            def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clsf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

                coord=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clsf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))
                
                    conn=mysql.connector.connect(user='root',password='1234',host='localhost',database='faceRecognition')    
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute("select student_id from student where student_id="+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)

                    my_cursor.execute("select Name from student where student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select roll from student where student_id="+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)

                    my_cursor.execute("select dep from student where student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)

                    my_cursor.execute("select phone from student where student_id="+str(id))
                    p=my_cursor.fetchone()
                    p="+".join(p)

                    my_cursor.execute("select sec from student where student_id="+str(id))
                    s=my_cursor.fetchone()
                    s="+".join(s)

                    if confidence>77:
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        mark_attendence(i,r,n,d,p,s)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    
                    coord = [x,y,w,h]

                return coord
            
            #===== recogniozing face function ============
            
            def recognize(img,clsf,faceCascade):
                coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clsf)
                return img
            
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clsf=cv2.face.LBPHFaceRecognizer_create() 
            clsf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clsf,faceCascade)
                cv2.imshow("Face Recognition Window",img)

                if cv2.waitKey(1)==13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()
                
        else:
            if not update:
                return