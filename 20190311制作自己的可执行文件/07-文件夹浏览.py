import PySimpleGUI as sg

layout = [[sg.Text('选择需要选择的文件夹')],
          [sg.Input(key='input')],
          #target表示broswer这个按钮的上一行，第一列
          [sg.FolderBrowse(target='input'), sg.OK()]]

with sg.FlexForm('文件夹浏览', auto_size_text=True) as form:
    event, dirinfo = form.Layout(layout).Read()
    sg.Popup(event, dirinfo['input'])


    
