import PySimpleGUI as sg

layout = [ [sg.Text('选择你的性别', auto_size_text=True)],
           [sg.InputCombo(['男', '女', '隐私'], auto_size_text=True)],
           [sg.OK('确认', auto_size_button=True)] ]

with sg.FlexForm('信息录入',auto_size_text=True) as form:
    button_name, (gender,) = form.Layout(layout).Read()
    sg.Popup(button_name, gender)
    
