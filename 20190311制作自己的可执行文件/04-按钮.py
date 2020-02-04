import PySimpleGUI as sg

layout = [ [sg.Text('你的学历是', auto_size_text=True)],
           [sg.Radio('高中', group_id=1),
            sg.Radio('本科', group_id=1),
            sg.Radio('硕士', group_id=1),
            sg.Radio('博士', group_id=1)],  #h或者v表示水平或者垂直
           [sg.OK('确认', auto_size_button=True)] ]

with sg.FlexForm('按钮',auto_size_text=True) as form:
    button_name, level = form.Layout(layout).Read()
    sg.Popup(button_name, level)
    
