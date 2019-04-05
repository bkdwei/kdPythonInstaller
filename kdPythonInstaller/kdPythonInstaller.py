'''
Created on 2019年4月5日

@author: bkd
'''
from os import environ,name,system
from os.path import join,dirname,realpath
import platform
from webbrowser import open_new_tab
from tkinter import Tk,Button,ttk,messagebox
from tkinter.constants import W,E
try:
    from os import startfile
except Exception as e:
#     messagebox.showerror("导入os.startfile", "导入python模块失败")
    pass

cur_dir = dirname(realpath(__file__))
# 获取文件的位置
def get_file_realpath(file):
    return join(cur_dir,file)

# 查看系统信息
def get_sysinfo():
    messagebox.showinfo("系统信息", "系统名称:\t" + platform.system() +"\n处理器：\t" + platform.processor()  + \
                        "\n\n系统路径：\t" + environ["PATH"])

#     下载64位的安装包
def down64_installer():
    open_new_tab("https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe")

#     下载32位的安装包
def down32_installer():
    open_new_tab("https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe")

#     安装pip
def install_pip():
    script_path = get_file_realpath("get-pip.py") 
    run_cmd("python " + script_path)
    messagebox.showinfo("安装pip", "安装pip成功")

# 安装软件
def install_package(package_name):
    if package_name :
        run_cmd("pip install " + package_name )
        messagebox.showinfo("安装软件", "安装"+ package_name + "成功")
    else :
        messagebox.showerror("安装软件", "请输入软件名")
        
# 卸载软件        
def uninstall_package(package_name):
    if package_name :
        run_cmd("pip uninstall " + package_name + " -y")
        messagebox.showinfo("卸载软件", "卸载"+ package_name + "成功")
    else :
        messagebox.showerror("卸载软件", "请输入软件名")
        
# 运行命令
def run_cmd(cmd):
    if name == "nt":
        startfile(cmd)
    elif name == "posix":
        system(cmd)
    else :
        messagebox.showerror("执行命令", "暂不支持的系统")
        
def main():
    root = Tk()
    Button(root, text='0.查看系统信息',command=get_sysinfo).grid(row=0, column=0, sticky=W,ipadx=11)
    ttk.Label(root, text="系统类型：" + platform.system()).grid(row=0, column=1)
    Button(root, text='1.安装64位python',command=down64_installer).grid(row=1, column=0, sticky=W)
    Button(root, text='1.安装32位python',command=down32_installer).grid(row=2, column=0, sticky=W)
    Button(root, text='2.安装pip',command=install_pip).grid(row=3, column=0, sticky=W,ipadx=27)
    package_entry = ttk.Entry(root, font=(None, 16))
    package_entry.grid(row=1, column=1, sticky=W)
    Button(root, text='3.安装软件',command=lambda :install_package(package_entry.get())).grid(row=2, column=1, sticky=E,ipadx=78)
    Button(root, text='4.卸载软件',command=lambda :uninstall_package(package_entry.get())).grid(row=3, column=1, sticky=E,ipadx=78)
    root.mainloop()
if __name__ == '__main__':
    main()