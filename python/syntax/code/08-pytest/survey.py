"""被测试的类"""


class AnonymousSurvey:
    """一个表示匿名问卷的类"""
    def __init__(self, question: str):
        self.question = question
        self.answers: list[str] = []

    def print_question(self) -> None:
        """将问卷的问题打印在屏幕上"""
        print(self.question)

    def store_answer(self, answer: str) -> None:
        """收集单份问卷的答案"""
        self.answers.append(answer)

    def print_answers(self) -> None:
        print('这个问题得到的答案是：')
        for index, answer in enumerate(self.answers, start=1):
            print(index, answer)


if __name__ == '__main__':
    """手动测试"""
    # 创建一个AnonymousSurvey实例对象
    question = '你会什么编程语言或标记语言？'
    my_survey = AnonymousSurvey(question)
    my_survey.print_question()
    while True:
        answer = input('输入你的答案，输入q停止： ')
        if answer == 'q':
            break
        my_survey.store_answer(answer)
    my_survey.print_answers()