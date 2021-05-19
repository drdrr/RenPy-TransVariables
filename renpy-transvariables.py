import re
import os

def allmode():
    filelist = os.listdir()
    for eachfile in filelist:
        if eachfile.endswith('.rpy'):
            cookedfile = open('.\\new\\'+eachfile, 'w', encoding='utf-8')
            variables = []

            for line in open(eachfile, 'r', encoding='utf-8'):
                qlist = re.findall(r'"(.*?)(?<![^\\\\]\\\\)"', line)
                if qlist != []:
                    for each in qlist:
                        vlist = re.findall(r'\[(.*?)\]', each)
                        if vlist != []:
                            for j in vlist:
                                if not j.endswith('!t'):
                                    variables.append(j)
                                    line = line.replace('['+j+']' , '['+j+'!t]')
                cookedfile.write(line)
                cookedfile.flush()

            if variables != []:
                print('{}处理完成，最后识别出的需要修改的变量有：'.format(eachfile))
                print('\n'.join(set(variables)))
            else:
                print('{}未识别出需要修改的变量'.format(eachfile))
            print('\n\n')

def blackmode():

    bl = set()
    for line in open('blacklist.txt', 'r', encoding='UTF-8'):
        eachvar = line.strip('\n').strip()
        if not (eachvar.startswith('#') or eachvar == ''):
            bl.add(eachvar)
    bl = list(bl)

    filelist = os.listdir()
    for eachfile in filelist:
        if eachfile.endswith('.rpy'):
            cookedfile = open('.\\new\\'+eachfile, 'w', encoding='utf-8')
            variables = []

            for line in open(eachfile, 'r', encoding='utf-8'):
                qlist = re.findall(r'"(.*?)(?<![^\\\\]\\\\)"', line)
                if qlist != []:
                    for each in qlist:
                        vlist = re.findall(r'\[(.*?)\]', each)
                        if vlist != []:
                            for j in vlist:
                                if not (j.endswith('!t') or j in bl):
                                    variables.append(j)
                                    line = line.replace('['+j+']' , '['+j+'!t]')
                cookedfile.write(line)
                cookedfile.flush()

            if variables != []:
                print('{}处理完成，最后识别出的需要修改的变量有：'.format(eachfile))
                print('\n'.join(set(variables)))
            else:
                print('{}未识别出需要修改的变量'.format(eachfile))
            print('\n\n')

def whitemode():
    wl = set()
    for line in open('whitelist.txt', 'r', encoding='UTF-8'):
        eachvar = line.strip('\n').strip()
        if not (eachvar.startswith('#') or eachvar == ''):
            wl.add(eachvar)
    wl = list(wl)

    filelist = os.listdir()
    for eachfile in filelist:
        if eachfile.endswith('.rpy'):
            cookedfile = open('.\\new\\'+eachfile, 'w', encoding='utf-8')
            variables = []

            for line in open(eachfile, 'r', encoding='utf-8'):
                qlist = re.findall(r'"(.*?)(?<![^\\\\]\\\\)"', line)
                if qlist != []:
                    for each in qlist:
                        vlist = re.findall(r'\[(.*?)\]', each)
                        if vlist != []:
                            for j in vlist:
                                if j in wl and not j.endswith('!t'):
                                    variables.append(j)
                                    line = line.replace('['+j+']' , '['+j+'!t]')
                cookedfile.write(line)
                cookedfile.flush()

            if variables != []:
                print('{}处理完成，最后识别出的需要修改的变量有：'.format(eachfile))
                print('\n'.join(set(variables)))
            else:
                print('{}未识别出需要修改的变量'.format(eachfile))
            print('\n\n')

def scanmode():
    filelist = os.listdir()
    for eachfile in filelist:
        if eachfile.endswith('.rpy'):
            variables = []

            for line in open(eachfile, 'r', encoding='utf-8'):
                qlist = re.findall(r'"(.*?)(?<![^\\\\]\\\\)"', line)
                if qlist != []:
                    for each in qlist:
                        vlist = re.findall(r'\[(.*?)\]', each)
                        if vlist != []:
                            for j in vlist:
                                if not j.endswith('!t'):
                                    variables.append(j)

            if variables != []:
                print('{}识别出的变量有：'.format(eachfile))
                print('\n'.join(set(variables)))
            else:
                print('{}未识别出变量'.format(eachfile))
            print('\n\n')



try:
    os.mkdir('new')
except FileExistsError:
    pass

if not os.path.isfile("blacklist.txt"):
    with open('blacklist.txt', 'w', encoding='UTF-8') as bfile:
        bfile.write('# 黑名单模式：将不需要转换的变量放在下面，一个变量一行，不需要方括号\n# 带有井号的行是注释，会被自动忽略\n')
if not os.path.isfile("whitelist.txt"):
    with open('whitelist.txt', 'w', encoding='UTF-8') as wfile:  
        wfile.write('# 白名单模式：将需要转换的变量放在下面，一个变量一行，不需要方括号\n# 带有井号的行是注释，会被自动忽略\n')

print('RenPy多语言变量处理工具')
print("By Koshiro, version 1.0")
print("使用前请将所有.rpy文件放在本目录，新的文件会存放在/new文件夹中\n\n")

print("选择模式：\n1 全模式：转换所有变量（默认）\n2 白名单模式：只转换whitelist.txt中的变量\n3 黑名单模式：只不转换blacklist.txt中的变量\n4 仅读取所有变量名，不转换")
mode = input('\n（1/2/3/4？）> ').strip()

if mode == '2':
    whitemode()
elif mode == '3':
    blackmode()
elif mode == '4':
    scanmode()
else:
    allmode()

input('按回车键退出')