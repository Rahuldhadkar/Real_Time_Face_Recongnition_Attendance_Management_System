from PIL import Image
from tkinter import messagebox
import cv2
import os
import numpy as np

class TrainDataSet:
    def train_classifier():
        update=messagebox.askyesno("Information","Do you want to Train DataSet Now?")
        if update>0:
            data_dir=("DataSet")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') #Gray Scale Image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('_')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13

            ids=np.array(ids)

            #==== Train the classifier and save ========

            clsf=cv2.face.LBPHFaceRecognizer_create() 
            clsf.train(faces,ids)
            clsf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Completed Successfully!!!")
            return
        else:
            if not update:
                return
        