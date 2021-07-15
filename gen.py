import face_recognition
import numpy as np
from face_recognition.api import face_locations
import os

dir = os.path.dirname(__file__)
encdir = os.path.join(dir,'encodings')
imgdir = os.path.join(dir,'images')

for file in os.listdir(imgdir):
    if file.endswith('.jpg') or file.endswith('.JPG'):
        f = os.path.join(imgdir, file)
        file = file[:-4]
        enf = os.path.join(encdir,file)
        img = face_recognition.load_image_file(f)
        fenc = face_recognition.face_encodings(img)[0]
        o = open(enf, "w")
        np.savetxt(o, fenc)
        o.close()
