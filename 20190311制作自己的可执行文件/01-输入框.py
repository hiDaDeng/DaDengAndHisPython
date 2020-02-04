import PySimpleGUI as sg

layout = [[sg.Text('Enter a Number')],      
          [sg.Input()],      
          [sg.OK()] ]

event, (number,) = sg.Window('Enter a number example').Layout(layout).Read()

sg.Popup(event, number)
    
