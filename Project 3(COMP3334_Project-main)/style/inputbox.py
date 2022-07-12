import tkinter as tk

from style.params import main_fg_color, inputReplaceEntryColor

###
# Source:https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tk
###

# Modified by us
# ... with ability to convert input to * in password row
# ... reset function for remove all the input

class InputBoxWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color=inputReplaceEntryColor, input_value_with_star=False):
        super().__init__(master)
        self.master = master # save the master
        self.placeholder = placeholder # save the default text
        self.placeholder_color = color # save the normal colour
        self.default_fg_color = self["fg"]
        self["bg"] = main_fg_color
        self.inputValueWithStar = input_value_with_star # boolean for show * or show normal

        self.bind("<FocusIn>", self.foc_in) # with user click the input bar
        self.bind("<FocusOut>", self.foc_out) # when user leave the input bar

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder) # input the word
        self["fg"] = self.placeholder_color # change the colour

    def foc_in(self, *args):
        if self["fg"] == self.placeholder_color: # remove all the word if it is empty
            self.delete("0", "end")
            self["fg"] = self.default_fg_color
        if self.inputValueWithStar: # change the input with star if boolean is true
            self["show"] = "*"

    def reset(self, *args):
        self.delete("0", "end") # remove all the word
        self.foc_out(self, args)
        self.master.focus() # remove the cursor from the input bar

    def foc_out(self, *args):
        if not self.get(): # if user does not input any thing 
            self.put_placeholder() # show back original word with default colour
            if self.inputValueWithStar: # show the word is boolean tru
                self["show"] = ""
