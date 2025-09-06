
## 十、测试unittest/pytest

可以使用 *标准库unittest* 或 *第三方库pytest* 进行单元测试。一种最简单的测试是单元测试（unit test），用于核实函数的某个方面没有问题。测试用例（test case）是一组单元测试，这些单元测试一道核实函数在各种情况下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情况的测试。全覆盖（full coverage）测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。

使用 pytest 进行测试，会让单元测试编写起来非常简单。我们将编写一个测试函数，它会调用要测试的函数，并做出有关返回值的断言 （`assert` 语句）。如果断言正确，表示测试通过；如果断言不正确，表示测试未通过。

测试函数和测试文件必须以 `test_` 开头

几种常用的断言（类似于if语句的条件判断）：

|         unittest断言         |          pytest断言          | 用途                |
|:--------------------------:|:--------------------------:|:------------------|
|     assertEqual(a, b)      |       assert a == b        | 断言两个值相等           |
|    assertNotEqual(a, b)    |       assert a != b        | 断言两个值不等           |
|       assertTrue(a)        |          assert a          | 断言 a 的布尔求值为 True  |
|       assertFalse(a)       |        assert not a        | 断言 a 的布尔求值为 False |
|  assertIn(element, list)   |   assert element in list   | 断言元素在列表中          |
| assertNotIn(element, list) | assert element not in list | 断言元素不在列表中         |

### 10.1 对函数进行单元测试pytest

测试文件和被测试文件要放在同一个目录下，此处都放置在 `code/08-pytest` 目录下。

#### 需要被测试的函数

`name_func.py`

```py
def get_format_name(first: str, last: str) -> str:
    """返回完整格式的姓名"""
    return first + ' ' + last
```

#### 测试函数

`test_name_func.py`

#### 运行测试

Pycharm运行测试非常简单，测试函数旁边会出现运行按钮，点击即可运行测试

通用方法：终端使用cd将当前工作目录切换到 `code/08-pytest`，输入`pytest`，回车

### 10.1 对函数进行单元测试unittest

测试文件和被测试文件要放在同一个目录下，此处都放置在 `code/08-unittest` 目录下。

#### 需要被测试的函数

`name_func.py`

#### 测试函数

`test_name_func.py`

#### 运行测试

直接运行 `test_name_func.py`

---

如果我们修改被测试函数，使它能够处理有中间名的姓名：

```py
def get_format_name(first, middle, last):
    """返回完整格式的姓名"""
    return first + ' ' + middle + ' ' + last
```

此时运行测试，测试将不会通过

测试不通过，说明我们编写的用于获取全名的函数 `name_func()` 并没有完成我们预期的行为：将只有姓和名的名字合成为全名，以及将有姓、名以及中间名的名字合成为全名。这种情况下我们应该修改 `name_func()` 这个函数，而不是修改测试。

修改后的 `name_func.py`

```py
def get_format_name(first, last, middle=''):
    """返回完整格式的姓名"""
    if middle:
        return first + ' ' + middle + ' ' + last
    else:
        return first + ' ' + last
```

此时运行测试，测试将通过。但是我们编写的测试函数只会测试只有姓和名的情况，并不会测试有中间名的情况，因此我们要添加一个用于测试含有中间名名字的测试。

### 10.2 对类进行单元测试

1. 一个需要被测试的类 `survey.py`
2. 编写测试函数 `test_survey.py`

    在测试中，夹具（fixture）可帮助我们搭建测试环境。这通常意味着创建供多个测试使用的资源。在 pytest 中，要创建夹具，可编写一个使用装饰器 @pytest.fixture装饰的函数。装饰器（decorator）是放在函数定义前面的指令。在运行函数前，Python将该指令应用于函数，以修改函数代码的行为。

3. 运行测试
