import tkinter as tk
from tkinter.filedialog import askopenfilename
import processing as pc
from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
import cv2
import numpy as np
from matplotlib import pyplot as plt
import cv2
import glob
import os,fnmatch
from skimage.data import coins
from skimage.morphology import label, remove_small_objects
from skimage.measure import regionprops, find_contours
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy
from scipy import stats
#from sklearn.grid_search import RandomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV
#from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
import tkinter.scrolledtext as st
import tkinter.scrolledtext as scrolledtext
from sklearn.svm import SVC
from skimage.measure import compare_ssim
import warnings

image_file = None
originimage = None
proceimage = None


def resize(w, h, w_box, h_box, pil_image):
    
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    # print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w * factor)
    height = int(h * factor)
    
    return pil_image.resize((width, height), Image.ANTIALIAS)


def open_image():
    global image_file
    filepath = askopenfilename()
    #############################################
    cap = cv2.VideoCapture(filepath)
    if(cap.isOpened() == False):
        print("Error Opening Video Stream Or File")
    while(cap.isOpened()):
        ret, frame =cap.read()
        if ret == True:
            cv2.imshow('frame', frame)
            if cv2.waitKey(25)  == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
    print('Video Completed Frame Process started..');
    ###################################################
    vidcap = cv2.VideoCapture(filepath)
    success,image = vidcap.read()
    count = 0
    import os
    dir = "./Database/Test/Abuse";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Abuse Removed')
    dir = "./Database/Test/Arrest";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Arrest Removed')
    dir = "./Database/Test/Arson";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Removed')
    dir = "./Database/Test/Assault";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Assault Removed')
    dir = "./Database/Test/Burglary";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Burglary Removed')
    dir = "./Database/Test/Explosion";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Explosion Removed')
    dir = "./Database/Test/Fighting";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Fighting Removed')
    dir = "./Database/Test/Normal";
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        print('Normal Removed')
    while success:
        #cv2.imwrite("Database\\Train\\Abuse\\frame%d.png" % count, image)     # save frame as JPEG file
        if count == 155:
            print('Start')
            cv2.imwrite("Database\\Test\\Abuse\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Arrest\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Arson\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Assault\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Burglary\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Explosion\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Fighting\\frame%d.png" % count, image)     # save frame as JPEG file
            cv2.imwrite("Database\\Test\\Normal\\frame%d.png" % count, image)     # save frame as JPEG file
        #print("Database\\Train\\Burglary\\frame%d.png" % count, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print('Frame Process Completed..');
    image_file = Image.open("Database\\Test\\Abuse\\frame155.png")
    w_box = 500
    h_box = 350
    showimg(image_file, imgleft, w_box, h_box)
    showimg(image_file, imgright, w_box, h_box)
    ##############################################
    


def showimg(PIL_img, master, width, height):
    
    w, h = PIL_img.size
   
    img_resize = resize(w, h, width, height, PIL_img)
    # Image 2 ImageTk
    Tk_img = ImageTk.PhotoImage(image=img_resize)
    
    master.config(image=Tk_img)
    master.image = Tk_img



def Otsu():
    PIL_gary,PIL_Otsu = pc.Otus_hold(image_file)
    w_box = 500
    h_box = 350
    showimg(PIL_gary, imgleft, w_box, h_box)
    showimg(PIL_Otsu, imgright, w_box, h_box)
    histleft.config(image=None)
    histleft.image = None
    histright.config(image=None)
    histright.image = None
###############################################

def selection():
    
    choice = var.get()
    if choice == 1:
        m = 'Low'
    elif choice == 2:
        m = 'High'
    elif choice == 3:
        pass
    return m

def submit():
    global res
    try:
        name = int(name_Tf.get())
        m = selection()
        if name <= 102:# and m=='Low':
            text=m+'Risk:1. Vitamin-C-34 2. Zinc-17 3. B-complex-17 4. Cloth Masks-6 5. Sanitizer-1 6. Liquid Hand Wash-1 7. Gloves-2pairs 8. Sodium Hypocholorate Solution-1 9. Home Isolation for 14 days 10. Dolo 650mg 11. mythaline-14 12. FabiFlu 800mg per Day'
            res=text
            file1 = open("op.txt","w")
            L = [m+"\n","Prescription::\n","1. Vitamin-C-34 \n","2. Zinc-17 \n","3. B-complex-17 \n","4. Cloth Masks-6 \n","5. Sanitizer-1 \n","6. Liquid Hand Wash-1 \n","7. Gloves-2pairs \n","8. Sodium Hypocholorate Solution-1 \n","9. Home Isolation for 14 days \n","10. Dolo 650mg \n","11. mythaline-14 \n ","12. FabiFlu 800mg per Day \n"]
            file1.writelines(L)
            file1.close()
            file1 = open("op.txt","r")
            res=file1.readlines()
            txt.insert(tk.INSERT,res)
        else:
            text='HIgh Risk admit to the hospital'
            res=text
            file1 = open("op.txt","w")
            L = [text+"\n"]
            file1.writelines(L)
            file1.close()
            file1 = open("op.txt","r")
            res=file1.readlines()
            txt.insert(tk.INSERT,res)
        return messagebox.showinfo('Result', text)
    except Exception as ep:
        return messagebox.showwarning('Result', 'Please provide valid input')

def termsCheck():
    if cb.get() == 1:
        submit_btn['state'] = NORMAL
    else:
        submit_btn['state'] = DISABLED
        messagebox.showerror('Result', 'other covid 19 symtpoms')
######################################################################
def run():
        import MAIN

root = tk.Tk()
root.title('Abnormal')
root.geometry('1100x700')
root.config(bg='white')

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='OPEN', command=open_image)
operate = tk.Menu(menubar, tearoff=0)
operate.add_command(label='OTSU',command=Otsu)
operate.add_command(label='Classify',command=run)


menubar.add_cascade(label='FILE', menu=filemenu)
menubar.add_cascade(label='Process', menu=operate)

frm = tk.Frame(root, bg='white')
frm.pack()
frm_left = tk.Frame(frm, bg='white')
frm_right = tk.Frame(frm, bg='white')
frm_left.pack(side='left')
frm_right.pack(side='right')

imgleft = tk.Label(frm_left, bg='white')
histleft = tk.Label(frm_left, bg='white')

imgright = tk.Label(frm_right, bg='white')
histright = tk.Label(frm_right, bg='white')
imgleft.pack()
histleft.pack()
imgright.pack()
histright.pack()
#################################
root.config(menu=menubar)
root.mainloop()
