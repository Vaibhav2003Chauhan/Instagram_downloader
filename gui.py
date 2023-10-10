from tkinter import *
import instaloader
from  time import sleep
import threading
ig = instaloader.Instaloader()

downloading=0 
queue=[]
# function for downloading up the  post or link 

def update_box(type):
    # global way
    print(type)
    Type.set(type)
    if type==0 :
        user_hedline.config(text="Enter Username")
        user_showout.config(text="Enter Username")
    elif type==2:
        user_hedline.config(text="Download all Post")
        user_showout.config(text="Enter")

    else:
        user_hedline.config(text="Enter URL ")
        user_showout.config(text="Enter URL")

# function for downloading all 
def download():
    global downloading
    downoading = 1
    while(len(queue)>0):
        iteml=queue.pop()
        user_input=iteml[0]
        type=iteml[1]
        trie=0
        if type==0 :
            status_label.config(text =f" Downloading the Profile Pic for user {user_input} ....")
        elif type==1 :
            status_label.config(text= f"Downloading out the Video from Link {user_input} .....")
        else:
            status_label.config(text=f"Downloading All Post from the {user_input}....")

        while trie < 3:
            try:
                # to download profile picture
                if type==0:
                    ig.download_profile(user_input , profile_pic_only=True)
                    break

                # to download video or particular post
                elif type==1:
                    shortcode=user_input.split("/")[4]
                    post = instaloader.Post.from_shortcode(ig.context,shortcode)
                    ig.download_post(post,target="downloads")
                    break

                # to download all posts 
                else:
                    profile = instaloader.Profile.from_username(ig.context,user_input)
                    for post in profile.get_posts():
                        ig.download_post(post, target=profile.username)
                    break
            except:
                trie=trie+1
                print(" Not getting output .....")

        if trie==3:
            status_label.config(text="Sorry There is an error occur......")
        else:
            status_label.config(text="Download Successfull .......")
            sleep(4)

        sleep(2)
        status_label.config(text="Ready to Download ......")
        downloading=0



#  function to cancel download
def cancel():
    global queue
    queue=[]
    
#  function for checking up the Link that was enter

def Check(given_link):
    if given_link=="" or given_link.find('instagram')==-1 :
        status_label.config(text="PLease Enter a valid link or username ....")
        return False
    
    return True

# initialize downloading

def start(user_input,type):
    
    global queue
    # print(user_input)
    # print("HELLO")
    # print(type)
    if type == 1  and (not Check(user_input)) :
        return

    queue.append((user_input,type))
    if downloading==0:
        print(user_input)
        t1 = threading.Thread(target=download, args=())
        t1.start()


   



root=Tk()
root.title('Instagram Detail Fetcher')
root.geometry('900x600')
root.maxsize(900,600)
root.minsize(900,600)


Userinput=StringVar()
Type=IntVar()
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
b4=Button(f3,text="Start Download", font=("Times", "12", "bold"), padx=6, pady=8,width=30, command=lambda:start(Userinput.get(),Type.get()))
b5=Button(f3,text="Cancel Download", font=("Times", "12", "bold"), padx=6, pady=8,width=30, command=lambda:cancel)
b4.pack(side=LEFT)
b5.pack(side=RIGHT)
status_label=Label(text="Ready to Downoad .....", bg='cyan', fg='black',font='Helventica 12 bold', anchor='w', height=2, padx=20) 
status_label.pack(side=BOTTOM, fill='x')




root.mainloop()