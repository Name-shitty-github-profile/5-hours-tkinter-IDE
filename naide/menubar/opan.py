from .data import stpath, gttxt, gtpath
def Open():
  path = stpath(filedialog.askopenfilename())
  textEditor = gttxt()
  try:
    f = open(path, 'r')
  except:
    popup("Error", f"No such file as {path}")
    return None
  textEditor.delete('1.0', END)
  textEditor.insert('1.0', f.read())

def ReOpen():
  path = gtpath()
  if path is None:
    Open()
    return None
  try:
    f = open(path, 'r')
  except:
    Open()
    return None
  textEditor.delete('1.0', END)
  textEditor.insert('1.0', f.read())
