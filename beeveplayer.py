from tkinter import *
from tkinter.ttk import *
from src.win10toast.win10toast import ToastNotifier
from random import *

import tkinter as tk
import time
import ctypes
import tkinter.messagebox as mb
import os
import pygame
import tkinter.filedialog as fd
import getpass

def checksetupdone():
	f = open("src/config/setup.txt", "r")
	fc = f.read()
	f.close()
	if fc == "not done":
		def preferenceusermode(*args):
			usermode = darkorwhitemodeVar.get()
			preferenceusermodefile = open("src/config/colormode.txt", "w")
			preferenceusermodefile.write(usermode)
			preferenceusermodefile.close()

		def finishSetup():
			username = choiceusername.get()
			if username == "":
				app.withdraw()
				ctypes.windll.user32.MessageBoxW(0, "You must choose a correct username !", "BeevePlayer - Error", 0)
				app.deiconify()
			else:
				app.destroy()
				usernamefile = open("src/config/username.txt", "w")
				usernamefile.write(username)
				usernamefile.close()
				setupdonefile = open("src/config/setup.txt", "w")
				setupdonefile.write("done")
				setupdonefile.close()
				ctypes.windll.user32.MessageBoxW(0, "Setup is now done, restart BeevePlayer to start using it.", "BeevePlayer - Setup Done", 0)
				os.system("taskkill /f /im python.exe")

		ctypes.windll.user32.MessageBoxW(0, "Welcome on BeevePlayer, click OK to continue.", "BeevePlayer - Welcome", 0)
		app = Tk()
		app.title("BeevePlayer - Setup")
		app.geometry("500x400")
		app.resizable(False, False)
		app.iconbitmap("src/icons/icon.ico")

		# icon = PhotoImage(file="src/icons/iconcircle.png")
		# icon3 = icon.subsample(5, 5)
		# icon2 = Label(app, image=icon3, bg="#333333")
		# icon2.image = icon3
		# icon2.place(relx=0.15, rely=0.12, anchor=CENTER)

		tk.Label(app, text="\n\nWelcome on BeevePlayer !", fg="white", bg="#333333", font=("Segoe UI", 15, "bold")).pack()
		tk.Label(app, text="\nTo continue, choose an username to use BeevePlayer:\n", fg="white", bg="#333333", font=("Segoe UI", 10)).pack()

		choiceusername = Entry(app, text="username")
		choiceusername.pack() 

		tk.Label(app, text="\n", bg="#333333").pack()

		tk.Label(app, text="Do you want to use Dark Mode\nor White Mode ? (Optional):\n", fg="white", bg="#333333", font=("Segoe UI", 10, "bold")).pack()

		darkorwhitemodeVar = StringVar(app)
		darkorwhitemodeVar.set(f"Dark/White Mode")
		modes = ("Dark", "White")

		choicemode = OptionMenu(app, darkorwhitemodeVar, modes[1], *modes, command=preferenceusermode)
		choicemode.pack()

		tk.Label(app, text="\n", bg="#333333").pack()
		Button(app, text="Continue", command=finishSetup).pack()

		app.config(bg="#333333")
		app.mainloop()
	else:
		pass

checksetupdone()

app = Tk()
app.title("BeevePlayer")
app.geometry("800x500")
app.resizable(False, False)
app.iconbitmap("src/icons/icon.ico")

def credits():
	ctypes.windll.user32.MessageBoxW(0, "made by: miyucode and Beeve / actual version: 1.0", "BeevePlayer - Credits", 0)

def stopMusic():
	pygame.mixer.music.stop()
	songname.pack_forget()
	app.title("BeevePlayer")
	stopmusicbutton2.place_forget()
	choosemusicbutton2.place(relx=0.50, rely=0.15, anchor=CENTER)
	pausemusicbutton2.place_forget()
	resumemusicbutton2.place_forget()
	# songphoto1.place_forget()

def resumeMusic():
	pygame.mixer.music.unpause()
	resumemusicbutton2.place_forget()
	pausemusicbutton2.place(relx=0.35, rely=0.25, anchor=CENTER)

def pauseMusic():
	pygame.mixer.music.pause()
	pausemusicbutton2.place_forget()
	resumemusicbutton2.place(relx=0.65, rely=0.25, anchor=CENTER)

def startMusic():
	global photo
	username = getpass.getuser()
	file = fd.askopenfilename(title='Choose a music (.mp3, .waw)', filetypes=[('MP3', '*.mp3*'), ("WAW", "*.waw*")], initialdir=f"C:/Users/{username}/Desktop")
	if file == "":
		pass
	else:
		# songphoto = PhotoImage(file=file)
		# songphoto1.config(image=songphoto)
		# songphoto1.place(relx=0.50, rely=0.35)
		pygame.mixer.init()
		choosemusicbutton2.place_forget()
		songname.pack()
		songname.config(text=f"\nCurrent song:\n{file}\n")
		app.title(f"BeevePlayer - Current song: {file}")
		pygame.mixer.music.load(file)
		pygame.mixer.music.play()
		stopmusicbutton2.place(relx=0.50, rely=0.25, anchor=CENTER)
		pausemusicbutton2.place(relx=0.35, rely=0.25, anchor=CENTER)

navbar = Menu(app)
navbarmenu = Menu(navbar, tearoff=0)

navbarmenu.add_command(label="Credits", command=credits)

navbar.add_cascade(label="Settings", menu=navbarmenu)

choosemusicbutton = PhotoImage(file="src/icons/choosemusicbutton.png")
choosemusicbutton3 = choosemusicbutton.subsample(4, 4)
choosemusicbutton2 = Button(app, image=choosemusicbutton3, command=startMusic)
choosemusicbutton2.image = choosemusicbutton3
choosemusicbutton2.place(relx=0.50, rely=0.15, anchor=CENTER)

songname = tk.Label(app, text="\n", fg="white", bg="#333333", font=("Segoe UI", 10, "bold"))
songname.pack_forget()

stopmusicbutton = PhotoImage(file="src/icons/stopicon.png")
stopmusicbutton3 = stopmusicbutton.subsample(7, 7)
stopmusicbutton2 = Button(app, image=stopmusicbutton3, command=stopMusic)
stopmusicbutton2.image = stopmusicbutton3
stopmusicbutton2.place(relx=0.50, rely=0.25, anchor=CENTER)
stopmusicbutton2.place_forget()

pausemusicbutton = PhotoImage(file="src/icons/pauseicon.png")
pausemusicbutton3 = pausemusicbutton.subsample(7, 7)
pausemusicbutton2 = Button(app, image=pausemusicbutton3, command=pauseMusic)
pausemusicbutton2.image = pausemusicbutton3
pausemusicbutton2.place(relx=0.35, rely=0.25, anchor=CENTER)
pausemusicbutton2.place_forget()

resumemusicbutton = PhotoImage(file="src/icons/resumeicon.png")
resumemusicbutton3 = resumemusicbutton.subsample(7, 7)
resumemusicbutton2 = Button(app, image=resumemusicbutton3, command=resumeMusic)
resumemusicbutton2.image = resumemusicbutton3
resumemusicbutton2.place(relx=0.65, rely=0.25, anchor=CENTER)
resumemusicbutton2.place_forget()

# photo = ""
# songphoto1 = tk.Label(app)
# songphoto1.place(relx=0.50, rely=0.35)
# songphoto1.place_forget()

app.config(bg="#333333", menu=navbar)
app.mainloop()