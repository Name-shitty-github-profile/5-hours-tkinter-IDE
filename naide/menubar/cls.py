from tkinter import Menu, END, messagebox, filedialog, SEL, INSERT
from ..utils import popup
from .data import gtpath, stpath, gttxt, sttxt, gtautosave
from .save import Save, SaveAs, AutoSave
from .opan import Open, ReOpen
def menubr(window, txt):
  sttxt(txt)
  menuBar = Menu(window)
  NewBar = Menu(menuBar, tearoff = 0)
  for k, v in ({"Open": Open, "Reopen": ReOpen, "Save": Save, "Save as": SaveAs, "AutoSave": AutoSave}).items():
    NewBar.add_command(label=k, command=v)
  menuBar.add_cascade(label='File', menu = NewBar)
  del NewBar
  NewBar = Menu(menuBar, tearoff = 0)
  NewBar.add_command(label="Select all", command = selectall)
  menuBar.add_cascade(label='Utils', menu = NewBar)
  del NewBar
  NewBar = Menu(menuBar, tearoff = 0)
  NewBar.add_command(label="Path", command = Path)
  menuBar.add_cascade(label='IDE vars', menu = NewBar)
  del NewBar
  return menuBar

def Path():
  path = gtpath()
  popup("Path", 'Path variable was not initialized' if path is None else f'The current path variable is {str(path)}')

def selectall(*args):
  textEditor = gttxt()
  textEditor.tag_add(SEL, "1.0", END)
  textEditor.mark_set(INSERT, "1.0")
  textEditor.see(INSERT)
