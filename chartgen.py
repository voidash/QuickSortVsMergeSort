import numpy as np
import matplotlib.pyplot as plt

def generate_chart(filename: str, arr1: list, arr2: list, xlabel, ylabel):
    x = np.array(arr1)
    y = np.array(arr2) 
    fig,ax = plt.subplots()
    ax.set(
        xlabel=xlabel, 
        ylabel = ylabel,
    )
    ax.plot(x,y)
    fig.savefig(filename)

# generate_chart("square.png", [1,2], [1,2], "time" , "number of elements")