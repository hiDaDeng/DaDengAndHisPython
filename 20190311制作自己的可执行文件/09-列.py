import PySimpleGUI as sg

# Column layout
col = [[sg.Text('col Row 1')],
       [sg.Text('col Row 2'), sg.Input('col input 1')],
       [sg.Text('col Row 3'), sg.Input('col input 2')],
       [sg.Text('col Row 4'), sg.Input('col input 3')],
       [sg.Text('col Row 5'), sg.Input('col input 4')],
       [sg.Text('col Row 6'), sg.Input('col input 5')],
       [sg.Text('col Row 7'), sg.Input('col input 6')]]

layout = [[sg.Slider(range=(1,100), default_value=10, orientation='v'), sg.Column(col)],
          [sg.Input('Last input')],
          [sg.OK()]]


event, values = sg.FlexForm('Compact 1-line window with column').Layout(layout).Read()

sg.Popup(event, values, line_width=200)

    
