from tkinter import *
root=Tk()
root.title=('Number pad')
root.geometry=('400x400')

f1=Frame(root,height='300',width='400',bg='blue')
num=([9,8,7],[6,5,4],[3,2,1],['#','0','*'])
for c in range(4):
        root.columnconfigure(c,weight=1, minsize=50)
        root.rowconfigure(c,weight=1, minsize=50)
        for d in range(3):
                f=Frame(root,relief=SUNKEN,borderwidth=1)
                f.grid(row=c,column=d,sticky='nsew')
                l1=Label(f,text=num[c][d],bg='coral')
                l1.pack(padx=3,pady=3)

root.mainloop()