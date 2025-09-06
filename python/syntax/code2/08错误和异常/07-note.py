"""用注释细化异常情况
当一个异常被创建以引发时，它通常被初始化为描述所发生错误的信息。
在有些情况下，在异常被捕获后添加信息是很有用的。
为了这个目的，异常有一个 add_note(note) 方法接受一个字符串，
并将其添加到异常的注释列表。
标准的回溯在异常之后按照它们被添加的顺序呈现包括所有的注释。
"""

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\07-note.py", line 10, in <module>
#     raise TypeError('bad type')
# TypeError: bad type
# Add some information
# Add some more information