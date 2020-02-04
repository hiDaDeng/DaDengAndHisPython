import PySimpleGUI as sg


layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]


form = sg.FlexForm('Custom Progress Meter').Layout(layout)
progress_bar = form.FindElement('progressbar')
for i in range(100):
    event, values = form.Read(timeout=0)
    if event == 'Cancel'  or event is None:
        break
    progress_bar.UpdateBar(i + 1)

form.Close()

    
