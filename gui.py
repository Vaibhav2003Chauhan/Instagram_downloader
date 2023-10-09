from tkinter import *
import instaloader
import threading
ig = instaloader.Instaloader()
# function for downloading up the  post or link 
def update_box(type):
    print(type)
    if type==0 or type==2:
        user_hedline.config(text="Enter Username")
        user_showout.config(text="Enter Username")
    else:
        user_hedline.config(text="Enter URL ")
        user_showout.config(text="Enter URL")

# function for downloading all 
def download():
    var=user_input.get()
    status_label.config(text=f"is {var}")


#  function to cancel download
def cancel():
    pass
#  function for checking up the Link that was enter

def Check(given_link):
    if given_link=="" or given_link.find('instagram')==-1 :
        return False
    return True


   



root=Tk()
root.title('Instagram Detail Fetcher')
root.geometry('900x600')
root.maxsize(900,600)
root.minsize(900,600)


Userinput=StringVar()
# main heading 
title=Label(text="INSTAGRAM DOWNLOADER" ,font=("Courie", "32", "bold") ,bg="cyan", padx=10, pady=10)
title.pack(fill='x')


f1=Frame(root)
f1.pack(padx=20 ,pady=20)
b1=Button(f1,text="Download profile picture", font=("Helventica", "12", "bold"),padx=12, pady=12,width=29, command=lambda:update_box(0))
b2=Button(f1,text="Download Videos", font=("Helventica", "12", "bold"),padx=12, pady=12,width=29 ,command=lambda:update_box(1))
b3=Button(f1,text="Download All post ", font=("Helventica", "12", "bold"),padx=12, pady=12,width=29, command=lambda:update_box(2))
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

user_hedline=Label(text="Enter Username" , font=("Helventica", "20", "bold"), bg="red")
user_hedline.pack( fill='x')


f2=Frame(root)
f2.pack(ipadx=20,ipady=20)
user_showout=Label(f2,text="Enter Username", font=("Helventica", "12", "bold"))
user_showout.pack(side=LEFT)
user_input=Entry(f2,font=("Helventica", "15"),width=40,textvariable=Userinput)
user_input.pack(side=RIGHT)


f3=Frame(root)
f3.pack()
b4=Button(f3,text="Start Download", font=("Times", "12", "bold"), padx=6, pady=8,width=30, command=download)
b5=Button(f3,text="Cancel Download", font=("Times", "12", "bold"), padx=6, pady=8,width=30, command=cancel)
b4.pack(side=LEFT)
b5.pack(side=RIGHT)
status_label=Label(text="Ready to Downoad .....", bg='cyan', fg='black',font='Helventica 12 bold', anchor='w', height=2, padx=20) 
status_label.pack(side=BOTTOM, fill='x')




root.mainloop()