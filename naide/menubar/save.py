from tkinter import filedialog, END
from .data import gtpath, stpath, gttxt, gtautosave, stautosave
def SaveAs():
  path = stpath(filedialog.asksaveasfilename())
  with open(path, 'w') as f:
    f.write(gttxt().get('1.0', END))

def Save(*args):
  path = gtpath()
  if path is None:
    SaveAs()
    return None
  with open(path, 'w') as f:
    f.write(gttxt().get('1.0', END))

def AutoSave():
  if stautosave() is False:
    Save()

def autosaveevent(*args):
  if gtautosave() is True:
    Save()
