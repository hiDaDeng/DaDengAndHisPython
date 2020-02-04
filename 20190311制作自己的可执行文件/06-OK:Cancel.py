import PySimpleGUI as sg

layout = [ [sg.OK(), sg.Cancel()] ]

with sg.FlexForm('OK_Cancel', auto_size_text=True) as form:
    ok_cancel = form.Layout(layout).Read()
    print(ok_cancel)

    
