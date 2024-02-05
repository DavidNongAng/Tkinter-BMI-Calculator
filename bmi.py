import customtkinter as ctk
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class App(ctk.CTk):
    # Constructor
    def __init__(self):
        
        # Window Setup
        super().__init__(fg_color = BLUE)
        self.title('')
        self.iconbitmap('hidden.ico')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()
        
        # Layout
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
        
        # Widgets
        ResultText(self)
        
        self.mainloop()
    
    # This method changes the color of the title bar.
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except: 
            pass

class ResultText(ctk.CTkLabel):
    # Constructor
    def __init__(self, parent):
        
        super().__init__(master = parent, text = 22.5)
        self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nsew')

# If we have multiple files, this will be useful
if __name__ == '__main__':
    App()
        
