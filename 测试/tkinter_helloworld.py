# -*- coding: utf-8 -*-
# @Time : 2019/4/1,001 9:50
# @Author : 徐缘
# @FileName: tkinter_helloworld.py
# @Software: PyCharm


from tkinter import *
from tkinter.filedialog import askdirectory


def run():
    print('run part 2')
    with open('GuGanDianXinLianTong_part2.py', 'r', encoding='UTF-8') as f:
        exec(f.read())
    return

# 创建Tk对象
root = Tk()

# 修改窗口标题
# root.title("Pack - Example")
root.wm_title("短彩系统局数据核查工具")

# 创建导航栏
menubar = Menu(root)

# 创建菜单项
fmenu1 = Menu(root)
for item in ['打开', '导出']:
    # 如果该菜单时顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。
    fmenu1.add_command(label=item)

fmenu2 = Menu(root)
for item in ['复制','粘贴','剪切']:
    fmenu2.add_command(label=item)

fmenu3 = Menu(root)
for item in ['默认视图', '新式视图']:
    fmenu3.add_command(label=item)

fmenu4 = Menu(root)
for item in ["版权信息", "其他说明"]:
    fmenu4.add_command(label=item)

menubar.add_cascade(label="文件", menu=fmenu1)
# menubar.add_cascade(label="编辑", menu=fmenu2)
# menubar.add_cascade(label="视图", menu=fmenu3)
menubar.add_cascade(label="关于", menu=fmenu4)

# 最后可以用窗口的 menu 属性指定我们使用哪一个作为它的顶层菜单
root['menu'] = menubar

# 界面标题
text = '短彩系统局数据核查工具'
# text = "This is Tcl/Tk version %s" % tk.TclVersion
# text += "\nThis should be a cedilla: \xe7"
label = Label(root, text=text, font=40)
label.pack()

# 文件路径
# 使用Frame增加一层容器
fm1 = Frame(root)
def selectPath():
    path_ = askdirectory()
    path.set(path_)

path = StringVar()
Entry(fm1, textvariable=path).pack(side=LEFT)
Button(fm1, text="打开", command=selectPath).pack(side=RIGHT)
fm1.pack(padx=10, pady=10)


# 按键
# 使用Frame增加一层容器
fm2 = Frame(root)
# test = Button(fm2, text="验证",
#               command=lambda root=root: root.test.configure(
#                   text="[%s]" % root.test['text']))

test = Button(fm2, text="验证",
              command=run())
test.pack(side=LEFT)
root.test = test

quit = Button(fm2, text="退出", command=root.destroy)
quit.pack(side=RIGHT)
fm2.pack(side=BOTTOM, padx=10, pady=30)
# The following three commands are needed so the window pops
# up on top on Windows...
root.iconify()
root.update()
root.deiconify()
root.mainloop()


