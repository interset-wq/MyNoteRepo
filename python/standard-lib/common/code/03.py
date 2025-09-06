import shutil, os

"""切换当前工作目录"""
os.chdir(r'C:\Users\d111k\Desktop\MyNoteRepo\python\standard-lib\os-shutil\code')
print(os.getcwd()) # C:\Users\d111k\Desktop\MyNoteRepo\python\standard-lib\os-shutil\code

"""复制文件"""
# shutil.copyfile('02.py', 'example.py')

"""移动文件"""
shutil.move('example.py', '../')