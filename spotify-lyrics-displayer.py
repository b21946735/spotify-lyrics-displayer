import tkinter, win32api, win32con, pywintypes
import ctypes
from selenium import webdriver
from selenium.webdriver.common.by import By


class UpdateLabel(tkinter.Label):
    def __init__(self, *args, **kwargs):
        tkinter.Label.__init__(self, *args, **kwargs)
        self._count = ""

    def update_text(self):
        
        self.config(text=str(self._count))
        try:
                current_text =  driver.find_element(By.CLASS_NAME,"TDPh45khCfG51fNwNIiw").text
                if(len(current_text) > 25):
                    lst = str(current_text[25:]).split(" ", 1)
                    current_text = current_text[:25]+"\n".join(lst)
                self._count = current_text
        except :
            pass
        self.after(100, self.update_text)

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:/Users/fredo/AppData/Local/Google/Chrome/User Data/Default") # CHANGE WITH YOUR GOOGLE CHROME PROFILE PATH
driver = webdriver.Chrome(executable_path=r"C:/Users/fredo/Downloads/chromedriver_win32/chromedriver.exe", chrome_options=options) # CHANGE WITH YOUR CHROME DRIVER PATH
driver.get("https://open.spotify.com/lyrics")
text = ''

ctypes.windll.shcore.SetProcessDpiAwareness(1)
label = UpdateLabel(text='Text on the screen', font=('Arial','20'), fg='grey', bg='black')
label.master.overrideredirect(True)
label.master.geometry("+1400+200")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparent", 'white')
label.master.wm_attributes("-transparentcolor", 'black')

hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

label.pack_propagate(False)
label.pack()
label.update_text()
label.mainloop()