'''
Created on 2019年4月5日

@author: bkd
'''
import platform
from os import environ
from os.path import join,dirname,realpath
from tkinter import Tk,Button,ttk
from tkinter import messagebox as msg
from tkinter.constants import W,E
try:
    from os import startfile
except Exception as e:
    pass

cur_dir = dirname(realpath(__file__))
#     下载64位的安装包
def down64_installer():
    startfile("https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe")

#     下载32位的安装包
def down32_installer():
    startfile("https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe")

#     安装pip
def install_pip():
    script_path = get_file_realpath("get-pip.py") 
    startfile("python " + script_path)
    msg.showerror("安装pip", "安装pip成功")
def get_file_realpath(file):
    return join(cur_dir,file)

# 安装软件
def install_package(package_name):
    if package_name :
        startfile("pip install " + package_name)
    else :
        msg.showerror("安装软件", "请输入软件名")
        
# 卸载软件        
def uninstall_package(package_name):
    if package_name :
        startfile("pip uninstall " + package_name)
    else :
        msg.showerror("卸载软件", "请输入软件名")
    
def get_sysinfo():
    sysinfo = {}
    sysinfo["PYTHONPATH"] = environ["PYTHONPATH"]
    sysinfo["HOME"] = environ["HOME"]
    sysinfo["USER"] = environ["USER"]
    sysinfo["PATH"] = environ["PATH"]
    return sysinfo
    
print(environ)

if __name__ == '__main__':
    root = Tk()
    system_label1 = ttk.Label(root, text="系统类型：").grid(row=0, column=0)
    system_label2 = ttk.Label(root, text=platform.system()).grid(row=0, column=1)
    Button(root, text='1.安装64位python',command=down64_installer).grid(row=1, column=0, sticky=W)
    Button(root, text='1.安装32位python',command=down32_installer).grid(row=2, column=0, sticky=W)
    Button(root, text='2.安装pip',command=install_pip).grid(row=3, column=0, sticky=W,ipadx=27)
    package_entry = ttk.Entry(root, font=(None, 16))
    package_entry.grid(row=1, column=1, sticky=W)
    Button(root, text='3.安装软件',command=lambda :install_package(package_entry.get())).grid(row=2, column=1, sticky=E,ipadx=78)
    Button(root, text='4.卸载软件',command=lambda :uninstall_package(package_entry.get())).grid(row=3, column=1, sticky=E,ipadx=78)
    root.mainloop()