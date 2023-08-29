from .menubar import Save, selectall, autosaveevent
def process_window(window, txt):
  window.bind('<Control-s>', Save)
  window.bind('<Control-a>', selectall)
  txt.bind('<Key>', autosaveevent)
  return window, txt
