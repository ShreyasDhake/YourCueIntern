import numpy as np
import glob
import os
from Filters import *
import pandas as pd
from scipy.signal import find_peaks


def non_overlapping_sliding_window_rms(signal, window_size):
    rms_v = []
    spike_l = []
    for i in range(0, len(signal), window_size):
        window = signal[i:i + window_size]
        rms = np.sqrt(np.mean(window ** 2))
        N_peak, _ = find_peaks(window)
        spike_l.append(len(N_peak))
        rms_v.append(rms)
    return rms_v, spike_l




def inter_peaks(signal,time):
    # Find peaks
    peaks, _ = find_peaks(signal)

    time_points = time[peaks]
    
    # Calculate peak-to-peak values
    peak_values = signal[peaks]
    peak_to_peak_values = peak_values[1:] - peak_values[:-1]
    return peak_to_peak_values,time_points



def peak_peak(y):
    peaks,_ = find_peaks(y)
    peak_to_peak_values = []
    peak_to_peak_value = y[peaks].max() - y[peaks].min()
    peak_to_peak_values.append(peak_to_peak_value)
    maxy = y[peaks].max()
    peak_to_peak_values.append(maxy)
    miny = y[peaks].min()
    peak_to_peak_values.append(miny)
    return peak_to_peak_values

def newfile_math(path):
    PPG_Mean = []
    PPG_STD = []
    ECG_Mean = []
    ECG_STD = []
    csv_files = glob.glob(os.path.join(path, '*.csv'))
    l_ength = len(csv_files)
    for j in range(l_ength):
        df = pd.read_csv(csv_files[j])
        temp_np = df.to_numpy()
        temp_np = butter_bandpass(temp_np,2,0.5,5,125)
    
        PPG_MEAN = mean_PPG(temp_np[:,1])
        PPG_Mean.append(PPG_MEAN)
        PPG_sTD = std_PPG(temp_np[:,1])
        PPG_STD.append(PPG_sTD)

        
        ECG_MEAN = mean_PPG(temp_np[:,2])
        ECG_Mean.append(ECG_MEAN)

        ECG_sTD = std_PPG(temp_np[:,2])
        ECG_STD.append(ECG_sTD)

    return PPG_Mean,PPG_STD,ECG_Mean,ECG_STD

def mean_PPG(Data):
    mean = np.mean(Data)
    return mean

def std_PPG(Data):
    std = np.std(Data)
    return std


def rms_PPG(Data):
# Calculate RMS
    rms = np.sqrt(np.mean(Data**2))
    return rms

def derivative(Data,n):
    deriv = np.diff(Data, n =n)
    return deriv


def normaliser(Data,Mean,STD):
    for i in range(len(Data)):
        Data[i] = (Data[i]-Mean)/STD
    return Data