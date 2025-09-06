"""字符串
字符串可以使用单引号、双引号、三重引号包裹
单引号和双引号无区别
三重引号既可以作为多行注释，又可以包裹字符串，
包裹字符串时可以换行
以上三种写法都可以使用转义字符

r-string纯字符串 忽视转义字符
"""

"""使用单引号或双引号包裹字符串"""
str1 = 'hello world'
print(type(str1)) # <class 'str'>
print(str1) # hello world

# 使用转义字符
str2 = "he\nllo wo\trld"
print(str2)
    # he
    # llo wo  rld

# 字符串太长可以使用\换行，便于观看
str3 = 'this is a very long string,\
very,very,very long'
    # str3 = 'this is a very long string,very,very,very long'
    # 以上两种写法等价
print(str3) # this is a very long string,very,very,very long

# 字符串的加法运算（拼接字符串）
str4 = str1 + '123' 
print(str4) # hello world123


# 相邻的两个或多个字符串字面值（引号标注的字符）会自动合并
# 必须是字面量，不能是变量，否则报错
print('hello' 'world') # helloworld


# 基于上面的特性，可以使用 + 或 ()来赋值比较长的字符串
# 方法一 +=
long_str1 = 'hello world, '
long_str1 += 'hello python'
print(long_str1) # hello world, hello python
# 方法二 ()
long_str2 = ('hello world, '
    'hello python, '
    'hello python world'
)
print(long_str2) # hello world, hello python, hello python world


# 字符串的乘法运算（重复n次）
str5 = str1 * 5
print(str5) # hello worldhello worldhello worldhello worldhello world


"""三重引号包裹的字符串"""
print('-'*10)
# 换行会导致首尾多出一些换行符
str6 = """
hello world
    python
string
int\tfloat\nstr list tuple dict
"""
print(str6)
print('-'*10)
    # ----------
    #
    # hello world
    #     python
    # string
    # int     float
    # str list tuple dict
    #
    # ----------
print('-'*10)

# 通过\可以删除多行字符串首尾多出的换行符
str6 = """\
hello world
    python
string
int\tfloat\nstr list tuple dict\
"""
print(str6)
print('-'*10)
    # ----------
    # hello world
    #     python
    # string
    # int     float
    # str list tuple dict
    # ----------

"""纯字符串r-string"""
str7 = r'he\tllo wo\nrld'
print(str7) # he\tllo wo\nrld
