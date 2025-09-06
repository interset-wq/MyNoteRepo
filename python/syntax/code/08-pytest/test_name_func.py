"""测试函数 pytest"""

from name_func import get_format_name


def test_first_last_name():
    """这个测试函数用于测试 Tom White 格式的全名"""
    full_name = get_format_name('Tom', 'White')
    assert full_name == 'Tom White'

    
def test_first_last_middle_name():
    """用于测试 Tom Walt White 格式的全名"""
    full_name = get_format_name('Tom', 'White', middle='Walt')
    assert full_name == 'Tom Walt White'