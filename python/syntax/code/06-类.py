class Dog:
    """一个用来表示小狗的类"""

    def __init__(self, name, gender, age):
        # 实例属性
        self.name = name
        self.gender = gender
        self.age = age

    def sit(self):
        # 小狗坐下这种行为
        print(self.name + '坐下来了')

    def roll_over(self):
        # 小狗打滚这种行为
        print(self.name + '开始打滚了')