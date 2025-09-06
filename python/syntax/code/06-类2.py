class Car:
    """一个代表汽车的类"""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """汽车的基本信息——品牌，型号，生产年份，里程表示数"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer: float = 0 # 汽车历程表读数

    def get_detailed_info(self) -> str:
        """返回一条包含品牌，型号和生产年份的字符串"""
        return f'这辆车是{self.brand} {self.model}，生产年份是{self.year}。'

    def print_odometer(self) -> None:
        """打印里程表示数"""
        print(f'这辆汽车总共行驶了{self.odometer}公里。')

    def set_odometer(self, km_mileage: float) -> None:
        """基本上没有汽车的里程表示数是0，汽车里程表不允许回调"""
        if km_mileage >= self.odometer:
            self.odometer = km_mileage
        else:
            raise ValueError('汽车里程表的示数禁止回调')

    def increse_odometer(self, kilometers: float) -> None:
        # 汽车每次行驶时，里程数都要增加
        self.odometer += kilometers


class ElectricCar(Car):
    """一个用于表示电动汽车的类，继承自Car"""

    def __init__(self, brand: str, model: str, year: int) -> None:
        # 继承父类的属性
        super().__init__(brand, model, year)
        self.battery_size: int = 40

    def print_battery(self) -> None:
        """打印电池容量信息"""
        print(f'这辆电动汽车的电池容量是{self.battery_size}千瓦时')