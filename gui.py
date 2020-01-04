import tkinter as tk
import pyautogui
import time
import atomcheats
from PIL import ImageTk, Image
import os


root = tk.Tk()
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1, uniform=1)
root.title('Atom RPG Trainer')

img = ImageTk.PhotoImage(Image.open('ScreenSelector.png'))

frame = tk.Frame(root)
frame.grid()
frame.grid_columnconfigure(0, weight=1, uniform=1)
#frame.grid_columnconfigure(1, weight=1, uniform=1)

activatecheats = tk.Button(frame, text='Enable cheats', command=atomcheats.enablecheats, fg='#00aaff')
activatecheats.grid(row=1, column=0, sticky='ew')
                           
addmoney = tk.Button(frame,
                   text='Add $2000',
                   command=atomcheats.addmoney)
addmoney.grid(row=2, column=0, sticky='ew')

herobutton = tk.Button(frame, text='Hero (+100 to stats)', command=atomcheats.hero)
herobutton.grid(row=3, column=0, sticky='ew')

jetvirus = tk.Button(frame, text='Add Strange Serum', command=atomcheats.jetvirus)
jetvirus.grid(row=4, column=0, sticky='ew')

cureMe = tk.Button(frame, text='Cure Rads/Poison/Hunger', command=atomcheats.cureMe)
cureMe.grid(row=5, column=0, sticky='ew')

apbutton = tk.Button(frame, text='+50 AP for current turn', command=atomcheats.addAP)
apbutton.grid(row=6, column=0, sticky='ew')


##### AMMO ##########

ammolabel = tk.Label(frame, text='Add ammo:', fg='#00aaff')
ammolabel.grid(column=0, sticky='ew')

akammo = tk.Button(frame,
                   text='7.62x39mm',
                   command=atomcheats.addakammo)
akammo.grid(column=0, sticky='ew')

sevenmmbtn = tk.Button(frame, text='7.62x54mm', command=atomcheats.sevenmm)
sevenmmbtn.grid(column=0, sticky='ew')

fiveammo = tk.Button(frame,
                   text='5.45mm',
                   command=atomcheats.fivemm)
fiveammo.grid(column=0, sticky='ew')

ninebtn = tk.Button(frame, text='9mm', command=atomcheats.addninemm)
ninebtn.grid(column=0, sticky='ew')

tenbtn = tk.Button(frame, text='10mm', command=atomcheats.tenmm)
tenbtn.grid(column=0, sticky='ew')

twelvebtn = tk.Button(frame, text='12mm', command=atomcheats.twelvemm)
twelvebtn.grid(column=0, sticky='ew')

fourteenbtn = tk.Button(frame, text='14mm', command=atomcheats.fourteen)
fourteenbtn.grid(column=0, sticky='ew')

threeo = tk.Button(frame, text='.30', command=atomcheats.threeoseven)
threeo.grid(column=0, sticky='ew')

threefivesixbtn = tk.Button(frame, text='.356', command=atomcheats.threefivesix)
threefivesixbtn.grid(column=0, sticky='ew')

sixfourninebtn = tk.Button(frame, text='6.49mm', command=atomcheats.sixfournine)
sixfourninebtn.grid(column=0, sticky='ew')

bbsbtn = tk.Button(frame, text='BB', command=atomcheats.addbbs)
bbsbtn.grid(column=0, sticky='ew')

boltsbtn = tk.Button(frame, text='Bolts', command=atomcheats.bolts)
boltsbtn.grid(column=0, sticky='ew')

nadesbtn = tk.Button(frame, text='Grenades', command=atomcheats.givenades)
nadesbtn.grid(column=0, sticky='ew')


#quitbutton = tk.Button(frame, 
#                   text='Close trainer', 
#                   fg='red',
#                   command=quit)
#quitbutton.grid(row=15, sticky='ew')

atomlogo = tk.Label(frame, image = img)
atomlogo.grid(row=0, column=0, sticky='ew')

root.mainloop()
