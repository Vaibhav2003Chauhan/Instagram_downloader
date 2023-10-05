from tkinter import *
# function for downloading up the  post or link 
def download():
    print("HELLO")



root=Tk()
root.title('Instagram Detail Fetcher')
root.geometry('1000x800')
root.maxsize(1000,800)
root.minsize(1000,800)

heading1=Label(root,text="Instagram downloader",font=" Courie 40 bold ",bg="cyan")
heading1.pack(fill='x')
heading2=Label(root,text="By Vaibhav Chauhan", font="Times 30 ", bg="red" ,fg="black")
heading2.pack(fill="x")
user_input=StringVar()
f1=Frame(root)
f1.pack()
user_giveninput=Entry(f1, textvariable=user_input,width=100)

user_heading=Label(f1,font=('Times,15,itaic'),text="enter username or Link")
user_heading.grid(row=0, column=1)
user_giveninput.grid(row=1,column=2)
b1=Button(f1,text="download",relief=SUNKEN, command=download)
b1.grid(row=1, column=1)



root.mainloop()