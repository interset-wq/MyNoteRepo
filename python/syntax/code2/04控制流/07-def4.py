"""不定长参数"""


# 最后一个形参为 **name 形式时，接收一个字典，
# 该字典包含与函数中已定义形参对应之外的所有关键字参数。
# **name 形参可以与 *name 形参组合使用（*name 必须在 **name 前面），
# *name 形参接收一个 元组，该元组包含形参列表之外的位置参数。

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    # arguments是一个元组
    for arg in arguments:
        print(arg)
    print("-" * 40)
    # keywords是一个元组
    for kw in keywords:
        print(kw, ":", keywords[kw])

if __name__ == '__main__':
    cheeseshop(
        "Limburger", # 位置参数kind
        "It's very runny, sir.", # 不定长位置参数argments的一个元素
        "It's really very, VERY runny, sir.", # 不定长位置参数
        shopkeeper="Michael Palin", # 不定长关键字参数
        client="John Cleese", # 不定长关键字参数
        sketch="Cheese Shop Sketch" # 不定长关键字参数
    )