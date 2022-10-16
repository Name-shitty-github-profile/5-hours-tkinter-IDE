from tkinter import Tk, Text
from .menubar import menubr
from .keys import process_window
def run():
  window = Tk()
  window.title("Naide")
  textEditor = Text()
  textEditor.pack()
  window, textEditor = process_window(window, textEditor)
  window.config(menu = menubr(window, textEditor))
  window.mainloop()
