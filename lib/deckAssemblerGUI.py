#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 25, 2018 04:22:17 PM

import os

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

from lib import MTG_TS_DA_1_support, imageDownload, deckAssembly, deckList, configurations as conf, util

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = MTG_TS_Deck_Assembler (root)
    MTG_TS_DA_1_support.init(root, top)
    root.mainloop()

w = None
def create_MTG_TS_Deck_Assembler(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = MTG_TS_Deck_Assembler (w)
    MTG_TS_DA_1_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_MTG_TS_Deck_Assembler():
    global w
    w.destroy()
    w = None


class MTG_TS_Deck_Assembler:

    def init_gui(self, top):
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("406x547+728+178")
        top.title("MTG TS Deck Assembler")
        top.configure(background="#d9d9d9")

        self.filename_text = Text(top)
        self.filename_text.place(relx=0.05, rely=0.07, relheight=0.04
                                 , relwidth=0.87)
        self.filename_text.configure(background="white")
        self.filename_text.configure(font="TkTextFont")
        self.filename_text.configure(foreground="black")
        self.filename_text.configure(highlightbackground="#d9d9d9")
        self.filename_text.configure(highlightcolor="black")
        self.filename_text.configure(insertbackground="black")
        self.filename_text.configure(selectbackground="#c4c4c4")
        self.filename_text.configure(selectforeground="black")
        self.filename_text.configure(width=354)
        self.filename_text.configure(wrap=WORD)

        self.output_folder_text = Text(top)
        self.output_folder_text.place(relx=0.05, rely=0.18, relheight=0.12
                                      , relwidth=0.87)
        self.output_folder_text.configure(background="white")
        self.output_folder_text.configure(font="TkTextFont")
        self.output_folder_text.configure(foreground="black")
        self.output_folder_text.configure(highlightbackground="#d9d9d9")
        self.output_folder_text.configure(highlightcolor="black")
        self.output_folder_text.configure(insertbackground="black")
        self.output_folder_text.configure(selectbackground="#c4c4c4")
        self.output_folder_text.configure(selectforeground="black")
        self.output_folder_text.configure(width=354)

        self.deck_input_text = Text(top)
        self.deck_input_text.place(relx=0.05, rely=0.37, relheight=0.46
                                   , relwidth=0.87)
        self.deck_input_text.configure(background="white")
        self.deck_input_text.configure(font="TkTextFont")
        self.deck_input_text.configure(foreground="black")
        self.deck_input_text.configure(highlightbackground="#d9d9d9")
        self.deck_input_text.configure(highlightcolor="black")
        self.deck_input_text.configure(insertbackground="black")
        self.deck_input_text.configure(selectbackground="#c4c4c4")
        self.deck_input_text.configure(selectforeground="black")
        self.deck_input_text.configure(width=354)
        self.deck_input_text.configure(wrap=WORD)

        self.filename_label = Label(top)
        self.filename_label.place(relx=0.02, rely=0.02, height=21, width=88)
        self.filename_label.configure(background="#d9d9d9")
        self.filename_label.configure(disabledforeground="#a3a3a3")
        self.filename_label.configure(foreground="#000000")
        self.filename_label.configure(text='''Deck File Name''')

        self.output_folder_label = Label(top)
        self.output_folder_label.place(relx=0.02, rely=0.13, height=21
                                       , width=105)
        self.output_folder_label.configure(background="#d9d9d9")
        self.output_folder_label.configure(disabledforeground="#a3a3a3")
        self.output_folder_label.configure(foreground="#000000")
        self.output_folder_label.configure(text='''Deck Output Folder''')

        self.deck_input_label = Label(top)
        self.deck_input_label.place(relx=0.02, rely=0.31, height=21, width=89)
        self.deck_input_label.configure(background="#d9d9d9")
        self.deck_input_label.configure(disabledforeground="#a3a3a3")
        self.deck_input_label.configure(foreground="#000000")
        self.deck_input_label.configure(text='''Deck Bulk Input''')

        self.defult_loc_button = Button(top, command=self.set_default_location)
        self.defult_loc_button.place(relx=0.62, rely=0.13, height=24, width=128)
        self.defult_loc_button.configure(activebackground="#d9d9d9")
        self.defult_loc_button.configure(activeforeground="#000000")
        self.defult_loc_button.configure(background="#d9d9d9")
        self.defult_loc_button.configure(disabledforeground="#a3a3a3")
        self.defult_loc_button.configure(foreground="#000000")
        self.defult_loc_button.configure(highlightbackground="#d9d9d9")
        self.defult_loc_button.configure(highlightcolor="black")
        self.defult_loc_button.configure(pady="0")
        self.defult_loc_button.configure(text='''Default Folder Location''')

        self.create_button = Button(top, command=self.generate_deck)
        self.create_button.place(relx=0.52, rely=0.86, height=24, width=164)
        self.create_button.configure(activebackground="#d9d9d9")
        self.create_button.configure(activeforeground="#000000")
        self.create_button.configure(background="#d9d9d9")
        self.create_button.configure(disabledforeground="#a3a3a3")
        self.create_button.configure(foreground="#000000")
        self.create_button.configure(highlightbackground="#d9d9d9")
        self.create_button.configure(highlightcolor="black")
        self.create_button.configure(pady="0")
        self.create_button.configure(text='''Create Deck Using Bulk Input''')

        self.update_label = Label(top)
        self.update_label.place(relx=0.05, rely=0.93, height=21, width=354)
        self.update_label.configure(background="#d9d9d9")
        self.update_label.configure(disabledforeground="#a3a3a3")
        self.update_label.configure(foreground="#000000")
        self.update_label.configure(width=354)

    def __init__(self, top=None):
        os.chdir("..")
        self.init_gui(top)
        self.modify_gui()

    def modify_gui(self):
        if os.path.exists(conf.savedFolderFile):
            with open(conf.savedFolderFile,"r") as f:
                self.output_folder_text.delete(1.0, END)
                self.output_folder_text.insert(END, f.read())
        else:
            self.set_default_location()

    def get_output_folder(self):
        return self.output_folder_text.get("1.0", END).strip()

    def get_location(self):
        filename = self.filename_text.get("1.0", END).strip()
        if ".json" not in filename:
            filename = filename + ".json"
        location = os.path.join(self.get_output_folder(), filename)

        return location

    def save_output_folder(self):
        save_folder = self.output_folder_text.get("1.0", END).strip()
        with open(conf.savedFolderFile, "w") as f:
            f.write(save_folder)

    # BUTTON COMMANDS
    def set_default_location(self):
        # inst the output_folder_text
        folders = "Documents/My Games/Tabletop Simulator/Saves/Saved Objects/".split("/")
        default_location = os.path.expanduser("~")
        # default_location = ""

        for folder in folders:
            default_location = os.path.join(default_location, folder)

        self.output_folder_text.delete(1.0, END)
        self.output_folder_text.insert(END, default_location)

    def generate_deck(self):
        self.update_label.config(text="")
        Tk.update(self.update_label)
        decklist_raw = self.deck_input_text.get("1.0", END)
        maindeck, sideboard = deckList.generate(decklist_raw)
        print(maindeck)
        print(sideboard)
        self.update_label.config(text="Finding Images for Maindeck...")
        Tk.update(self.update_label)
        imageDownload.download_images_from_decklist(maindeck)
        self.update_label.config(text="Finding Images for Sideboard...")
        Tk.update(self.update_label)
        imageDownload.download_images_from_decklist(sideboard)
        # imageDownload.test_print_cache()

        # assemble the deck file in the given location
        util.generateDirectories(self.get_output_folder())
        deckAssembly.createDeck(maindeck, sideboard, imageDownload.get_cache(), self.get_location())
        self.update_label.config(text="deck assembly completed!")
        Tk.update(self.update_label)

        self.deck_input_text.delete("1.0", END)

        # save the output folder for next run of the program
        self.save_output_folder()



if __name__ == '__main__':
    vp_start_gui()


