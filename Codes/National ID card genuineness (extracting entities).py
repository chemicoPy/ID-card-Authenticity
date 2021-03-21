import numpy as np
from numpy import *
import pandas as pd
from pandas import DataFrame, Series
from numpy.random import randn
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import re
from skimage.io import imread, imshow
from termcolor import colored
import keras
import h5py
import cv2
from scipy import spatial
from keras.layers import Flatten, Dense, Input, concatenate
from keras.layers import MaxPooling2D
from keras.layers import Activation, Dropout
from keras.models import Model
from keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from scipy.fftpack import dct, idct
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
from pytesseract import *

id_card = cv2.imread("ID card (original) 1.jpg")
gray = cv2.cvtColor(id_card, cv2.COLOR_RGB2GRAY)

gray, img_bin = cv2.threshold(gray, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2,1), np.uint8)
id_card = cv2.erode(gray,kernel, iterations=1)
id_card = cv2.dilate(id_card, kernel, iterations=1)

exp_txt = pytesseract.image_to_string(id_card)
print(exp_txt)


with open("exp.txt", mode = "w") as file:
    file.write(exp_txt)
    file.close()

open_file = open("exp.txt",'r')
with open_file as p:
    lines = p.readlines()

""" These 2 commented lines of code is for having the extracted entities in Dictionary form - this datatype would be exposed
to an API of Nigeria National ID card details for verification"""
#data = pd.DataFrame(lines)
#print(data.to_dict())


imshow(gray)







