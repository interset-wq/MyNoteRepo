class Banana:
    """一个用于表示香蕉的类"""

    food_group = 'fruit'
    colors = ['green', 'green-yellow', 'yellow', 'brown-spotted', 'black']
    __ripe_colors = ['yellow', 'brown-spotted']  

    def __init__(self, color='green'):  
        if not self.check_color(color):
            raise ValueError(f'{self.__class__.__name__} cannot be {color}!!!')
        self.color = color
        self.peeled = False

    def __str__(self):  
        return f'A {self.color} {self.__class__.__name__}'

    def peel(self):
        # 香蕉去皮
        self.peeled = True

    def set_color(self, color):
        # 香蕉颜色
        if color in self.colors:
            self.color = color
        else:
            raise ValueError(f'{self.__class__.__name__} cannot be {color}!!!')

    def can_eat(self):
        # 香蕉是否可以吃
        return self._is_ripe()

    def _is_ripe(self):  
        """香蕉是否成熟"""
        return self.color in self.__ripe_colors

    @classmethod  
    def check_color(cls, color):
        # 检查传入的颜色是否可能是香蕉的颜色，返回布尔值
        return color in cls.colors

    @classmethod
    def make_greenie(cls):
        # 创建一个绿色香蕉对象
        banana = cls()  
        banana.set_color('green')
        return banana

    @staticmethod  
    def estimate_calories(num_bananas):
        # 计算卡路里
        return num_bananas * 105


class RedBanana(Banana):  
    """表示红色香蕉的类"""

    colors = ['green', 'arange', 'red', 'brown', 'black']
    botanical_name = 'red dacca'

    def __init__(self, color='green'):
        super().__init__(color)  

    def peel(self):  # (10)
        super().peel()
        print('It just like normal Banana')