import pandas as pd
from tkinter import ttk
dataset = pd.read_csv('C:\\Users\\ADmin\\Desktop\\Fraud.csv')

import tkinter as tk

my_w = tk.Tk()
my_w.geometry('500x350')
my_w.title('mini project gui')
my_w.resizable(0,0)


l1=tk.Label(my_w,text="Details",width=5,font=18)
l1.grid(row=1,column=1,padx=5,pady=10)

e1=tk.Entry(my_w,width=25,bg='#00f3ff',font=18)
e1.grid(row=1,column=2,padx=5,pady=10)

b1=tk.Button(my_w,text="search",width=9,height=1,font=18,command=lambda:mysearch())
b1.grid(row=1,column=3,padx=5)

def mysearch():
    x=dataset[['Date','amount','newbalanceOrig','City','Gender']]
    li=list(x)
    query=e1.get().strip()
    str1=dataset['nameOrig']==query
    df2=x[(str1)]
    print(df2)
    trv=ttk.Treeview(my_w,selectmode='browse')
    trv.grid(row=2,column=1,columnspan=3,padx=10,pady=20)
    




















my_w.mainloop()