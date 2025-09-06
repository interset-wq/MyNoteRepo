"""函数注解和文档字符串"""

# 写法一
def person_info(name: str, gender: str, age: int | None=None) -> dict[str, str | int]:
    """一个人的基本信息
    
    Args:
        name (str): 姓名
        gender (str): 性别
        age (int): 年龄
    
    Returns:
        dict: 人的基本信息字典
        
    Examples:
        >>> person_info("张三", "男")
        {'姓名': '张三', '性别': '男'}
        
        >>> person_info("李四", "女", 30)
        {'姓名': '李四', '性别': '女', '年龄': 30}
    """
    info = {'姓名': name, '性别': gender}
    if age:
        info['年龄'] = age
    return info

# 写法二 vscode无法识别这种格式的文档字符串
def person_info2(name: str, gender: str, age: int | None=None) -> dict[str, str | int]:
    """
    一个人的基本信息
    :param name: 这个人的姓名
    :param gender: 这个人的年龄
    :param age: 这个人的年龄，可选参数
    :return: 返回这个人的基本信息字典
    """
    info = {'姓名': name, '性别': gender}
    if age:
        info['年龄'] = age
    return info
    
if __name__ == '__main__':
    my_dict = person_info('cook', 'male', 17)
    print(my_dict) # {'姓名': 'cook', '性别': 'male', '年龄': 17}