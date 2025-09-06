import glob, os

"""切换工作目录"""
os.chdir(r'C:\Users\d111k\Desktop\MyNoteRepo\python\standard-lib')
print(os.getcwd()) # C:\Users\d111k\Desktop\MyNoteRepo\python\standard-lib

"""获取所有后缀名是md的文件列表"""
print(glob.glob('*.md')) # ['lib.md', 're.md', 'string.md', 'threading.md']