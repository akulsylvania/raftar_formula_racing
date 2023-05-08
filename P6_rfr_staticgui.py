import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt



# ALL FUNCTIONS NECESSARY

#OPENING CSV FILE AND GETTING ITS PATH
def select_file():

    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    if(filename == ""):
        showinfo(
            title='Selected File',
            message='No file selected',
        )

    else:
        showinfo(
            title='Selected File',
            message=filename,

        )
        # store path of selected file
        source_csv = filename
        print(source_csv)
        data_store(source_csv)




def x_select(dropdown_x,df):
    x=df[dropdown_x.get()]
    print(x.info())




#DROPDOWN MENUS
def dropdown(columns,df):

    dropdown_y = ttk.Combobox(win, state="readonly", values=columns)
    dropdown_y.grid(row = 3, column = 1, pady = 10, padx=20)

    dropdown_x = ttk.Combobox(win, state="readonly", values=columns)
    dropdown_x.grid(row=2, column=1, pady=10, padx=20)


    #generate button
    def generate(dropdown_y, dropdown_x):
        print(dropdown_y.get(),dropdown_x.get())
        plt.plot(df[dropdown_x.get()], df[dropdown_y.get()])
        plt.show()


    button = ttk.Button(text="Generate Plot", command=lambda: generate(dropdown_y, dropdown_x))
    button.place(x=200, y=175)

#convert read csv file into pandas dataframe globally
def data_store(source_csv):
    data = pd.read_csv(source_csv)
    df = pd.DataFrame(data)
    columns=df.columns.tolist()
    print(columns)
    dropdown(columns,df)





#tkinter window setup
win=tk.Tk()
win.title("Plotter")
win.geometry("500x300")

'''
#selector
selector=tk.Frame(win, bg='#ffffff')
selector.pack(side=tk.TOP)
selector.configure(width=500, height=500)


#plotter
plotter=tk.Frame(win, bg='#ffffff')
plotter.pack(side=tk.TOP)
plotter.configure(width=500, height=500)
'''

#selector features:

#open button
open_button = ttk.Button(win, text='Open a File', command=select_file)
open_button.grid(row = 1, column = 1, pady = 10, padx=200)









win.mainloop()



