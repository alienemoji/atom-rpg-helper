#!/usr/bin/env python3

import pyautogui

def hero():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('hero')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def addmoney():
    print("Adding rubles")
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem money 2000')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def addakammo():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 7_62mm_jhp 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 7_62mm_ap 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
    print('added 7.62mm ammos')

def jetvirus():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('AddItem JetVirus')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
    print('added strange serum')

def cureMe():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('radiation 0')
    pyautogui.press('enter')
    pyautogui.typewrite('toxic 0')
    pyautogui.press('enter')
    pyautogui.typewrite('hunger 0')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def fivemm():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 5_45mm_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 5_45mm_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
    print('added 5.45mm ammos')

def addninemm():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 9mm_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 9mm_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
    print('added 9mm ammos')

def enablecheats():
    print('Activated')
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('youshallnotpass')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def addAP():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('AP 50')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
    print('granted 50ap')

#################
# NEED TO ADD THESE TO GUI
#########################

def tenmm():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 10mm_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 10mm_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def twelvemm():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 12_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 12_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def fourteen():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 14_5mm_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 14_5mm_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def threeoseven():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 307cal_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 307cal_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def threefivesix():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 356cal_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 356cal_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def sixfournine():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 6_49mm_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 6_49mm_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def sevenmm():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem 7mm_54R 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem 7mm_54R_AP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def addbbs():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem BB_AP 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem BB_JHP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def bolts():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem Bolt 100')
    pyautogui.press('enter')
    pyautogui.typewrite('additem Bolt_AP 100')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def givebackpack():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem Backpack_2')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def givenades():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem Grenade 10')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')

def giveapomorphine():
    atomWindow = pyautogui.getWindow("Atom")
    atomWindow.minimize()
    atomWindow.maximize()
    pyautogui.hotkey('num0', 'multiply')
    pyautogui.typewrite('additem Morphine')
    pyautogui.press('enter')
    pyautogui.hotkey('num0', 'multiply')
