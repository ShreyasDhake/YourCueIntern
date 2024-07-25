import matplotlib.pyplot as plt

def diff_plotter_2_0(time,ppg_data,ecg_data,first_filt,second_filt,third_filt,fourth_filt):
    
    xrange = [5,8]
    

    time_first = time[:-1]
    time_second = time_first[:-1]
    time_third = time_second[:-1]
    time_fourth = time_third[:-1]
    
    fig,axs = plt.subplots(6,1, sharex = True)
    fig.suptitle("Filtered Derivative Plot")

    axs[0].plot(time,ppg_data)
    #axs[0,1].plot(time,first_filt, label = "Filtered 1st Order")

    #axs[0,1].plot(time_first,first, label = "Raw 1st Order")
    axs[1].plot(time_first,first_filt)

    #axs[1,1].plot(time_second,second, label = "Raw 2nd Order")
    axs[2].plot(time_second,second_filt)

    #axs[2,1].plot(time_third,third, label = "Raw 3rd Order")
    axs[3].plot(time_third,third_filt)

    #axs[3,1].plot(time_fourth,fourth, label = "Raw 4th Order")
    axs[4].plot(time_fourth,fourth_filt)

    axs[5].plot(time,ecg_data)

    axs[0].set_xlim(xrange)

    axs[0].set_ylim([-0.25,0.35])
    axs[1].set_ylim([-0.025,0.035])
    axs[2].set_ylim([-0.0035,0.0045])
    axs[3].set_ylim([-0.0007,0.00055])
    axs[4].set_ylim([-0.00013,0.00013])
    axs[5].set_ylim([-0.18,0.8])

    axs[0].set_ylabel("PPG")
    axs[1].set_ylabel("1st")
    axs[2].set_ylabel("2nd")
    axs[3].set_ylabel("3rd")
    axs[4].set_ylabel("4th")
    axs[5].set_ylabel("ECG")


    axs[5].set_xlabel("Time (s)")

    plt.show()


def diff_plotter(title,time,first,label1,first_filt,label2,second,label3,second_filt,label4,third,label5,third_filt,label6,fourth,label7,fourth_filt,label8):
    
    time_first = time[:-1]
    time_second = time_first[:-1]
    time_third = time_second[:-1]
    time_fourth = time_third[:-1]
    
    fig,axs = plt.subplots(2,2, sharex = True, sharey=True)
    fig.suptitle(str(title))

    axs[0,0].plot(time_first,first, label = str(label1))
    axs[0,0].plot(time_first,first_filt, label = str(label2))

    axs[0,1].plot(time_second,second, label = str(label3))
    axs[0,1].plot(time_second,second_filt, label = str(label4))

    axs[1,0].plot(time_third,third, label = str(label5))
    axs[1,0].plot(time_third,third_filt, label = str(label6))

    axs[1,1].plot(time_fourth,fourth, label = str(label7))
    axs[1,1].plot(time_fourth,fourth_filt, label = str(label8))

    axs[0,0].set_xlim([5,5.01])
    axs[0,1].set_xlim([5,5.01])
    axs[1,0].set_xlim([5,5.01])
    axs[1,1].set_xlim([5,5.01])

    


    axs[0,0].legend()
    axs[1,0].legend()
    axs[0,1].legend()
    axs[1,1].legend()

    axs[1,0].set_xlabel("Time (s)")
    axs[1,1].set_xlabel("Time (s)")

    plt.show()




def sub_plotting4x4(t_title,x0,y0,y1,num1,x1,y3,y4,num2):
    fig, axs = plt.subplots(2,2,sharex = True,sharey=True)
    fig.suptitle(str(t_title))

    axs[0,0].plot(x0, y0[:,0],label='PPG')
    axs[1,0].plot(x0, y1,label='Filter PPG')

    axs[0,1].plot(x1, y3[:,0],label='PPG')
    axs[1,1].plot(x1, y4,label='Filter PPG')

    axs[0,0].set_xlim([5,8])
    axs[0,1].set_xlim([5,8])
    axs[1,0].set_xlim([5,8])
    axs[1,1].set_xlim([5,8])

    axs[0,0].legend()
    axs[0,1].legend()
    axs[1,0].legend()
    axs[1,1].legend()

    axs[1,1].set_xlabel("Time (s)")
    axs[1,0].set_xlabel("Time (s)")
    axs[1,0].set_ylabel("Amplitude")
    axs[0,0].set_ylabel("Amplitude")


    axs[0,0].set_title("AF Patient"+" "+str(num1))
    axs[0,1].set_title("AF Patient"+" "+str(num2))

def sub_plotting4x4af(t_title,x0,y0,y1,num1,x1,y3,y4,num2):
    fig, axs = plt.subplots(2,2,sharex = True,sharey=True)
    fig.suptitle(str(t_title))

    axs[0,0].plot(x0, y0[:,0],label='PPG')
    axs[1,0].plot(x0, y1,label='Filter PPG')

    axs[0,1].plot(x1, y3[:,0],label='PPG')
    axs[1,1].plot(x1, y4,label='Filter PPG')

    axs[0,0].set_xlim([0,5])
    axs[0,1].set_xlim([0,5])
    axs[1,0].set_xlim([0,5])
    axs[1,1].set_xlim([0,5])

    axs[0,0].legend()
    axs[0,1].legend()
    axs[1,0].legend()
    axs[1,1].legend()

    axs[1,1].set_xlabel("Time (s)")
    axs[1,0].set_xlabel("Time (s)")
    axs[1,0].set_ylabel("Amplitude")
    axs[0,0].set_ylabel("Amplitude")


    axs[0,0].set_title("AF Patient"+" "+str(num1))
    axs[0,1].set_title("AF Patient"+" "+str(num2))



def sub_plotting4x4mod(t_title,x0,y0,y1,y2,num1,x1,y3,y4,y5,num2):
    fig, axs = plt.subplots(2,2,sharex = True,sharey=True)
    fig.suptitle(str(t_title))

    axs[0,0].plot(x0, y0[:,0],label='PPG')
    axs[0,0].plot(x0, y0[:,1],label='ECG')
    axs[1,0].plot(x0, y1,label='Filter PPG')
    axs[1,0].plot(x0, y2,label='Filter ECG')

    axs[0,1].plot(x1, y3[:,0],label='PPG')
    axs[0,1].plot(x1, y3[:,1],label='ECG')
    axs[1,1].plot(x1, y4,label='Filter PPG')
    axs[1,1].plot(x1, y5,label='Filter ECG')

    axs[0,0].set_xlim([5,10])
    axs[0,1].set_xlim([5,10])
    axs[1,0].set_xlim([5,10])
    axs[1,1].set_xlim([5,10])

    axs[0,0].legend()
    axs[0,1].legend()
    axs[1,0].legend()
    axs[1,1].legend()

    axs[1,1].set_xlabel("Time (s)")
    axs[1,0].set_xlabel("Time (s)")


    axs[0,0].set_title("AF Patient"+" "+str(num1))
    axs[0,1].set_title("AF Patient"+" "+str(num2))

def sub_plotting4x4modaf(t_title,x0,y0,y1,y2,num1,x1,y3,y4,y5,num2):
    fig, axs = plt.subplots(2,2,sharex = True,sharey=True)
    fig.suptitle(str(t_title))

    axs[0,0].plot(x0, y0[:,0],label='PPG')
    axs[0,0].plot(x0, y0[:,1],label='ECG')
    axs[1,0].plot(x0, y1,label='Filter PPG')
    axs[1,0].plot(x0, y2,label='Filter ECG')

    axs[0,1].plot(x1, y3[:,0],label='PPG')
    axs[0,1].plot(x1, y3[:,1],label='ECG')
    axs[1,1].plot(x1, y4,label='Filter PPG')
    axs[1,1].plot(x1, y5,label='Filter ECG')

    axs[0,0].set_xlim([5,10])
    axs[0,1].set_xlim([5,10])
    axs[1,0].set_xlim([5,10])
    axs[1,1].set_xlim([5,10])

    axs[0,0].legend()
    axs[0,1].legend()
    axs[1,0].legend()
    axs[1,1].legend()

    axs[1,1].set_xlabel("Time (s)")
    axs[1,0].set_xlabel("Time (s)")


    axs[0,0].set_title("AF Patient"+" "+str(num1))
    axs[0,1].set_title("AF Patient"+" "+str(num2))

