import pandas as pd
import numpy as np
import glob
from Filters import *
import csv
import os
from Mathy import *
from Filters import *

my_filter = Filters(Order=4 , Filter_type="bandpass")



def Mimic_all_reader(destination):
    files = glob.glob(destination+"/*.csv")

    Collection = []

    for i in files:
        temp_df = pd.read_csv(i)
        temp_np = np.array(temp_df)
        if temp_np.shape[1] == 4:
            temp_np = np.delete(temp_np, 3, axis =1)
        else :
            pass
        #print(temp_np.shape)
        Collection.append(temp_np)
    pass
    return Collection

def Mean_std_reader(path,x):
    files = glob.glob(path+"/*.csv")
    my_filter = Filters(Order=4 , Filter_type="bandpass")
    Collection_mean = []
    Collection_std = []
    Collection_rms = []
  
    if x == "y":
        for i in files:
            temp_df = pd.read_csv(i)
            temp_np = np.array(temp_df)
         
            temp_np = my_filter.butter_bandpass(temp_np[:,1],0.5,5,125)
            
           

            mean = np.mean(temp_np)
            std = np.std(temp_np)
            rms = rms_PPG(temp_np)


            Collection_mean.append(mean)
            Collection_std.append(std)
            Collection_rms.append(rms)
        pass
    else :
        for i in files:
            temp_df = pd.read_csv(i)
            temp_np = np.array(temp_df)
            if temp_np.shape[1] == 4:
                temp_np = np.delete(temp_np, 3, axis =1)
            else :
                pass
            mean = np.mean(temp_np[:,1])
            std = np.std(temp_np[:,1])
            rms = rms_PPG(temp_np)

            Collection_mean.append(mean)
            Collection_std.append(std)
            Collection_rms.append(rms)

        pass

    return Collection_mean, Collection_std, Collection_rms
