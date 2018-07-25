#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 24, 2018 11:24:48 PM

import os
from lib import deckList, imageDownload, deckAssembly

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from lib import unknown_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Insert_Decklist (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Insert_Decklist(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Insert_Decklist (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Insert_Decklist():
    global w
    w.destroy()
    w = None


class Insert_Decklist:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("316x311+650+150")
        top.title("Insert Decklist")
        top.configure(background="#d9d9d9")

        self.decklist = Text(top)
        self.decklist.place(relx=0.06, rely=0.23, relheight=0.56, relwidth=0.84)
        self.decklist.configure(background="white")
        self.decklist.configure(font="TkTextFont")
        self.decklist.configure(foreground="black")
        self.decklist.configure(highlightbackground="#d9d9d9")
        self.decklist.configure(highlightcolor="black")
        self.decklist.configure(insertbackground="black")
        self.decklist.configure(selectbackground="#c4c4c4")
        self.decklist.configure(selectforeground="black")
        self.decklist.configure(width=264)
        self.decklist.configure(wrap=WORD)

        self.okay = Button(top, command = self.dummpy)
        self.okay.place(relx=0.73, rely=0.8, height=24, width=38)
        self.okay.configure(activebackground="#d9d9d9")
        self.okay.configure(activeforeground="#000000")
        self.okay.configure(background="#d9d9d9")
        self.okay.configure(disabledforeground="#a3a3a3")
        self.okay.configure(foreground="#000000")
        self.okay.configure(highlightbackground="#d9d9d9")
        self.okay.configure(highlightcolor="black")
        self.okay.configure(pady="0")
        self.okay.configure(text='''Okay''')

        self.Title = Text(top)
        self.Title.place(relx=0.06, rely=0.13, relheight=0.08, relwidth=0.84)
        self.Title.configure(background="white")
        self.Title.configure(font="TkTextFont")
        self.Title.configure(foreground="black")
        self.Title.configure(highlightbackground="#d9d9d9")
        self.Title.configure(highlightcolor="black")
        self.Title.configure(insertbackground="black")
        self.Title.configure(selectbackground="#c4c4c4")
        self.Title.configure(selectforeground="black")
        self.Title.configure(width=264)
        self.Title.configure(wrap=WORD)

    def dummpy(self):
        decklist_raw = self.decklist.get("1.0", END)
        maindeck, sideboard = deckList.generate(decklist_raw)
        print(maindeck)
        print(sideboard)
        print("Downloading Images for Maindeck...")
        imageDownload.download_images_from_decklist(maindeck)
        print("Downloading Images for Sideboard...")
        imageDownload.download_images_from_decklist(sideboard)
        #imageDownload.test_print_cache()
        deckAssembly.createDeck(maindeck, sideboard, imageDownload.get_cache(), "testCode.json")
        print("deck assembly completed!")


if __name__ == '__main__':
    os.chdir("..")
    vp_start_gui()


