import tkinter as tk

from style.params import main_color, main_fg_color, checkbutton_fg_colour, checkbutton_on_value, checkbutton_off_value


# tk.Button with our basic settings
class DefaultButton(tk.Button): # tk button with default setting
    defaults = dict(background=main_color,
                    activebackground=main_color,
                    foreground=main_fg_color,
                    activeforeground=main_fg_color)
# call the super from tk.Button
    def __init__(self, master=None, button_text=None, **kwargs):
        kwargs = dict(self.defaults, **kwargs)
        super().__init__(master, **kwargs)

        self["text"] = button_text


class DefaultCheckbutton(tk.Checkbutton):
    defaults = dict(selectcolor=main_color,# tk check button with default setting
                    onvalue=checkbutton_on_value,
                    offvalue=checkbutton_off_value,
                    background=main_color,
                    activebackground=main_color,
                    foreground=checkbutton_fg_colour,
                    activeforeground=checkbutton_fg_colour)
# call the super from tk.Checkbutton
    def __init__(self, master=None, checkbutton_text=None, **kwargs):
        kwargs = dict(self.defaults, **kwargs)
        super().__init__(master, **kwargs)

        self["text"] = checkbutton_text
