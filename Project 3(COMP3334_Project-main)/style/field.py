import tkinter as tk

from style.params import main_color, main_fg_color, main_text_font


# tk.Label with our basic settings
class DefaultTextField(tk.Label):
    defaults = dict(background=main_color,# tk label with default setting
                    foreground=main_fg_color,
                    font=main_text_font)
# call the super from tk.Label
    def __init__(self, master=None, field_text=None, **kwargs):
        kwargs = dict(self.defaults, **kwargs)
        super().__init__(master, **kwargs)

        self["text"] = field_text
