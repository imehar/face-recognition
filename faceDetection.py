
# coding: utf-8

# In[12]:


import face_recognition as fr
import cv2
import os
import numpy as np

def match_faces(img_name,workdir):
    fl =[]
    os.chdir(workdir)
    unknown_img = fr.load_image_file(img_name,mode="RGB")
#    small = cv2.resize(unknown_img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    fl = fr.face_locations(unknown_img)
    try:
        face_encodings = fr.face_encodings(unknown_img,fl,2)
    except Exception:
        print("No face found, check the image passed")
    encode = np.load('encodings.npy')
    names = np.load('names.npy')
#    print(names)
    name ="Unkown.jpg"
    for faceencode in face_encodings:
        matches = fr.compare_faces(encode,faceencode)
        if True in matches:
            print("Person Identified")
            match_index = matches.index(True)
            name = names[match_index]
            break
    else:
        print("Unkown")
    for top, right, bottom, left in fl:
        cv2.rectangle(unknown_img, (left, top), (right, bottom), (0, 0, 255), 2)
    unknown_img = unknown_img[:,:,::-1]
    if not name =='Unkown.jpg':
        name = name.split('.')
        name[0] = name[0][0:len(name[0])-1]
        name = ".".join(name)
    if name !='Unkown.jpg':
        if os.path.isdir(workdir+"/Faces Identified") :
    	   	os.chdir(workdir+"/Faces Identified")
        elif not os.path.isdir(workdir+"/Faces Identified") :
            os.mkdir("Faces Identified")
            os.chdir(workdir+"/Faces Identified")
    else:
        if os.path.isdir(workdir+"/Unknown Faces Identified") :
    	   	os.chdir(workdir+"/Uknown Faces Identified")
        elif not os.path.isdir(workdir+"/Unknown Faces Identified") :
            os.mkdir("Unknown Faces Identified")
            os.chdir(workdir+"/Unknown Faces Identified")
    cv2.imwrite(name,unknown_img)
    os.chdir(workdir)
workingdir = os.getcwd()
print("Enter name of image file")
n = input()
if n.find(".")==-1:
	n = n + ".jpg"
match_faces(n,workingdir)

