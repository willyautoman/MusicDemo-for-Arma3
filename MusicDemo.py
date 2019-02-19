from tkinter import ttk
from tkinter import *
import os

root = Tk()
root.geometry('600x600')
root.iconbitmap('img/music.ico')
root.title('音乐包自助整合系统V1.0.0 ---designed by 半夏冰河')
label1 = Label(root, text='音乐包自助整合系统\n\n', font=('宋体', 16))
label1.pack()

Label(root, text='本软件由4th MISG战队-半夏冰河倾情推出', font=('宋体', 14)).pack()

Label(root, text='\n“懒惰是第一生产力”\n ', font=('宋体', 14)).pack()

Label(root, text='“软件制作不易，感谢您的赞助” ', font=('宋体', 14)).pack()

photo = PhotoImage(file="img/ZanZhu.gif", )
Label(root, image=photo, width=600, height=308).pack()

content = list()
author_name = "4th-半夏冰河"


def start():
    window = Toplevel(root)
    window.geometry('500x350')
    window.iconbitmap('img/music.ico')
    Label(window, text='输入作者姓名 \n\n', font=('宋体', 14)).pack()
    ent = Entry(window)
    ent.pack()

    def Ok():
        Label(window, text='添加完成\n\n', font=('宋体', 14)).pack()
        author_name = ent.get()
        fp1 = open("config.txt", 'w')
        fp2 = open("BIS_AddonInfo.txt", 'w')
        fp1.write('#include "BIS_AddonInfo.hpp"\nclass CfgPatches\n{\nclass 7_Music{\nunits[]= {};\nweapons[]={};'
                  '\nrequiredVersion=1.0;\nrequiredAddons[] = {};\nauthor[] = {"' + author_name
                  + '"};\n};\n};\nclass CfgMusicClasses {\n')
        fp1.close()
        fp2.close()

        def add_list():
            window1 = Toplevel(root)
            window.withdraw()
            window1.geometry('500x350')
            window1.iconbitmap('img/music.ico')
            frame_root = Frame(window1)
            frame1 = Frame(frame_root)
            Label(window1, text='\n添加目录 \n', font=('宋体', 14)).pack()
            Label(window1, text='添加目录可以将音乐分类存放，目录名称应为英语，\n否则游戏内会出现乱码。同时使用下划线代替空格可以'
                                '避免错误。\n此项必须填写，否则后续步骤无法检测到目录', bg='yellow', font=('宋体', 12)).pack()
            Label(frame1, text='目录名称：', font=('宋体', 12)).pack(side='left')
            ent2 = Entry(frame1)
            ent2.pack(side='left')
            frame1.pack()
            frame_root.pack()

            def add():
                list_name = ent2.get()
                content.append(list_name)
                fp1 = open("config.txt", 'a')
                fp1.write('\nclass ' + list_name + '\n{\ndisplayName = "' + list_name + '";\n};')
                fp1.close()
                T1.insert('insert', list_name + '   目录已添加\n')

            Button(window1, text='添加', command=add).pack()
            T1 = Text(window1, height=10)
            T1.pack()

            def add_music():
                fp1 = open("config.txt", 'a')
                fp1.write('\n};\nclass CfgMusic{\n\n')
                fp1.close()
                window2 = Toplevel(root)
                window1.withdraw()
                window2.geometry('500x350')
                window2.iconbitmap('img/music.ico')
                frame_root = Frame(window2)
                frame1 = Frame(frame_root)
                frame2 = Frame(frame_root)
                frame3 = Frame(frame_root)
                Label(window2, text='\n添加音乐 \n', font=('宋体', 14)).pack()
                Label(window2, text='音乐名称应为英语，\n否则游戏内会出现乱码。同时使用下划线代替空格可以'
                                    '避免错误', bg='yellow', font=('宋体', 12)).pack()
                Label(frame1, text='音乐名称：').pack(side='left')
                ent3 = Entry(frame1)
                ent3.pack(side='left')
                Label(frame2, text='音乐时长（秒）：').pack(side='left')
                ent4 = Entry(frame2)
                ent4.pack(side='left')
                Label(frame3, text='所属目录：').pack(side='left')
                content1 = tuple(content)
                cmb = ttk.Combobox(frame3)
                cmb['value'] = content1
                cmb.pack(side='left')
                frame1.pack()
                frame2.pack()
                frame3.pack()
                frame_root.pack()

                def add_mu():
                    music_name = ent3.get()
                    music_time = ent4.get()
                    music_content = cmb.get()
                    fp3 = open("config.txt", 'a')
                    fp3.write(
                        'class ' + music_name + '\n{\nname = "' + music_name + '";\n sound[] = {"\MusicPackage\''
                        + music_name + '.ogg",db+0,1.0};\nduration=' + music_time + ';\ntheme="safe";\nmusicClass = "'
                        + music_content + '";\n};\n')
                    T2.insert('insert', music_name + ' 已添加\n')

                Button(window2, text='添加', command=add_mu).pack()
                T2 = Text(window2, height=8)
                T2.pack()

                def format_doc():
                    window3 = Toplevel(root)
                    window2.withdraw()
                    window3.geometry('500x350')
                    window3.iconbitmap('img/music.ico')
                    Label(window3, text='\n格式化文件 \n', font=('宋体', 14)).pack()
                    Label(window3, text='只剩最后一步了！\n单击下面按钮，对文件格式化。', bg='yellow', font=('宋体', 12)).pack()

                    def format_docs():
                        fp1 = open("config.txt", 'a')
                        fp2 = open("BIS_AddonInfo.txt", 'a')
                        fp1.write('};')
                        fp2.write('class BIS_AddonInfo\n{\n	author="' + author_name + '";\n	timepacked="";\n};')
                        fp1.close()
                        fp2.close()
                        os.rename('config.txt', 'config.cpp')
                        os.rename('BIS_AddonInfo.txt', 'BIS_AddonInfo.hpp')
                        Label(window3, text='完成！\n请关闭本窗口以完成本次制作！\n谢谢您的使用！')

                    Button(window3, text='格式化文件', command=format_docs).pack()

                Button(window2, text='下一步', command=format_doc).pack()

            Button(window1, text='下一步', command=add_music).pack()

        Button(window, text='下一步', command=add_list).pack()

    Button(window, text='确定', command=Ok).pack()


BT1 = Button(root, text='开始制作', font=('宋体', 18), width=50, height=20, bg='yellow', command=start).pack()

root.mainloop()
