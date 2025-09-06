"""测试函数 unittest"""


import unittest
from name_func import get_format_name


class NameTestCasse(unittest.TestCase):
    """用于测试name_func.py的类"""

    def test_first_last_name(self):
        """这个测试函数用于测试 Tom White 格式的全名"""
        full_name = get_format_name('Tom', 'White')
        self.assertEqual(full_name, 'Tom White')  # 断言

    def test_first_last_middle_name(self):
        """用于测试 Tom Walt White 格式的全名"""
        full_name = get_format_name('Tom', 'White', middle='Walt')
        self.assertEqual(full_name, 'Tom Walt White')


if __name__ == '__main__':
    unittest.main()