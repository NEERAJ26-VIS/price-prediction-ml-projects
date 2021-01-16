import pandas as pd
import numpy as np

from tkinter import *
from mywindow import LRwindow
import pickle

window = Tk() # to create a window
lrw = LRwindow(window) # pass empty window to mywindow
window.title("House price prediction") # set title to window
window.mainloop() # this will keep the window alive

f=open("LR_without_scaling.sav","rb")
model=pickle.load(f)
f.close()


