"""测试 unittest"""

from survey import AnonymousSurvey
import unittest


# class TestAnonymousSurvey(unittest.TestCase):
#     """用于测试AnonymousSurvey类的类"""
#
#     def test_store_1_answer(self):
#         """测试只回答1个答案的情况"""
#         question = '你会什么编程语言或标记语言？'
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_answer('C')
#         self.assertIn('C', my_survey.answers)
#
#     def test_store_3_answers(self):
#         """测试回答3个答案的情况"""
#         question = '你会什么编程语言或标记语言？'
#         my_survey = AnonymousSurvey(question)
#         answers = ['html', 'css', 'javascripts']
#         for answer in answers:
#             my_survey.store_answer(answer)
#         for answer in answers:
#             self.assertIn(answer, my_survey.answers)

class TestAnonymousSurvey(unittest.TestCase):
    """用于测试AnonymousSurvey类的类"""

    def setUp(self): # 类似于pytest中的夹具
        """创建一个问卷调查对象和一组答案"""
        question = '你会什么编程语言或标记语言？'
        self.my_survey = AnonymousSurvey(question)
        self.answers = ['html', 'css', 'javascripts']

    def test_store_1_answer(self):
        """测试只回答1个答案的情况"""
        self.my_survey.store_answer(self.answers[0])
        self.assertIn(self.answers[0], self.my_survey.answers)

    def test_store_3_answers(self):
        """测试回答3个答案的情况"""
        for answer in self.answers:
            self.my_survey.store_answer(answer)
        for answer in self.answers:
            self.assertIn(answer, self.my_survey.answers)

if __name__ == '__main__':
    unittest.main()