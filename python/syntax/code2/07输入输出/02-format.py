"""字符串的format()方法
"""


"""f字符串"""
print('We are the {} who say "{}!"'.format('knights', 'Ni')) # We are the knights who say "Ni!"

"""指定位置参数"""
print('{0} and {1}'.format('spam', 'eggs')) # spam and eggs
print('{1} and {0}'.format('spam', 'eggs')) # eggs and spam

"""关键字参数"""
print('This {food} is {adjective}.'.format(
    food='spam', 
    adjective='absolutely horrible')
) # This spam is absolutely horrible.

"""位置参数和关键字参数"""
print('The story of {0}, {1}, and {other}.'.format(
    'Bill', 'Manfred',
    other='Georg')
) # The story of Bill, Manfred, and Georg.


"""字典参数"""
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# 写法一 位置参数
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table)
) # Jack: 4098; Sjoerd: 4127; Dcab: 8637678
# 写法二 字典解包
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)) # # Jack: 4098; Sjoerd: 4127; Dcab: 8637678
