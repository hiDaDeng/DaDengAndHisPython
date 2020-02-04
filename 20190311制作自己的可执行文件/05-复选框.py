import PySimpleGUI as sg

layout = [ [sg.Text('你的爱好', auto_size_text=True)],
           [sg.Checkbox('游泳', default=True),
            sg.Checkbox('篮球'),
            sg.Checkbox('足球'),
            sg.Checkbox('羽毛球')],  #h或者v表示水平或者垂直
           [sg.OK('确认', auto_size_button=True)] ]

with sg.FlexForm('复选框',auto_size_text=True) as form:
    button_name, choices = form.Layout(layout).Read()
    sg.Popup(button_name, choices)
    
