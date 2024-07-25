import scipy
import scipy.signal as signal
import numpy as np

class Filters:
    
    def __init__(self, **kwargs) -> None:
        super().__init__()

        self._kwargs=kwargs

# Butterworth Bandpass Filter
    def butter_bandpass(self, Data,  Low: float, High: float, fs:int):
        b,a = scipy.signal.butter(
            self._kwargs["Order"],[Low,High],
            self._kwargs.get('Filter_type', "bandpass") , fs=fs
        )
        filtered = scipy.signal.filtfilt(b,a,Data,axis=0)
        return filtered

# def PPG_FIR(data,low,high,freq):
#     nyq = freq/2
#     b= signal.firwin(1001, cutoff = [low/nyq, high/nyq], pass_zero = False)
#     y = signal.lfilter(b,1,data)
#     return y




# def Cheby2_band(data,order,low,high,fs):
#     w1 = low/(fs/2)
#     w2 = high/(fs/2)
#     b,a = signal.cheby2(order,rs = 40,Wn = [w1, w2],btype="bandpass",fs = fs)
#     filtered_signal = signal.lfilter(b, a, data)
#     return filtered_signal

if __name__ == '__main__':
    args = {
        "Data": np.random.randn(100),
        "Order": 4,
    }
    filt = Filters(**args)
    bfilt = filt.butter_bandpass(0.1,1,125)
    print(bfilt)