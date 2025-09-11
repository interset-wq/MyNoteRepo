# 常用Linux命令

## Linux 命令提示符

- root用户 `[root@localhost ~]#`
- 普通用户 `[d111kc@localhost Desktop]$`

命令提示符的说明：

- `root` 和 `d11kc` 表示当前的登陆用户
- `@` 是分隔符号，没有特殊含义
- `localhost` 当前系统的主机名（`localhost`完整名 `localhost.localdommain`），主机名是电脑的设备名，自定义设备名之后显示的不是`localhost`
- `~` 和 `Desktop` 当前所在目录 `~` 特指用户文件夹（家目录/主目录），root用户的用户文件夹是 `/root`，普通用户的用户文件夹是 `/home/<username>`，打开终端时默认进入的是家目录
- `#` 和 `$` 命令提示符，root用户是 `#`，普通用户是 `$`

## Linux 命令的基本格式

`$ 命令 [选项] [参数]`

Linux 选项：

- 短格式选项 为英文简写，以 `-` 开头
- 长格式选项 为完整英文单词，以 `--` 开头

``` bash
[d111kc@localhost ~]$ ls
Desktop    Downloads  Pictures  Templates
Documents  Music      Public    Videos
[d111kc@localhost ~]$ ls -l
总用量 0
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Desktop
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Documents
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Downloads
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Music
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Pictures
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Public
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Templates
drwxr-xr-x. 2 d111kc d111kc 6 8月  13 16:45 Videos
[d111kc@localhost ~]$ ls --all
.              .bashrc  Desktop    .ICEauthority  Pictures
..             .cache   Documents  .local         Public
.bash_logout   .config  Downloads  .mozilla       Templates
.bash_profile  .dbus    .esd_auth  Music          Videos
```

`ls` 可以不传参，是因为它有默认参数，那就是当前所在目录

命令的选项用于调整命令的执行方式，而命令的参数是这个命令的操作对象。

## Linux 简单命令

### w 和 who 命令

二者都可查看服务器上目前已登陆的用户信息，区别是 `w` 命令除了能知道目前已登陆的用户信息，还可知道每个用户执行任务的情况。

`w` 命令基本格式：`$ w [选项] [用户名]`

- `-h` 不显示输出信息的标题
- `-s` 用简洁格式输出，不显示登陆时间，JCPU，PCPU
- 参数 传入用户名，表示只显示此用户的信息

``` bash
$ w
 21:19:52 up 28 min,  2 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
root     pts/2    -                21:02    5:01   0.03s   ?    -bash
d111kc   pts/1    -                20:49   30:08   0.01s  0.01s -bash
$ w -h
root     pts/2    -                21:02    5:09   0.03s   ?    -bash
d111kc   pts/1    -                20:49   30:16   0.01s  0.01s -bash
$ w -s
 21:20:03 up 28 min,  2 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM               IDLE WHAT
root     pts/2    -                 5:12  -bash
d111kc   pts/1    -                30:19  -bash
```

- USER 登录到系统的用户
- TTY 登录终端
- FROM 用户从哪里登录进来，一般显示远程登录主机的IP地址或主机名
- LOGIN@ 用户登录的时间
- IDLE 某个程序上次从终端开始执行到现在所持续的时间
- JCPU 和该终端连接的所有进程占用的CPU运算时间。这个时间里并不包括过去的后台作业时间，但是包括当前正在运行的后台作业所占用的时间
- PCPU 当前进程所占用的CPU运算时间
- WHAT：当前用户正在执行的进程名称和选项，换句话说，就是表示用户当前执行的是什么命令

`who` 命令基本格式：`$ who [选项] [file]`

`who` 命令只能显示当前登录的用户信息，但无法知晓每个用户正在执行的命令

- `-a` 列出所有信息
- `-b` 列出系统最近启动时间
- `-l` 列出所有可登录的终端信息
- `-s` 仅显示名称线路和时间字段信息，是 who 命令的默认选项
- 参数 若无指定文件，则 who 命令默认通过`/var/run/utmp` 文件来获取登陆用户信息

``` bash
$ who
d111kc   pts/1        2025-07-30 20:49
```

### echo 

可将命令行中的参数显示到标准输出（屏幕）上

命令格式：`$ echo [选项] [输出内容]` 

- `-n` 取消输出后行末的换行符号
- `-e` 支持使用转义字符

``` bash
d111kc@D111KC:~$ echo '1\n2'
1\n2
d111kc@D111KC:~$ echo -e '1\n2'
1
2
d111kc@D111KC:~$ echo -n 'hello'
hellod111kc@D111KC:~$
```

#### 转义字符

- `\\` 输出\本身
- `\a` 输出警告音
- `\b` 退格键，向左删除键
- `\c` 取消输出行末的换行符，和-n 一样
- `\e` Esc 键
- `\f` 换页符
- `\n` 换行符
- `\r` 回车键
- `\t` 制表符，就是 Tab 键
- `\v` 垂直制表符
- `\0nnn` 按八进制 ASCII 码表输出字符
- `\xhh` 按十六进制 ASCII 码表输出字符

### date 命令

显示或设定系统的日期与时间

``` bash
$ date
Wed Jul 30 22:01:25 CST 2025
```

### passwd 命令

密码配置指令

基本格式 `$ passwd [选项] [用户名]`

普通用户仅能修改自己的密码，root用户 可以修改自己和普通用户的密码。默认修改当前用户的密码。

``` bash
$ passwd
Changing password for d111kc.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

## 软件包

Linux 的软件包可细分为两种：源码包和二进制包

Linux 常用打包压缩格式“tar.gz”，因此源码包又被称为 Tarball，源码包常为 tar.gz 格式的压缩包，安装时还是要先将源码转换为二进制文件

两大主流的二进制包管理系统：RPM 包管理系统(Red Hat系列)，DPKG 包管理系统(Debian系列)

## 软件安装、运行与卸载

### RPM 包安装、卸载和升级

在 Linux 系统中，rpm 是 Red-Hat Package Manager（红帽包管理器） 的缩写，是一种用于管理软件包的工具和文件格式，主要应用于基于 Red Hat 架构的 Linux 发行版（如 CentOS、Fedora、RHEL 等）。

RPM二进制包的命名须遵守统一的命名规则，用户通过名称就可以直接获取这类包的版本、适用平台等信息。

RPM二进制包命名的一般格式如下：`包名-版本号-发布次数.发行商.Linux平台.适合的硬件平台.包扩展名`

例如，RPM包的全名是 `httpd-2.2.15-15.el6.centos.1.i686.rpm`

- httpd：软件包名。这里需要注意，httpd是包名，而httpd-2.2.15-15.el6.centos.1.i686.rpm通常称为包全名，包名和包全名是不同的，在某些Linux命令中，有些命令（如包的安装和升级）使用的是包全名，而有些命令（包的查询和卸载）使用的是包名，一不小心就会弄错。
- 2.2.15：包的版本号。版本号的格式通常为`主版本号.次版本号.修正号`
- 15：二进制包发布的次数，表示此RPM包是第几次编程生成的
- el6：软件发行商。el6表示此包是由RedHat公司发布的，适合在RHEL6.x和CentOS6.x上使用
- centos：此包适用于CentOS系统
- 6i686：此包使用的硬件平台。目前的RPM包支持的平台
- rpm：RPM包的扩展名。表明这是编译好的二进制包，可以使用rpm命令直接安装。此外，还有以src.rpm作为扩展名的RPM包，这表明是源代码包，需要安装生成源码，然后对其编译并生成rpm格式的包，最后才能使用rpm命令进行安装。

需要说明的是，Linux系统不靠扩展名区分文件类型，这里的扩展名是为系统管理员准备的，
如果不对RPM包标注扩展名，管理员很难知道这是一个RPM包，当然也就无法正确使用。

| 硬件平台 | 说明 |
| -------- | ---- |
| i386 | 386以上的计算机都可以安装 |
| i586 | 586以上的计算机都可以安装 |
| i686 | 奔腾Ⅱ以上的计算机都可以安装，目前所有的CPU都是奔腾Ⅱ以上的，所以这个软件版本居多 |
| X86_64 | 64位CPU可以安装 |
| noarch | 没有硬件限制 |

RPM 包默认安装路径，最好不要手动指定安装路径:

    /etc/
    /usr/bin/
    /usr/lib/
    /usr/share/doc/
    /usr/share/man/

RPM是通过本地的文件安装应用，并不是联网安装。

#### 安装RPM包

安装 RPM 包的命令格式：`$ rpm -ivh 包全名`

涉及包全名的命令，一定要注意路径。此命令中各选项参数的含义为：

- `-i` 安装（install）
- `-v` 显示更详细的信息（verbose）
- `-h` 打印，显示安装进度（hash）

命令还可以一次性安装多个软件包，仅需空格隔开，如下：`$ rpm -ivh a.rpm b.rpm c.rpm`

安装完成后，可尝试启动：`$ service 服务名 start |stop |restart |status`

各参数含义：启动服务|停止服务|重启|查看状态

#### 升级RPM包

RPM 包的升级：

- `$ rpm -Uvh 包全名`
- `$ rpm -Fvh 包全名`

-U 若该软件没安装过则直接安装，若已安装则升级至最新版本。
-F 若该软件没有安装，则不会安装，必须安装较低版本才能升级。

RPM 包的卸载要考虑包之间的依赖性，如先安装 httpd 软件包，后安装 httpd 的功能模块mod_ssl 包，那么卸载时，必须先卸载 mod_ssl 包，然后卸载 httpd，否则会报错

#### 卸载RPM包

卸载命令格式：`$ rpm -e 包名`

-e 卸载，erase，卸载命令支持“-nocteps”选项，既可以不检测依赖性直接卸载，但不推荐

#### 软件包的查询

RPM软件包做查询操作，具体包括：

- 查询软件包是否已安装。
- 查询系统中所有已安装的软件包。
- 查看软件包的详细信息。
- 查询软件包的文件列表。
- 查询某系统文件具体属于哪个RPM包

rpm查询命令语法 `$ rpm 选项 查询对象`

-q 包名 ，表示查询是否安装
-i 表示查询软件信息，information
-p 表示查询未安装的软件包，package
-l 表示列出软件包所有文件的安装目录
-f 查询文件所属那个软件包，file
-R 查询软件包的依赖关系，requires


`$ rpm -q 包名` 查询软件包是否安装

例如：查询是否安装了Apache服务

``` bash
$ rpm -q httpd
httpd-2.4.6-99.el7.centos.1.x86_64
```

`$ querry -qa` 查询所有已安装软件包，可以用管道符查找出需要的内容，如`$ rpm -qa | grep httpd`，采用这种方式可以找到含有httpd的所有软件包

`$ rpm -qi 包名` 查询软件包的详细信息

```
$ rpm -qi httpd
Name        : httpd
Version     : 2.4.6
Release     : 99.el7.centos.1
Architecture: x86_64
Install Date: 2025年07月22日 星期二 18时51分20秒
Group       : System Environment/Daemons
Size        : 9829328
License     : ASL 2.0
Signature   : RSA/SHA256, 2023年05月30日 星期二 23时15分45秒, Key ID 24c6a8a7f4a80eb5
Source RPM  : httpd-2.4.6-99.el7.centos.1.src.rpm
Build Date  : 2023年05月30日 星期二 22时02分56秒
Build Host  : x86-01.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
URL         : http://httpd.apache.org/
Summary     : Apache HTTP Server
Description :
The Apache HTTP Server is a powerful, efficient, and extensible
web server.
```

`$ rpm -qip 包全名` 查询未安装的软件包的详细信息。未安装的软件包需使用“包全名的绝对路径”的方式才能确定

`$ rpm -ql 包名` 查询已安装软件包中包含的所有文件及各自安装位置

`$ rpm -qlp 包全名` 未安装软件包中包含的所有文件以及打算安装的路径

`$ rpm -qf 系统文件名` 反向查询，查询文件属于哪个 RPM 软件包。只有使用 RPM 安装的文件才能使用该命令，手动方式建立的文件无法使用

例如：

``` bash
$ rpm -qf /bin/ls
coreutils-8.22-23.el7.x86_64
```

`$ rpm -qR 包名` 查询某已安装软件依赖的其他包

`$ rpm -qRp 包名` 查询某未安装软件依赖的其他包



