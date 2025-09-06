"""match-case和类
"""

"""
# 如果用类组织数据，
# 可以用“类名后接一个参数列表”这种很像构造器的形式，
# 把属性捕获到变量里
"""

"""不定义魔术属性__match_args__
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        # 必须使用关键字参数创建实例 从而捕获match中提供的变量
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

"""定义魔术属性__match_args__
"""

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")