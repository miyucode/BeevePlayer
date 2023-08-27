from tkinter import *
from tkinter.ttk import *
from src.win10toast.win10toast import ToastNotifier
from random import *

import tkinter as tk
import time
import ctypes
import tkinter.messagebox as mb
import os

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
app.iconbitmap("src/icons/icon.ico")

# code:

app.config(bg="#333333")
app.mainloop()