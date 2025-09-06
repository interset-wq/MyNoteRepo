import os
cwd_dir = os.getcwd()      # 返回当前工作目录
print(cwd_dir) # C:\Users\d111k\Desktop\MyNoteRepo\python\standard-lib

os.chdir(r'C:\Users\d111k\Desktop')   # 改变当前工作目录
print(os.getcwd()) # C:\Users\d111k\Desktop
os.system('mkdir today')   # 在系统 shell 中运行 mkdir 命令创建today目录
