path = None
TextEditor = None
autosave: bool = False

def stpath(New):
  global path
  if New is None:
    return
  path = New
  return path

def gtpath():
  return path

def sttxt(New) -> None:
  global TextEditor
  TextEditor = New
  return TextEditor

def gttxt():
  return TextEditor

def stautosave():
  global autosave
  autosave = autosave is False
  return autosave
    
def gtautosave():
  return autosave
