# 计算机二级python常用语法

## f-string 格式控制

基本语法 `f"{变量名:格式控制标记}"`

格式控制标记 `<填充字符><对齐方式><宽度><,><.精度><类型>`

- 填充字符 默认是空格，只能是单个字符，需要配合 `宽度` 使用
- 对齐方式 需要配合`宽度`使用：
    - `^` 居中
    - `>` 右对齐
    - `<` 左对齐
- 宽度 整数，表示这个字符串的长度
- `,` 千位分隔符

## random库

- `random.randint(a, b)` 生成随机整数，闭区间

## 内置函数eval()

eval(source, /, globals=None, locals=None) 将传入的值转换为python表达式

    参数:

            source (str | code object) -- 一个 Python 表达式。

            globals (dict | None) -- 全局命名空间 (默认值: None)。

            locals (mapping | None) -- 局部命名空间 (默认值: None)。

    返回:

        被求值表达式的求值结果。
    引发:

        语法错误将作为异常被报告。

    警告

    此函数可执行任意代码。 调用它时附带用户提供的输入可能导致安全弱点。

    expression 参数将作为一个 Python 表达式 (从技术上说，是一个条件列表) 使用 globals 和 locals 映射作为全局和局部命名空间被解析并求值。 如果 globals 字典存在并且不包含 __builtins__ 键对应的值，则在 expression 被解析之前会插入该键对应的指向内置模块 builtins 的字典的引用。 这样你就可以在将 globals 传给 eval() 之前通过向其传入你自己的 __builtins__ 字典来控制被执行代码可以使用哪些内置对象。 如果 locals 映射被省略则它将默认为 globals 字典。 如果两个映射都被省略，则将使用调用 eval() 所在环境中的 globals 和 locals 来执行该表达式。 请注意，eval() 将只能访问所在环境中的 嵌套作用域 (非局部作用域)，如果它们已经在调用 eval() 的作用域中被引用的话 (例如通过 nonlocal 语句)。

``` py
>> x = 1
>> eval('x+1')
>> 2
```

该函数还可用于执行任意代码对象（比如由 compile() 创建的对象）。 这时传入的是代码对象，而非一个字符串了。如果代码对象已用参数为 mode 的 'exec' 进行了编译，那么 eval() 的返回值将为 None。

如果给出的源数据是个字符串，那么其前后的空格和制表符将被剔除。

## 第三方库jieba

- `jieba.cut(sentence, cut_all=False, HMM=True, use_paddle=False)` 函数 返回generator迭代器, 可以使用 `list()`函数 转换为分词之后的 `list` 对象
    - `sentence` 需要分词的字符串
    - `cut_all` 参数用来控制是否采用全模式
    - `HMM` 参数用来控制是否使用 HMM 模型
    - `use_paddle` 参数用来控制是否使用paddle模式下的分词模式
- `jieba.cut_for_search(sentence, HMM=True)` 函数 返回generator迭代器, 可以使用 `list()`函数 转换为分词之后的 `list` 对象. 搜索引擎模式, 该方法适合用于搜索引擎构建倒排索引的分词. 效果类似于 `jieba.cut()`全模式
    - `sentence` 需要分词的字符串. unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
    - `HMM` 是否使用 HMM 模型        

???+ note
    `jieba.cut()` 以及 `jieba.cut_for_search()` 返回的结构都是一个可迭代的 `generator` ，可以使用 for 循环来获得分词后得到的每一个词语(unicode)，或者用 `jieba.lcut()` 以及 `jieba.lcut_for_search()` 直接返回 `list`对象

