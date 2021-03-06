import PySimpleGUI as sg
import xlrd
import os
import json


def xmlFormater(pathRaw, sheetIndex=0):
    arr = []
    arr1 = []
    workbook = xlrd.open_workbook(pathRaw)
    sheet = workbook.sheet_by_index(sheetIndex)
    for i in range(sheet.nrows):
        arr0 = sheet.row_values(i)
        a = '\t\t\t\t<key ID="' + str(int(arr0[1])) + '"\tname="' + str(
            arr0[2]) + '"\tSort="100" free="1" />\n'
        arr0[1] = str(int(arr0[1]))
        arr1.append(arr0)
        arr.append(a)
    return arr, arr1


def writeFile(path2Store, arr, gameName):
    xmlHeader = """<?xml version="1.0" encoding="gb2312" ?>\n\t<Tourney>\n\t<!--比赛归类配置-->\n\t\t<MatchGroup>\n\t\t\t<label\tname=""\tFlag="1">\n\t\t\t</label>\n"""
    xmlFooter = """\t\t</MatchGroup>\n\t</Tourney>"""
    arrHeader = '\t\t\t<label\tname="' + gameName + '"\tFlag="1">\n'
    arrFooter = '\t\t\t</label>\n'
    os.chdir(path2Store)
    if not (os.path.exists(path2Store + '\\' + gameType[gameName])):
        os.mkdir(gameType[gameName])
    path0 = os.getcwd()
    path = os.path.join(path0, gameType[gameName])
    os.chdir(path)
    ff = open("config.ini", 'w+')
    ff.write('[attribute]\n')
    ff.write('name=' + gameName)
    ff.close()
    f = open("Layout.xml", 'w+')
    arr.append(arrFooter)
    arr.append(xmlFooter)
    arr.insert(0, arrHeader)
    arr.insert(0, xmlHeader)
    f.writelines(''.join(arr))
    f.close()


def write181(pathRaw, path2Store):
    text1 = xmlFormater(pathRaw, 1)
    text11 = ''.join(text1[0])
    text2 = xmlFormater(pathRaw, 0)
    text22 = ''.join(text2[0])
    os.chdir(path2Store)
    if not (os.path.exists(path2Store + "\\181")):
        os.mkdir("181")
    os.chdir(path2Store + "\\181")
    f1 = open("config.ini", 'w+')
    f1.write('[attribute]\n')
    f1.write('name=随来随打，今日大赛')
    f1.close()
    f2 = open("Layout.xml", 'w+')
    f2.writelines(
        '''<?xml version="1.0" encoding="gb2312" ?>\n<Tourney>\n\t<!--比赛归类配置-->\n\t<MatchGroup>\n\t\t<label name="" Flag="1">\n\t\t</label>\n\t\t<label name="广告" Flag="1" ad="1">\n\t\t</label>\n\t\t        <label name="今日大赛" tnycolor="" Flag="0" id="8001" SortGroup="2">\n'''
    )
    f2.writelines(text11)
    f2.writelines(
        '''\t\t</label>\n\t\t<label name="随来随打" tnycolor="" Flag="0" id = "8002" SortGroup="1">\n'''
    )
    f2.writelines(text22)
    f2.writelines(
        '''\t\t</label>\n\t</MatchGroup>\n\t<LabelSortGroup name = "随来随打（30分钟内开始）" ShowTime = "" ShowMinutes = "30"   Position = "0" Flag = "1" id="1" />\n\t<LabelSortGroup name = "今日大赛" ShowTime = "23:59" ShowHour = "23"  Position = "1" Flag = "1" id="2" />\n</Tourney>'''
    )
    f2.close()


layout = [[sg.Text('Filename', size=(12, 1)),
           sg.Input(),
           sg.FileBrowse()],
          [sg.Text('Foldername', size=(12, 1)),
           sg.Input(),
           sg.FolderBrowse()], [sg.Submit()]]
window = sg.Window('Layout Transformer').Layout(layout)
while True:
    button, values = window.Read()
    if (values[0] == ''):
        sg.Popup("error!", "please just choose a path")
        window = sg.Window('Layout Transformer').Layout(layout)
        continue
    # 获取根目录
    path00 = os.getcwd()
    # 读取json存储的布局id与比赛类型对应表
    try:
        jFlie = open(path00 + '\\config.json', encoding='utf-8')
    except IOError:
        sg.Popup("error!","please move config.json into root-dir")
        break
    res = jFlie.read()
    jFlie.close()
    gameType = json.loads(res)
    # 比赛列表路径
    pathRaw = values[0]
    # 布局文件存储路径
    path2Store = values[1]
    if (path2Store == ''):
        path2Store = path00
    if (button == 'Submit'):
        index = 0
        left = 0
        text, content = xmlFormater(pathRaw)
        right = len(content)
        gameName = content[0][0]
        for i in range(left, right):
            if content[i][0] != gameName:
                index = i
                arr2add = text[left:index]
                writeFile(path2Store, arr2add, gameName)
                left = i
                gameName = content[i][0]
                next
            arr2add = text[left:]
            writeFile(path2Store, arr2add, gameName)
            write181(pathRaw, path2Store)
        sg.PopupOK('layouts done!')
    break
