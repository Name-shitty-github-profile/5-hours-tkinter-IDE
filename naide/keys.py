from ..menubar import Save, selectall, autosaveevent
def process_window(window, txt):
  for k, v in ({"<Control-s>": Save, "<Control-a>": selectall):
    window.bind(k, v)
  txt.bind('<Key>', autosaveevent)
  return window, txt
