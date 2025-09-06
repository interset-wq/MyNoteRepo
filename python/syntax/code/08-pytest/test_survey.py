"""测试 pytest"""
from survey import AnonymousSurvey
from pytest import fixture

"""不使用夹具 两个测试函数要分别创建AnonymousSurvey实例，浪费了资源"""
# def test_store_1_answer():
#     """测试只回答1个答案的情况"""
#     question = '你会什么编程语言或标记语言？'
#     my_survey = AnonymousSurvey(question)
#     my_survey.store_answer('C')
#     assert 'C' in my_survey.answers
#
#
# def test_store_3_answers():
#     """测试回答3个答案的情况"""
#     question = '你会什么编程语言或标记语言？'
#     my_survey = AnonymousSurvey(question)
#     answers = ['html', 'css', 'javascripts']
#     for answer in answers:
#         my_survey.store_answer(answer)
#     for answer in answers:
#         assert answer in my_survey.answers


"""使用夹具简化测试 只需要创建一次AnonymousSurvey实例"""
@fixture
def my_survey():
    """一个可供所有测试函数使用的 AnonymousSurvey 实例"""
    question = '你会什么编程语言或标记语言？'
    my_survey = AnonymousSurvey(question)
    return my_survey

def test_store_1_answer(my_survey):
    """测试只回答1个答案的情况"""
    my_survey.store_answer('C')
    assert 'C' in my_survey.answers

def test_store_3_answers(my_survey):
    """测试回答3个答案的情况"""
    answers = ['html', 'css', 'javascripts']
    for answer in answers:
        my_survey.store_answer(answer)
    for answer in answers:
        assert answer in my_survey.answers