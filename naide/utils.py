from tkinter import messagebox
def popup(*args, **qwargs):
  try:
    messagebox.showinfo(*args, **qwargs)
  except Exception as e:
    try:
      messagebox.showinfo("ERROR CATCHED", f"Error : {e}\nArgs : {args}\nQwargs : {qwargs}")
    except Exception as e2:
      print(f"ERROR CATCHED\nError : {e2}\nOriginal Error : {e}\nArgs : {args}\nQwargs : {qwargs}")
