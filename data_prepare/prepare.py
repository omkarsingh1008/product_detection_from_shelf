import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.coordinate_lable import coor_lbl
from tqdm import tqdm

for img in tqdm(os.listdir("ShelfImages/")):
    (coordinate,l)=coor_lbl(img)
    img_file=img.split('.')[0]
    image=plt.imread('ShelfImages/'+img)
    h,w=image.shape[0:2]
    f = open("yolo_txt/"+img_file+".txt", "w")
    for i,j in zip(l,coordinate):
        x_cen=((j[0]+j[2])/2)/w
        y_cen=((j[1]+j[3])/2)/h
        weidth=(j[2]-j[0])/w
        higth=(j[3]-j[1])/h
        f.write(f"{i} {x_cen} {y_cen} {weidth} {higth}\n")
    f.close()