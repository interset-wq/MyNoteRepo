"""match-case"""


# 形如解包赋值的模式可被用于绑定变量

def position(point):
    # point 是一个 (x, y) 元组
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")



if __name__ == '__main__':
    point = (0, 3)
    position(point)