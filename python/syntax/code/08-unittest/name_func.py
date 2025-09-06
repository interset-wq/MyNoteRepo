"""被测试的函数"""


# def get_format_name(first: str, last: str) -> str:
#     """返回完整格式的姓名"""
#     return first + ' ' + last

# def get_format_name(first: str, middle: str, last: str) -> str:
#     """返回完整格式的姓名"""
#     return first + ' ' + middle + ' ' + last

def get_format_name(first: str, last: str, middle: str='') -> str:
    """返回完整格式的姓名"""
    if middle:
        return first + ' ' + middle + ' ' + last
    else:
        return first + ' ' + last



if __name__ == '__main__':
    """手动测试"""
    print('输入q结束程序')
    while True:
        first_name = input('输入你的名： ')
        if first_name == 'q':
            break
        last_name = input('输入你的姓： ')
        if last_name == 'q':
            break
        full_name = get_format_name(first_name, last_name)
        print(f'你的全名是 {full_name}')