
# coding: utf-8

# In[1]:


import face_recognition as fr
import cv2
import os
import numpy as np

def load_images():
    encodings =[]
    names = []
    folder = os.chdir(os.getcwd()+'/images')
    try:
        for filename in os.listdir(folder):
            print(filename)
            img = fr.load_image_file(filename,mode='RGB')
            if img is not None:
                encode = fr.face_encodings(img,None,2)[0]
                names.append(filename)
                encodings.append(encode)
        os.chdir('../')
        np.save('encodings.npy',encodings)
        np.save('names.npy',names)
    except Exception:
        print("No face found, check the image passed")
        os.chdir('../')  

load_images()

