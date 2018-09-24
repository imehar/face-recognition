
# coding: utf-8

# In[5]:


import face_recognition as fr
import cv2
import os
import numpy as np

def add_images(workdir):
    names = np.load('names.npy')
    encodings = np.load('encodings.npy')
    folder = os.chdir(workdir+'/images')
    for filename in os.listdir(folder):
        if not filename in names:
            print(filename)
            try:
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

workingdir = os.getcwd()
add_images(workingdir)

