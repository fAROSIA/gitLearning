def get181(idToAdd, fileNameToSave):
    import os

    # 创建布局文件
    os.chdir('d:\\test\\c5')
    i = 0
    # 读取数据
    name = [[], [], []]
    index = [0]
    flag = []
    j = 0
    with open('d:\\test\\c5\\' + idToAdd) as f:
        for line in f:
            for each in enumerate(line.split('\t')):
                name[each[0]].append(each[1])
                if each[1] == '\n':
                    z = int((j + 1) / 2)
                    index.append(z)
                j += 1
    IDs, Ns, Frees = name
    index.append(len(Ns) + 1)
    flag.append(len(Ns) + 1)
    for x in range(len(Ns)):
        str1 = Ns[x]
        Ns[x] = str1.replace("\n", " ")

    # 写入
    os.chdir("c:\\Users\\duandz\\Desktop\\Act\\test")
    f = open(fileNameToSave, 'w+')

    # part3

    for i in range(0, len(Ns)):
        if IDs[i] == "":
            f.write('\n===============================================')
            continue
        elif Frees[i] == '免费\n':
            f.write('\n\t<key ID="' + IDs[i] + '"    name="' + Ns[i] +
                    '"  Sort="100" free="1" /> ')
        else:
            f.write('\n\t<key ID="' + IDs[i] + '"    name="' + Ns[i] +
                    '"  Sort="100" free="0" /> ')
    f.write('\n')

    f.close()


def buildALot(idFile, lidFile, raw):
    import os
    os.chdir('d:\\test\\c5')
    f00 = open('d:\\test\\c5\\' + idFile)
    Game_name0 = f00.read()
    f00.close
    Game_name = Game_name0.split(",")

    # 读取layout ID
    layout0 = []
    f0 = open('d:\\test\\c5\\' + lidFile)
    layout0 = f0.read()
    f0.close
    lids = layout0.split(",")
    name = [[], [], []]
    j = 0
    index = []
    IDs = []
    Ns = []
    Fs = []
    with open('d:\\test\\c5\\' + raw) as f:
        for line in f:
            for each in enumerate(line.split('\t')):
                name[each[0]].append(each[1])
            if line == '\t\t\n':
                index.append(j)
                # name[0].append('Flamenco')
                # name[1].append('Flamenco')
                # name[2].append('Flamenco')
            j += 1

    index.append(j)
    IDs, Ns, Fs = name
    for x in range(len(Ns)):
        str1 = Ns[x]
        Ns[x] = str1.replace("\n", " ")
        str1 = Fs[x]
        Fs[x] = str1.replace("\n", " ")
    f.close

    # 写入
    y = 0
    h = 0
    k = 0
    index.insert(0, -1)
    for lid in lids:
        if IDs[k] == '':
            h += 1
            k += 1
        os.chdir("c:\\Users\\duandz\\Desktop\\Act\\test")
        os.mkdir(lid)
        path0 = os.getcwd()
        path = os.path.join(path0, lid)
        os.chdir(path)
        ff = open("config.ini", 'w+')
        ff.write('[attribute]\n')
        ff.write('name=' + Game_name[h])
        ff.close
        f = open("Layout.xml", 'w+')

        # part1
        f.write("""<?xml version="1.0" encoding="gb2312" ?>
    <Tourney>
    <!--比赛归类配置-->
        <MatchGroup>

            <label    name=""  Flag="1"  >


            </label>


        """)

        # part2
        f.write('\t<label    name="' + Game_name[h] + '"  Flag="1"  >\n')

        # part3

        for i in range(index[y] + 1, index[y + 1]):
            if Fs[i] == '免费 ':
                f.write('\n\t\t\t<key ID="' + IDs[i] + '"    name="' + Ns[i] +
                        '"  Sort="100" free="1" />')
            else:
                f.write('\n\t\t\t<key ID="' + IDs[i] + '"    name="' + Ns[i] +
                        '"  Sort="100" free="0" />')
            k = i + 1
        y += 1
        f.write('\n')

        # part4
        f.write("""
            </label>







        </MatchGroup>

    </Tourney>""")
        f.close()
        os.chdir(path0)
