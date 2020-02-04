import PySimpleGUI as sg

layout = [[sg.Text('选择需要选择的文件')],
          [sg.Input(key='input')],
          #target表示broswer这个按钮的上一行，第一列
          [sg.FilesBrowse(target='input'), sg.OK()]]

with sg.FlexForm('文件浏览', auto_size_text=True) as form:
    event, fileinfo = form.Layout(layout).Read()
    sg.Popup(event, fileinfo['input'])

    
