#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()

def musicWindow():
    window = Tk()
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

window=Tk()
window.title('Music Window')
window.geometry("300x300")
window.configure(bg='LightSkyBlue')

selectlabel = Label(window, text= "SelectSong",bg="LightBlueSky", font = ("Algerian",8))
selectlabel.place(x=2, y=1)

listbox = listBox(window,height = 10,width = 39,activestyle = 'dotbox',bg='LightSkyBlue',borderwidth = 2, font = ("Algerian",10))
listbox.place(x=10,y=18)

scrollbar1 = Scrollbar(listbox)
scrollbar1.place(relheight = 1,relx = 1)
scrollbar1.config(command = listbox.yview)

playButton=Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font = ("Algerian",10))
playButton.place(x=30,y=200)

stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue',font = ("Algerian",10))
stop.place(x=200,y=200)

upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Algerian",10))
upload.place(x=30,y=250)

download = Button(window,text="Download",width=10,bd=1,bg="SkyBlue", font = ("Algerian",10))
download.place(x=200,y=250)

infoLabel = Label(window, text="",fg="blue", font = ("Algerian",8))
infoLabel.place(x=4, y=280)

window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()