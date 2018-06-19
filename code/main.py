from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import os
import numpy as np
import pdb
import monthly
from dates import Dates as dt
import tkinter as tk


#------------------------------TODO LIST---------------------------------------
# -Find monthly expenditures
# -Create graphical display of money spent and money deposited
# -create graphical display of total amount
NUMLATEST = 10
def close (master):
    master.destroy()
    
def create_frames(master):
    statframe = tk.Frame(master)
    return [statframe]

def destroy_frames(frames):
    for frame in frames:
        frame.destroy()

def load_dataset(filename):
    with open (os.path.join ('..','data',filename), 'rb') as f:
        return pd.read_csv(f, parse_dates = True)
    
def statistics (frames,X):
    destroy_frames(frames)
    statframe = frames[0]
    pdb.set_trace()
    tk.Label(statframe, text="The latest " + str(NUMLATEST) +"entries" 
             +"of your statement").pack(side=tk.LEFT)
    fiveFreq = tk.Listbox(statframe)
    for i in range(0,NUMLATEST):
        fiveFreq.insert(i,X[i,1])
    fiveFreq.pack(side=tk.RIGHT)
    statframe.pack(expand=tk.YES)
    
def line_plot(frames, X, master):
    fig = Figure (figsize=(5,5),dpi=100)
    f = fig.add_subplot(111)
    X[pd.isnull(X[:,3]),3]=0
    X[pd.isnull(X[:,2]),2]=0
    spending = X[:,2]*-1 + X[:,3]
#    pdb.set_trace()
    #TODO: find way to display years as x labels for a number of transactions
    #that isn't clustered
        #TODO: Create datetime objects for the dates
    #TODO: Find way to delete canvas to make the GUI more dynamic
    f.plot (X[:,0],spending, scalex=True)
    canvas = FigureCanvasTkAgg (fig, master)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill = tk.BOTH, expand=True)
    canvas._tkcanvas.pack(side=tk.TOP, fill = tk.BOTH, expand=True)
    canvas.delete("all")

if __name__ == '__main__':
    read = load_dataset("visa.csv")
    X = read.values
#    monthly.find_Monthly_Expenditure(X)
    root = tk.Tk()
    mainmenu = tk.Menu(root)
    frames = create_frames(root)
    mainmenu.add_command(label="stop", command = lambda: close(master=root))
    statmenu = tk.Menu(mainmenu,tearoff=0)
    statmenu.add_command(label= str(NUMLATEST)+" latest transactions", 
                         command = 
                         lambda: statistics(frames,X))
    statmenu.add_command(label="linear graph trans.", command = lambda: 
        line_plot(frames, X, root))
    mainmenu.add_cascade(label="stats", menu=statmenu)
    root.config(menu=mainmenu)
    root.mainloop()

