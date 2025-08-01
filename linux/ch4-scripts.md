# shell 脚本编程基础

## shell 编程概述

shell 本身是一个用 C 语言编写的程序，是连接 用户 和 UNIX/Linux 内核 的桥梁。

一个简单的shell脚本 `ShowHello.sh` （Linux脚本一般使用 `.sh` 作为文件后缀名）：

``` shell
#! /bin/bash
#ShowHello
#To show hello to somebody
echo -n "Enter your name:"
read name
echo "Hello, $name"
```

- 第一行 `#! /bin/bash` 这是一个特殊的标记（称为 shebang），告诉系统这个脚本需要用 `/bin/bash` 这个程序来执行，是 shell 脚本的标准开头。通常放在脚本第一行，从而调用相应的解释程序予以执行
- 第二行 `#ShowHello` 和第三行 `#To show hello to somebody` 以 `#` 开头的行是注释，不会被执行，用来解释脚本的功能
- 第四行 `echo -n "Enter your name:"` echo 是输出文字的命令，-n 选项表示输出后不自动换行。这行的效果是在屏幕上显示 "Enter your name:"，光标会停在冒号后面等待输入
- 第五行 `read name` read 命令用来接收用户从键盘输入的内容，这里把输入的内容保存到变量 name 中。比如你输入 "Tom"，那么 name 这个变量就代表 "Tom"
- 第六行 `echo "Hello, $name"` 再次使用 echo 输出内容，$name 表示取出变量 name 中保存的值。如果之前输入了 "Tom"，这行就会输出 "Hello, Tom"

这个shell脚本还不能运行，因为它没有 `x` 权限，无法作为应用程序执行。为这个脚本的所有者 `u` 添加 `x` 权限 `$ chomd u+x ShowHello.sh`

Linux 中，创建文件默认是不可执行的文件，需要修改文件的权限，为文件增加可执行权限，后在命令行模式下直接输入该文件的相对路径 ./文件名，即可运行

``` bash
$ vim ShowHello.sh
$ ./ShowHello.sh
-bash: ./ShowHello.sh: Permission denied
$ ls -l
total 8
-rw-r--r-- 1 d111kc d111kc  108 Jul 31 20:23 ShowHello.sh
-rw-r--r-- 1 d111kc d111kc    0 Jul 30 21:05 note1.txt
drwxr-xr-x 2 d111kc d111kc 4096 Jul 30 21:04 test1
$ chmod u+x ShowHello.sh
$ ./ShowHello.sh
Enter your name:Mike
Hello, Mike
```

## shell 的种类

shell脚本的第一行需要指出该脚本的解释程序，即shell的种类。Linux系统提供了多种不同的shell。

查看Linux系统提供的shell种类：

``` bash
$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/usr/bin/dash
/usr/bin/tmux
```

最常见的shell有Bourne shell（简称sh）、C shell（简称csh）、Korn shell（简称ksh）和Bourne-again shell（简称bash）。默认的shell是bash，它具有以下优点：

- 命令记忆功能 通过键盘上的上下箭头可以快速输入之前输入过的命令
- Tab自动补全
- 设置别名功能 例如 `$ alias ll='ls -l'` 可以将 `ls -l`的别名设置为 `ll`

## shell 脚本的运行

有3中方式执行shell脚本：

### 方式一

将shell脚本的权限设置为可执行，然后在提示符下直接运行。脚本文件的编辑完成后，利用chmod命令修改脚本文件的权限为可执行，如前面的示例：

``` bash
$ chmod u+x ShowHello.sh
$ ./ShowHello.sh
```

在运行该脚本时，必须给出该脚本的相对路径（如 `./ShowHello.sh`，这个相对路径不能省略 `./`）或绝对路径。在执行系统命令时，只需要给出命令文件名。因为命令和用户的可执行脚本文件是否能够执行，与环境变量PATH有关。

查看环境变量PATH `$ echo $PATH`

环境变量PATH的值决定了shell将到哪些目录中寻找命令或可执行程序，当用户运行一个命令或可执行程序时，Linux在这些目录下按顺序依次搜寻。由于用户的可执行脚本是放在用户家目录下的，所以直接输人 `ShowHello.sh`，系统无法找到该文件。

通过这种方式运行脚本，脚本文件第一行的`#！/bin/bash`一定要写对，好让系统查找到正确的解释器。

### 方式二

以脚本名作为参数传递给shell程序。

``` bash
$ bash ShowHello.sh
Enter your name:Mike
Hello, Mike
```

这种执行方式就是运行bash，将脚本 `ShowHello.sh` 作为参数传递给bash。通过这种方式运行脚本，不需要在脚本文件的第一行指定解释器信息，并且脚本名后面还可以带参数。

### 方式三（不推荐使用）

将脚本以输人重定向的方式传递给bash。

运行bash程序，以输入重定向的方式让bash从给定文件中读入命令行，并进行相应处理。

``` bash
d111kc@D111KC:~$ bash < ShowHello.sh
Enter your name:d111kc@D111KC:~$
```

这种方式的脚本后面是不能带参数的

## shell 基础

shell脚本是文本文件

### 通配符

文件名的扩展称为通配（Globbing）

- `*` 匹配任意字符（不包括路径分隔符`/`）的 0 次或多次出现
- `?` 匹配任意单个字符（不包括 `/`）
- `[]` 将一组字符列表括起来，其作用是匹配该列表中的任意一个字符。例如，`space.[co]`匹配`space.c`或者`space.o`，`[Hh]*`匹配以“H"或“h”开头的文件名。`[]`中无论有几个字符，都只代表某一个字符。在`[]`中，可以使用 `-` 指定字符的范围，例如`[0-9]`匹配任何0至9的数字。
- `[^]` 或 `[!]` 为了匹配不在列表中的字符，需要在列表的开头加一个`^`或者`!`，代表反向选择。例如，`[^Hh]*`和`[!Hh]*`匹配以非“H"或“h”开头的文件名。
- `{stringl,string2,...}` 匹配 sringl或 string2（或更多）中的一个字符串。`{}`告诉shell依次使用每种string形成一个单独的文件名进行匹配，大括号扩展只适用于bash、tcsh和Cshell，不适用于Kornshell和FreeBSDshell。例如，用户希望查看目录/home/student，/home/cs1，/home/re中所有文件的名称，`$ ls /home/student /home/cs1 /home/re`
使用通配符命令就比较简单：`$ ls /home/{student,cs1,re}` 大括号中的逗号前面和后面都不能有空格

### 转义字符

shell默认支持转义字符，如果是特殊字符想要表示字面意义需要在前面添加 `\` 转义

### 引号

shell 中引用字符有 3 种：单引号`''`，双引号`""`和反引号`

1. 单引号引用一串字符，所有字符都是普通字符

#### 单引号

被单引号括起来的所有字符都是普通字符，就算特殊字符也不再有特殊含义。在某些时候，会希望使用个别特殊字符，如`$`来引用变量的值，例如：

``` bash
$ echo 'the directory is $HOME; the userid is $USER'
the directory is $HOME; the userid is $USER
```

很显然这样的输出并不是我们所需要的。这时命令就不能正常工作，在不使用转义字符 `\`（若命令中存在多个特殊字符，使用转义字符“\”会让命令可读性变差）时，双引号可以很好地解决这个问题。

#### 双引号

由双引号括起来的字符（除`$`、反引号和转义字符 `\` 外）均作为普通字符。“$”“\”和倒引号是拥有特殊含义的，“$”代表引用变量的值，而反引号代表引用命令。在上述例题中，采用双引号可以使 `$` 保留特殊含义

``` bash
d111kc@D111KC:~$ echo 'the directory is $HOME; the userid is $USER'
the directory is $HOME; the userid is $USER
d111kc@D111KC:~$ echo "the directory is $HOME; the userid is $USER"
the directory is /home/d111kc; the userid is d111kc
```

``` bash
$ name=d111kc
$ echo '$name'
$name
$ echo "$name"
d111kc
```

如果需要在双引号中间输出“$”和倒引号，则要在符号前加转义符“\”

#### 反引号

由反引号括起来的字符串被shell解释为命令行，shell会先执行该命令，并以它的标准输出结果取代整个倒引号部分。

``` bash
$ today=`date`
$ echo "Today is $today"
Today is Thu Jul 31 21:45:01 CST 2025
```

### 重定向符

输入/输出方向就是数据的流动方向。
1. 标准输入重定向
1.1 command<file 将文件作为命令的输入
[root@localhost ~]# wc -l<file 表示统计 file 文件中有多少行文本
1.2 command<<分界符 从标准输入中读入，直到遇见分界符才停止。使用特定的分界
符作为命令输入的结束标志，而不使用默认的 Ctril+D 组合键。
1. 标准输出重定向
2.1 command>file 以覆盖的方式，把 command 的正确输出结果输出到 file 文件
[root@localhost ~]# cat file1 file2>file3 . 这种方式将命令的输出写到文件时，这个文件可
以存在也可不存在，不存在就自动创建，存在则原文件内容将被覆盖。
2.1 command>>file 以追加的方式，把 command 的正确输出结果输出到 file 文件
1. 文件描述符
输出重定向的完整写法是 fd>file, fd>>file，fd 表示文件描述符，file descriptor。不写默认
为 1. 标准输入 stdin ， 0；
标准输出 stdout， 1；
错误输出 stderr， 2；
如：
grep li si file: si 和 file 被视作两个文件名，查找 li
若需要把正确和错误信息都保存在一个文件中，应这样写：
ying@ying-virtual-machine:~/one$ grep li si file >file1 2>& 1
2>& 之间不允许有空格，fd> 间不允许有空格
若既不想把结果保存到文件中，也不想显示到屏幕上，可以把结果重定向到/dev/null 文件
中，
/dev/null 视作 Linux 系统的垃圾箱，数据都会被丢弃，不能恢复。
4.2.4 命令执行操作符
1. 顺序执行
使用“；”连接多条命令，这些命令会依次执行。
1. 逻辑与
“&&”连接，这些命令之间就有逻辑关系。只有第一条命令正确执行了，&&连接的第二条
命令才会执行。
1. 逻辑或
“||”连接多条命令，则只有前一条命令执行错误，后一条命令才能执行。
4.2.5 小括号和大括号
当用户启动 shell 时，这个 shell 是 __ 交互__ 的，当它执行完第一条命令后，接着显示另一
个提示符，始终在前台等待用户。还有一种 shell 是 __ 非交互__ 的，当在交互 shell 中运行
一个外部命令或者执行一个脚本时，交互 shell 会创建一个子 shell，运行结束后子 shell 进
程结束。
小括号（）和大括号{}都可以将若干命令括起来，组合在一起，逻辑上视为一条命令。
后台进程在运行过程中与用户无交互，无交互是指 __不响应用户的输入和终端控制
信号__ ，在后台运行的命令一样会将结果输出到显示器上。