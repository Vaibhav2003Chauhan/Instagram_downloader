from tkinter import *
# function for downloading up the  post or link 
def download():
    print("HELLO")
    var=user_input.get()
    print(f" the user input is {var}")



root=Tk()
root.title('Instagram Detail Fetcher')
root.geometry('900x800')
# root.maxsize(900,800)
root.minsize(900,800)
# main heading 
heading1=Label(root,text="Instagram downloader",font=" Courie 38 bold ",bg="cyan")
heading1.pack(fill='x')

user_input=StringVar()
f1=Frame(root)
f1.pack(padx=10,pady=20)
user_giveninput=Entry(f1, textvariable=user_input,width=80)

user_heading=Label(f1,font=('Times,15,itaic'),text="Enter username ")
user_heading.grid(row=0, column=3)
user_giveninput.grid(row=3,column=3)
b1=Button(f1,text="download",relief=SUNKEN, command=download)
b1.grid(row=4, column=3)
# status bar at bottom 
data_label=Label(text="status shows here", bg='cyan', fg='black',font='Times 22 ',height=2)
data_label.pack(side=BOTTOM, fill='x')


root.mainloop()