import PySimpleGUI as sg

layout = [ [sg.Text('选择一个你喜欢的程度', auto_size_text=True)],
           [sg.Slider(range=(1, 500),default_value=200, orientation='h')],  #h或者v表示水平或者垂直
           [sg.OK('确认', auto_size_button=True)] ]

with sg.FlexForm('滑动条',auto_size_text=True) as form:
    button_name, (likelevel,) = form.Layout(layout).Read()
    sg.Popup(button_name, likelevel)
    
