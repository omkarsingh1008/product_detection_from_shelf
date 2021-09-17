import pandas as pd

def coor_lbl(img):
    cols = ["image_name", "x_i", "y_i", "w_i", "h_i", "b_i"]
    master_df = pd.read_csv("annotations.csv", 
                        names=cols)


    codnte_columns = master_df.columns[1:-1]
    coordinate = master_df[master_df["image_name"]==img][codnte_columns]
    coordinate = coordinate.values.tolist()
    label = master_df[master_df["image_name"]==img]['b_i']
    l=list(label)
    return (coordinate, l)