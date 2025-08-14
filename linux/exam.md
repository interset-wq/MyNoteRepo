# 计算机三级Linux

一．填空题：（加粗的文字为该题的答案）

1. 在Linux系统中，以 文件 方式访问设备 。
2.Linux内核引导时，从文件 /etc/fstab 中读取要加载的文件系统。
3.Linux文件系统中每个文件用 i节点 来标识。
1. 全部磁盘块由四个部分组成，分别为引导块 、专用块 、i节点表块 和数据存储块。
2. 链接分为： 硬链接 和 符号链接 。
3. 超级块包含了i节点表 和 空闲块表 等重要的文件系统信息。
4. 某文件的权限为：drw-r--r--，用数值形式表示该权限，则该八进制数为： 644 ，该文件属性是 目录 。
5. 前台起动的进程使用 Ctrl+c 终止。
6. 静态路由设定后，若网络拓扑结构发生变化，需由系统管理员修改路由的设置。
7.  网络管理的重要任务是： 控制 和 监控 。
8.  安装Linux系统对硬盘分区时，必须有两种分区类型： 文件系统分区 和 交换分区 。
9.  编写的Shell程序运行前必须赋予该脚本文件 执行 权限。
10. 系统管理的任务之一是能够在 分布式 环境中实现对程序和数据的安全保护、备份、恢复和更新。
11. 系统交换分区是作为系统 虚拟存储器 的一块区域。
12. 内核分为 进程管理系统 、 内存管理系统 、 I/O管理系统 和文件管理系统 等四个子系统。
13. 内核配置是系统管理员在改变系统配置 硬件 时要进行的重要操作。
14. 在安装Linux系统中，使用netconfig程序对网络进行配置，该安装程序会一步步提示用户输入主机名、域名、域名服务器、IP地址、 网关地址 和 子网掩码 等必要信息。
15. 唯一标识每一个用户的是用户 ID 和用户名。
20.RIP 协议是最为普遍的一种内部协议，一般称为动态路由选择协议。
1.  在Linux系统中所有内容都被表示为文件，组织文件的各种方法称为 文件系统 。
22.DHCP可以实现动态 IP 地址分配。
1.  系统网络管理员的管理对象是服务器、 用户 和服务器的进程 以及系统的各种资源。
2.  网络管理通常由监测、传输和管理三部分组成，其中管理部分是整个网络管理的中心。
3.  当想删除本系统用不上的 设备驱动程序 时必须编译内核，当内核不支持系统上的设备驱动程序 时，必须对内核 升级 。
26Ping命令可以测试网络中本机系统是否能到达 一台远程主机 ，所以常常用于测试网络的 连通性 。
27.vi编辑器具有两种工作模式： 命令模式 和 输入模式 。 28. 可以用ls –al命令来观察文件的权限，每个文件的权限都用10位表示，并分为四段，其中第一段占 1 位，表示 文件类型 ，第二段占3位，表示 文件所有者 对该文件的权限。
1.  进程与程序的区别在于其动态性，动态的产生和终止，从产生到终止进程可以具有的基本状态为： 运行态 、 就绪态 和 等待态（阻塞态） 。
30.DNS实际上是分布在internet上的主机信息的数据库，其作用是实现 IP地址和主机名 之间的转换。
31.Apache是实现WWW服务器功能的应用程序，即通常所说的“浏览web服务器”，在服务器端 为用户提供浏览 web服务 的就是apache应用程序。
1.  在Linux系统上做备份可以有两种类型：系统备份 和 用户备份 。其中前者是指对 操作系统 的备份，后者是指对 应用程序和用户文件的备份。
33.CD-ROM标准的文件系统类型是 iso9660 。
1.  当lilo.conf配置完毕后，使之生效，应运行的命令及参数是 lilo 。
2.  在使用ls命令时，用八进制形式显示非打印字符应使用参数 -b 。
36.Linux使用支持Windows9.x/2000长文件名的文件系统的类型是 vfat 。
1.  设定限制用户使用磁盘空间的命令是 quota 。
38 在Linux系统中，用来存放系统所需要的配置文件和子目录的目录是 /etc 。
1.  硬连接只能建立对 文件 链接。符号链接可以跨不同文件系统创建
2.  套接字文件的属性位是 s 。
3.  结束后台进程的命令是 kill。
4.  进程的运行有两种方式，即 独立运行和使用父进程运行 。
43.Links分为 硬链接和符号链接 。
1.  在超级用户下显示Linux系统中正在运行的全部进程，应使用的命令及参数是 ps-aux 。
2.  管道文件的属性位是 p。
3.  将前一个命令的标准输出作为后一个命令的标准输入，称之为 管道 。
4.  为脚本程序指定执行权的命令及参数是 chmoda+xfilename 。
5.  进行远程登录的命令是 telnet 。
6.  欲发送10个分组报文测试与主机abc.tuu.edu.cn的连通性，应使用的命令和参数是：pingabc.tuu.edu.cn –c10 。
50.DNS服务器的进程命名为named，当其启动时，自动装载 /etc目录下的 named.conf文件中定义的DNS分区数据库文件。
51.Apache服务器进程配置文件是 httpd.conf 。
52.在 Linux系统中，压缩文件后生成后缀为.gz文件的命令是 gzip 。
1.  在用 vi编辑文件时，将文件内容存入 test.txt文件中，应在命令模式下键入 ：wtest.txt 。
54 可以在标准输出上显示整年日历的命令及参数是 cal-y 。
1.  在shell编程时，使用方括号表示测试条件的规则是：方括号两边必须有 空格 。
2.  检查已安装的文件系统/dev/had5是否正常，若检查有错，则自动修复，其命令及参数是 fsck –a/dev/had5 。
3.  在Windows9.x环境下共享Unix/Linux中的用户目录的一个工具是 Samba服务器 。
4.  系统管理员的职责是进行系统资源管理、系统性能管理、设备管理、安全管理和 系统性能监测 。
59 在Linux系统中，测试DNS服务器是否能够正确解析域名的的客户端命令，使用命令 nslookup 。
1.  在Linux系统下，第二个IDE通道的硬盘（从盘）被标识为 hdb。
2.  当系统管理员需升级内核版本和改变系统硬件配置时，应 重新编译内核 。
3.  如果只是要修改系统的IP地址，应修改 /etc/rc.d/rc.inet1 配置文件。
4.  当LAN内没有条件建立DNS服务器，但又想让局域网内的用户可以使用计算机名互相访问时，应配置 /etc/hosts 文件。
5.  在vi编辑环境下，使用 Esc键 进行模式转换。
65.SlackwareLinux9.0通常使用 ext3 文件系统，系统的全部磁盘块由 四 部分组成。
1.  将/home/stud1/wang目录做归档压缩，压缩后生成wang.tar.gz文件，并将此文件保存到/home目录下，实现此任务的tar命令格式 tarzcvf/home/wang.tar.gz/home/stud1/wang 。
2.  管道就是将前一个命令的 标准输出 作为后一个命令的 标准输入 。
3.  在使用手工的方法配置网络时，可通过修改 /etc/HOSTNAME 文件来改变主机名，若要配置该计算机的域名解析客户端，需配置 /etc/resolv.conf文件。
4.  启动进程有手动启动和调度启动两种方法，其中调度启动常用的命令为 at 、batch和 crontab 。
70.test.bns.com.cn的域名是 bns.com.cn ，如果要配置一域名服务器，应在 named.conf文件中定义DNS数据库的工作目录。
71.Sendmail邮件系统使用的两个主要协议是： SMTP 和 POP ，前者用来发送邮件,后者用来接收邮件。
72.DHCP是动态主机配置协议的简称，其作用是：为网络中的主机分配IP地址 。
1.  目前代理服务器使用的软件包有很多种，教材中使用的是 squid 。
74.rm命令可删除文件或目录，其主要差别就是是否使用递归开关 -r或-R 。
75.mv 命令可以移动文件和目录，还可以为文件和目录重新命名。
1.  路由选择协议（RIP）的跳数表示到达目的地之前必须通过的 网关 数，RIP接受的最长距离是 15跳 。
77.ping命令用于测试网络的连通性，ping命令通过 ICMP 协议来实现。
78.nfs 协议用于实现Unix（/linux）主机之间的文件系统共享。
1.  在Linux操作系统中，设备都是通过特殊的 文件 来访问。
80.shell不仅是 用户命令的解释器 ，它同时也是一种功能强大的编程语言。 bash是Linux的缺省shell。
1.  用 >;>; 符号将输出重定向内容附加在原文的后面。
2.  增加一个用户的命令是：adduser 或useradd 。
83 进行字符串查找，使用grep命令。
1.  使用 * 每次匹配若干个字符。
85./sbin 目录用来存放系统管理员使用的管理程序。
二．单项选择题:
1. 下面的网络协议中，面向连接的的协议是： A 。
A 传输控制协议 B 用户数据报协议 C 网际协议 D 网际控制报文协议
1. 在/etc/fstab文件中指定的文件系统加载参数中， D 参数一般用于CD-ROM等移动设备。
AdefaultsBswCrw和roDnoauto
3.Linux文件权限一共10位长度，分成四段，第三段表示的内容是 C 。
A 文件类型 B 文件所有者的权限 C 文件所有者所在组的权限 D 其他用户的权限
1. 终止一个前台进程可能用到的命令和操作 B 。
AkillB;+CCshutdownDhalt
5．在使用mkdir命令创建新的目录时，在其父目录不存在时先创建父目录的选项是 D 。
A-mB-dC-fD-p
1. 下面关于i节点描述错误的是 A 。
Ai节点和文件是一一对应的Bi节点能描述文件占用的块数Ci节点描述了文件大小和指向数据块的指针D 通过i节点实现文件的逻辑结构和物理结构的转换
1. 一个文件名字为rr.Z，可以用来解压缩的命令是： D 。
AtarBgzipCcompressDuncompress
1. 具有很多C语言的功能，又称过滤器的是 C 。
AcshBtcshCawkDsed
1. 一台主机要实现通过局域网与另一个局域网通信，需要做的工作是 C 。
A 配置域名服务器B 定义一条本机指向所在网络的路由C 定义一条本机指向所在网络网关的路由D 定义一条本机指向目标网络网关的路由
1.  建立动态路由需要用到的文件有 D 。
A/etc/hostsB/etc/HOSTNAMEC/etc/resolv.confD/etc/gateways
1.  局域网的网络地址 192.168.1.0/24，局域网络连接其它网络的网关地址是
192.168.1.1。主机192.168.1.20访问172.16.1.0/24网络时，其路由设置正确的是 B 。
Arouteadd –net192.168.1.0gw192.168.1.1netmask255.255.255.0metric1Brouteadd –net172.16.1.0gw192.168.1.1netmask255.255.255.255metric1Crouteadd –net172.16.1.0gw172.16.1.1netmask255.255.255.0metric1Drouteadddefault192.168.1.0netmask172.168.1.1metric1
1.  下列提法中，不属于ifconfig命令作用范围的是 D 。
A 配置本地回环地址 B 配置网卡的IP地址C 激活网络适配器 D 加载网卡到内核中
1.  下列关于链接描述，错误的是 B 。
A 硬链接就是让链接文件的i节点号指向被链接文件的i节点B 硬链接和符号连接都是产生一个新的i节点C 链接分为硬链接和符号链接 D 硬连接不能链接目录文件
1.  在局域网络内的某台主机用ping命令测试网络连接时发现网络内部的主机都可以连同，而不能与公网连通，问题可能是 C。
A 主机IP设置有误B 没有设置连接局域网的网关C 局域网的网关或主机的网关设置有误D 局域网DNS服务器设置有误
1.  下列文件中，包含了主机名到IP地址的映射关系的文件是： B 。
A/etc/HOSTNAMEB/etc/hostsC/etc/resolv.confD/etc/networks
1.  不需要编译内核的情况是 D 。
A 删除系统不用的设备驱动程序时 B 升级内核时C 添加新硬件时 D 将网卡激活
1.  在shell中变量的赋值有四种方法，其中，采用name=12的方法称 A 。
A 直接赋值 B使用read命令C 使用命令行参数 D使用命令的输出
18.D 命令可以从文本文件的每一行中截取指定内容的数据。
AcpBddCfmtDcut
1.  下列不是Linux系统进程类型的是 D 。
A 交互进程 B 批处理进程 C 守护进程 D 就绪进程
20．配置Apache1.3.19服务器需要修改的配置文件为___A______Ahttpd.confBaccess.confCsrm.confDnamed.conf
1.  内核不包括的子系统是 D 。
A 进程管理系统 B 内存管理系统 CI/O管理系统 D硬件管理系统
22． 在日常管理中，通常CPU会影响系统性能的情况是： A 。
ACPU已满负荷地运转 BCPU的运行效率为30%CCPU的运行效率为50%DCPU的运行效率为80%
23． 若一台计算机的内存为128MB，则交换分区的大小通常是 C 。
A64MBB128MBC256MBD512MB
24． 在安装Linux的过程中的第五步是让用户选择安装方式，如果用户希望安装部分组件（软件程序），并在选择好后让系统自动安装，应该选择的选项是 D 。
AfullBexpertCnewbieDmenu
25． Linux有三个查看文件的命令，若希望在查看文件内容过程中可以用光标上下移动来查看文件内容，应使用 C 命令。
AcatBmoreClessDmenu
26．下列信息是某系统用ps –ef命令列出的正在运行的进程，D 进程是运行Internet超级服务器，它负责监听Internetsockets上的连接，并调用合适的服务器来处理接收的信息。
Aroot14.00.0344204?S17:090:00initBroot20.00.129161520?S17:090:00/sbin/gettyCroot30.00.21364632?S17:090:00/usr/sbin/syslogdDroot40.013441204?S17:090:10/usr/sbin/inetd
27．在TCP/IP模型中，应用层包含了所有的高层协议，在下列的一些应用协议中， B是能够实现本地与远程主机之间的文件传输工作。
AtelnetBFTPCSNMPDNFS
28．当我们与某远程网络连接不上时，就需要跟踪路由查看，以便了解在网络的什么位置出现了问题，满足该目的的命令是 C 。
ApingBifconfigCtracerouteDnetstat
29．对名为fido的文件用chmod551fido 进行了修改，则它的许可权是 D 。
A-rwxr-xr-xB-rwxr--r--C-r--r--r--D-r-xr-x—x
30． 在i节点表中的磁盘地址表中，若一个文件的长度是从磁盘地址表的第1块到第
11块，则该文件共占有 B 块号。
A256B266C11D256×10
31． 用ls –al 命令列出下面的文件列表， D 文件是符号连接文件。
A-rw-rw-rw-2hel-susers56Sep0911:05helloB-rwxrwxrwx2hel-susers56Sep0911:05goodbeyCdrwxr--r--1helusers1024Sep1008:10zhangDlrwxr--r--1helusers2024Sep1208:12cheng
32． DNS域名系统主要负责主机名和 A 之间的解析。
AIP地址 BMAC地址 C 网络地址 D 主机别名
33． WWW服务器是在Internet上使用最为广泛，它采用的是 B 结构。
A 服务器/工作站 BB/SC 集中式 D 分布式
34．Linux系统通过 C 命令给其他用户发消息。
AlessBmesgyCwriteDechoto
35．NFS是 C 系统。
A 文件 B 磁盘 C 网络文件 D 操作
36． B 命令可以在Linux的安全系统中完成文件向磁带备份的工作。
AcpBtrCdirDcpio
37．Linux文件系统的文件都按其作用分门别类地放在相关的目录中，对于外部设备文件，一般应将其放在 C 目录中。
A/binB/etcC/devD/lib
38．在重新启动Linux系统的同时把内存中的信息写入硬盘，应使用 D 命令实现。
A#rebootB#haltC#rebootD#shutdown –rnow
39．网络管理具备以下几大功能：配置管理、 A 、性能管理、安全管理和计费管理等。
A 故障管理 B 日常备份管理 C 升级管理 D 发送邮件
40．关于代理服务器的论述，正确的是 A 。
A 使用internet上已有的公开代理服务器，只需配置客户端。
B 代理服务器只能代理客户端http的请求。
C 设置好的代理服务器可以被网络上任何主机使用。
D 使用代理服务器的客户端没有自己的ip地址。
41.关闭linux系统（不重新启动）可使用命令 B 。
ACtrl+Alt+DelBhaltCshutdown-rnowDreboot
42．实现从IP地址到以太网MAC地址转换的命令为： C 。
ApingBifconfigCarpDtraceroute
43．在vi编辑器中的命令模式下，键入 B 可在光标当前所在行下添加一新行。
A ＜a＞;B ＜o＞;C ＜I＞;D
44．在vi编辑器中的命令模式下，删除当前光标处的字符使用 A 命令。
A ＜x＞;B ＜d＞;＜w＞;C ＜D＞;D ＜d＞;＜d＞;
45．在vi编辑器中的命令模式下，重复上一次对编辑的文本进行的操作，可使用 C 命令。
A 上箭头 B 下箭头 C<.>;D<*>;
46．用命令 ls -al 显示出文件 ff的描述如下所示，由此可知文件 ff的类型为 A 。
-rwxr-xr--1rootroot599Cec1017:12ffA 普通文件 B 硬链接 C 目录 D 符号链接
47．删除文件命令为： D 。
AmkdirBrmdirCmvDrm
48．在下列的名称中，不属于DNS服务器类型的是：____C_____APrimaryMasterServerBSecondaryMasterServerCsambaDCache_onlyServer
49．网络管理员对WWW服务器进行访问、控制存取和运行等控制，这些控制可在 A文件中体现。
Ahttpd.confBlilo.confCinetd.confDresolv.conf
50．邮件转发代理也称邮件转发服务器，它可以使用SMTP协议，也可以使用 C 协议。
AFTPBTCPCUUCPDPOP
51．启动samba服务器进程，可以有两种方式：独立启动方式和父进程启动方式，其中前者是在 C 文件中以独立进程方式启动。
A/usr/sbin/smbdB/usr/sbin/nmbdCrc.sambaD/etc/inetd.conf
52．DHCP是动态主机配置协议的简称，其作用是可以使网络管理员通过一台服务器来管理一个网络系统，自动地为一个网络中的主机分配___D______地址。
A 网络 BMACCTCPDIP
53．为了保证在启动服务器时自动启动DHCP进程，应将 A文件中的dhcpd=no改为dhcpd=yes。
Arc.inet1Blilo.confCinetd.confDhttpd.conf
54．对文件进行归档的命令为 D 。
AddBcpioCgzipDtar
55．改变文件所有者的命令为 C 。
AchmodBtouchCchownDcat
56．在给定文件中查找与设定条件相符字符串的命令为： A 。
AgrepBgzipCfindDsort
57．建立一个新文件可以使用的命令为 D 。
AchmodBmoreCcpDtouch
58．在下列命令中，不能显示文本文件内容的命令是： D 。
AmoreBlessCtailDjoin
59．在使用匿名登录ftp时，用户名为 B 。
AusersBanonymousCrootDguest
60．在实际操作中，想了解命令logname 的用法，可以键入 D 得到帮助。
Alogname--manBlogname/？ ChelplognameDlogname--help
61．如果LILO被安装在MBR，使用 A 命令即可卸载LILO。
Alilo –uBlilo –cClilo –vDlilo-V
62．当用命令ls –al查看文件和目录时，欲观看卷过屏幕的内容，应使用组合键 D 。
AShift+HomeBCtrl+PgUpCAlt+PgDnDShift+PgUp
63．mc是UNIX风格操作系统的 C 。
A 文件编辑器/程序编译器 B 配置网络的窗口工具C 目录浏览器/文件管理器 DSamba服务器管理工具
64．i节点是一个 D 长的表，表中包含了文件的相关信息。
A8字节 B16字节 C32字节 D64字节
65．文件权限读、写、执行的三种标志符号依次是 A 。
ArwxBxrwCrdxDsrw
66．Linux 文件名的长度不得超过 C 个字符。
A64B128C256D512
67．进程有三种状态： C 。
A 准备态、执行态和退出态 B 精确态、模糊态和随机态C 运行态、就绪态和等待态 D 手工态、自动态和自由态
68． 从后台启动进程，应在命令的结尾加上符号 A 。
A&B@C#D$
69． B 不是邮件系统的组成部分。
A 用户代理 B 代理服务器 C 传输代理 D 投递代理
70．在Shell脚本中，用来读取文件内各个域的内容并将其赋值给Shell变量的命令是D 。
AfoldBjoinCtrDread
71．crontab文件由六个域组成，每个域之间用空格分割，其排列如下： B 。
AMINHOURDAYMONTHYEARCOMMANDBMINHOURDAYMONTHDAYOFWEEKCOMMANDCCOMMANDHOURDAYMONTHDAYOFWEEKDCOMMANDYEARMONTHDAYHOURMIN
72．用ftp进行文件传输时，有两种模式： C 。
AWord和binaryB.txt和WordDocumentCASCII和binaryDASCII和RichTextFormat
73．某文件的组外成员的权限为只读；所有者有全部权限；组内的权限为读与写，则该文件的权限为 D 。
A467B674C476D764
74．在DNS系统测试时，设named进程号是53，命令 D 通知进程重读配置文件。
Akill –USR253Bkill –USR153Ckill-INT63Dkill –HUP53
75．Apache服务器默认的接听连接端口号是 C 。
A1024B800C80D8
76．PHP和MySQL的联合使用解决了 C 。
A 在Proxy上处理数据库的访问问题 B 在WWW服务器上处理黑客的非法访问问题C 在WWW服务器上处理数据库的访问问题D 在Sendmail邮件系统上处理数据库的访问问题
77．OpenSSL是一个 A 。
A 加密软件 B 邮件系统 C 数据库管理系统 D 嵌入式脚本编程语言
78．Samba服务器的配置文件是 D 。
Ahttpd.confBinetd.confCrc.sambaDsmb.conf
79．关于DNS服务器，叙述正确的是 D 。
ADNS服务器配置不需要配置客户端B 建立某个分区的DNS服务器时只需要建立一个主DNS服务器C 主DNS服务器需要启动named进程，而辅DNS服务器不需要DDNS服务器的root.cache文件包含了根名字服务器的有关信息
80．退出交互模式的shell，应键入 C 。
A;B^qCexitDquit
81．将WindowsC:盘(hda1)安装在Linux文件系统的/winsys目录下，命令是 B 。
Aroot@l04.edu.cn:~#mountdev/had1/winsysBroot@l04.edu.cn:~#mount/dev/had1/winsysCroot@l04.edu.cn:~#mount/dev/had1winsysDroot@l04.edu.cn:~#mountdev/had1winsys
82．设超级用户root当前所在目录为：/usr/local，键入cd命令后，用户当前所在目录为 B 。
A/homeB/rootC/home/rootD/usr/local
83．字符设备文件类型的标志是 B 。
ApBcCsDl
84．将光盘CD-ROM（hdc）安装到文件系统的/mnt/cdrom目录下的命令是 C 。
Amount/mnt/cdromBmount/mnt/cdrom/dev/hdcCmount/dev/hdc/mnt/cdromDmount/dev/hdc
85．将光盘/dev/hdc卸载的命令是 A 。
Aumount/dev/hdcBunmount/dev/hdcCumount/mnt/cdrom/dev/hdcDunmount/mnt/cdrom/dev/hdc
86．在/home/stud1/wang目录下有一文件file，使用 D 可实现在后台执行命令，此命令将file文件中的内容输出到file.copy文件中。
Acatfile>;file.copyBcat>;file.copyCcatfilefile.copy&Dcatfile>;file.copy&
87．在DNS配置文件中，用于表示某主机别名的是： B 。
ANSBCNAMECNAMEDCN
88．可以完成主机名与IP地址的正向解析和反向解析任务的命令是： A 。
AnslookupBarpCifconfigDdnslook
89．下列变量名中有效的shell变量名是： C 。
A-2-timeB_2$3Ctrust_no_1D2004file
90．qmail是 B 。
A 收取邮件的协议 B 邮件服务器的一种 C 发送邮件的协议 D 邮件队列
91．已知某用户stud1，其用户目录为/home/stud1。如果当前目录为/home，进入目录/home/stud1/test的命令是 C 。
AcdtestBcd/stud1/testCcdstud1/testDcdhome
92．已知某用户stud1，其用户目录为/home/stud1。分页显示当前目录下的所有文件的文件或目录名、用户组、用户、文件大小、文件或目录权限、文件创建时间等信息的命令是D 。
Amorels –alBmore –allsCmore<ls –alDls –al|more
93．关于进程调度命令， B 是不正确的。
A 当日晚11点执行clear命令，使用at命令：at23:00todayclearB 每年1月1日早上6点执行date命令，使用at命令：at6amJan1dateC 每日晚11点执行date命令，crontab文件中应为：023***dateD 每小时执行一次clear命令，crontab文件中应为：0*/1***clear
94．系统中有用户user1和user2，同属于users组。在user1用户目录下有一文件file1，它拥有644的权限，如果user2用户想修改user1用户目录下的file1文件，应拥有 B 权限。
A744B664C646D746
95．如果想配置一台匿名ftp服务器，应修改 C 文件。
A/etc/gatewayB/etc/ftpserversC/etc/ftpusersD/etc/inetd.conf
96．Samba服务器的进程由B 两部分组成 。
Anamed和sendmailBsmbd和nmbdCbootp和dhcpdDhttpd和squid
97．要配置NFS服务器，在服务器端主要配置 C 文件。
A/etc/rc.d/rc.inet1B/etc/rc.d/rc.MC/etc/exportsD/etc/rc.d/rc.S
98．为保证在启动服务器时自动启动DHCP进程，应对 B 文件进行编辑。
A/etc/rc.d/rc.inet2B/etc/rc.d/rc.inet1C/etc/dhcpd.confD/etc/rc.d/rc.S
99．在配置代理服务器时，若设置代理服务器的工作缓存为64MB，配置行应为 D 。
Acache64MBBcache_dirufs/usr/local/squid/cache1000016256Ccache_mgr64MBDcache_mem64MB
100．安全管理涉及的问题包括保证网络管理工作可靠进行的安全问题和保护网络用户及网络管理对象问题。 C 属于安全管理的内容。
A 配置设备的工作参数 B 收集与网络性能有关的数据C 控制和维护访问权限 D 监测故障
101．以下命令对中，正确的是： B 。
Als和slBcat和tacCmore和eromDexit和tixe
102． B 命令是在vi编辑器中执行存盘退出。
A:qBZZC:q!D:WQ
103．下列关于/etc/fstab文件描述，正确的是 D 。
Afstab文件只能描述属于linux的文件系统 BCD_ROM和软盘必须是自动加载的Cfstab文件中描述的文件系统不能被卸载 D 启动时按fstab文件描述内容加载文件系统
104．通过文件名存取文件时，文件系统内部的操作过程是通过 C 。
A 文件在目录中查找文件数据存取位置。B 文件名直接找到文件的数据，进行存取操作。
C 文件名在目录中查找对应的I节点，通过I节点存取文件数据。
D 文件名在中查找对应的超级块，在超级块查找对应i节点，通过i节点存取文件数据
105．Linux将存储设备和输入/输出设备均看做文件来操作， C 不是以文件的形式出现。
A 目录 B 软链接 Ci节点表 D 网络适配器
106．关于i节点和超级块，下列论述不正确的是 B 。
Ai节点是一个长度固定的表 B 超级块在文件系统的个数是唯一的Ci节点包含了描述一个文件所必需的全部信息D 超级块记录了i节点表和空闲块表信息在磁盘中存放的位置
107． D 设备是字符设备。
AhdcBfd0Chda1Dtty1
108． B 目录存放着Linux的源代码。
A/etcB/usr/srcC/usrD/home
109．关于文件系统的安装和卸载，下面描述正确的是 A 。
A 如果光盘未经卸载，光驱是打不开的 B 安装文件系统的安装点只能是/mnt下C 不管光驱中是否有光盘，系统都可以安装CD-ROM设备Dmount/dev/fd0/floppy 此命令中目录/floppy是自动生成的
110． B 不是进程和程序的区别。
A 程序是一组有序的静态指令，进程是一次程序的执行过程B 程序只能在前台运行，而进程可以在前台或后台运行C 程序可以长期保存，进程是暂时的D 程序没有状态，而进程是有状态的
111．文件exer1的访问权限为rw-r--r--，现要增加所有用户的执行权限和同组用户的写权限，下列命令正确的是 A 。
Achmoda+xg+wexer1Bchmod765exer1Cchmodo+xexer1Dchmodg+wexer1
112．有关归档和压缩命令，下面描述正确的是 C 。
A 用uncompress命令解压缩由compress命令生成的后缀为.zip的压缩文件Bunzip命令和gzip命令可以解压缩相同类型的文件Ctar归档且压缩的文件可以由gzip命令解压缩Dtar命令归档后的文件也是一种压缩文件
113．不是shell具有的功能和特点的是 C 。
A 管道 B 输入输出重定向 C 执行后台进程 D 处理程序命令
114．下列对shell变量FRUIT操作，正确的是： C 。
A 为变量赋值：$FRUIT=appleB 显示变量的值：fruit=appleC 显示变量的值：echo$FRUITD 判断变量是否有值：[-f “$FRUIT” ]三．简答题：
1．简述Linux文件系统通过i节点把文件的逻辑结构和物理结构转换的工作过程。
参考答案：Linux通过i节点表将文件的逻辑结构和物理结构进行转换。
i 节点是一个64字节长的表，表中包含了文件的相关信息，其中有文件的大小、文件所有者、文件的存取许可方式以及文件的类型等重要信息。在i节点表中最重要 的内容是磁盘地址表。在磁盘地址表中有13个块号，文件将以块号在磁盘地址表中出现的顺序依次读取相应的块。Linux文件系统通过把i节点和文件名进行 连接，当需要读取该文件时，文件系统在当前目录表中查找该文件名对应的项，由此得到该文件相对应的i节点号，通过该i节点的磁盘地址表把分散存放的文件物 理块连接成文件的逻辑结构。
2．简述进程的启动、终止的方式以及如何进行进程的查看。
参考答案：在Linux中启动一个进程有手工启动和调度启动两种方式：（1）手工启动用户在输入端发出命令，直接启动一个进程的启动方式。可以分为：①前台启动：直接在SHELL中输入命令进行启动。
②后台启动：启动一个目前并不紧急的进程，如打印进程。
（2）调度启动系统管理员根据系统资源和进程占用资源的情况，事先进行调度安排，指定任务运行的时间和场合，到时候系统会自动完成该任务。
经常使用的进程调度命令为：at、batch、crontab。
1. 简述DNS进行域名解析的过程。
参考答案：首先，客户端发出DNS请求翻译IP地址或主机名。DNS服务器在收到客户机的请求后：（1）检查DNS服务器的缓存，若查到请求的地址或名字，即向客户机发出应答信息；（2）若没有查到，则在数据库中查找，若查到请求的地址或名字，即向客户机发出应答信息；（3）若没有查到，则将请求发给根域DNS服务器，并依序从根域查找顶级域，由顶级查找二级域，二级域查找三级，直至找到要解析的地址或名字，即向客户机所在网络的DNS服务器发出应答信息，DNS服务器收到应答后现在缓存中存储，然后，将解析结果发给客户机。
（4）若没有找到，则返回错误信息。
4．系统管理员的职责包括那些？管理的对象是什么？
参考答案：系统管理员的职责是进行系统资源管理、设备管理、系统性能管理、安全管理和系统性能监测。管理的对象是服务器、用户、服务器的进程及系统的各种资源等。
5．简述安装SlackwareLinux系统的过程。
参考答案：（1）对硬盘重新分区。 （2）启动Linux系统（用光盘、软盘等）。
（3）建立Linux主分区和交换分区。（4）用setup命令安装Linux系统。
（5）格式化Linux主分区和交换分区（6）安装Linux软件包（7）安装完毕，建立从硬盘启动Linux系统的LILO 启动程序，或者制作一张启动Linux系统的软盘。重新启动Linux系统。
6．什么是静态路由，其特点是什么？什么是动态路由，其特点是什么？
参考答案：静态路由是由系统管理员设计与构建的路由表规定的路由。适用于网关数量有限的场合，且网络拓朴结构不经常变化的网络。其缺点是不能动态地适用网络状况的变化，当网络状况变化后必须由网络管理员修改路由表。
动态路由是由路由选择协议而动态构建的，路由协议之间通过交换各自所拥有的路由信息实时更新路由表的内容。动态路由可以自动学习网络的拓朴结构，并更新路由表。其缺点是路由广播更新信息将占据大量的网络带宽。
87．进程的查看和调度分别使用什么命令？
参考答案：进程查看的命令是ps和top。
进程调度的命令有at，crontab，batch，kill。
8．当文件系统受到破坏时，如何检查和修复系统？
参考答案：成功修复文件系统的前提是要有两个以上的主文件系统，并保证在修复之前首先卸载将被修复的文件系统。
使 用命令fsck对受到破坏的文件系统进行修复。fsck检查文件系统分为5步，每一步检查系统不同部分的连接特性并对上一步进行验证和修改。在执行 fsck命令时，检查首先从超级块开始，然后是分配的磁盘块、路径名、目录的连接性、链接数目以及空闲块链表、i-node。
9．解释i节点在文件系统中的作用。
参考答案：在linux文件系统中，是以块为单位存储信息的，为了找到某一个文件在存储空间中存放的位置，用i节点对一个文件进行索引。I节点包含了描述一个文件所必须的全部信息。
所以i节点是文件系统管理的一个数据结构。
10．什么是符号链接，什么是硬链接？符号链接与硬链接的区别是什么？
参考答案：链接分硬链接和符号链接。
符号链接可以建立对于文件和目录的链接。符号链接可以跨文件系统，即可以跨磁盘分区。符号链接的文件类型位是l，链接文件具有新的i节点。
硬链接不可以跨文件系统。它只能建立对文件的链接，硬链接的文件类型位是－，且硬链接文件的i节点同被链接文件的i节点相同。
11．在对linux系统分区进行格式化时需要对磁盘簇（或i节点密度）的大小进行择，请说明选择的原则。
参考答案：磁盘簇（或i节点密度）是文件系统调度文件的基本单元。磁盘簇的大小，直接影响系统调度磁盘空间效率。当磁盘分区较大时，磁盘簇也应选得大些；当分区较小时，磁盘簇应选得小些。通常使用经验值。
12．简述网络文件系统NFS，并说明其作用。
参考答案：网络文件系统是应用层的一种应用服务，它主要应用于Linux和Linux系统、Linux和Unix系统之间的文件或目录的共享。对于用户而言可以通过 NFS方便的访问远地的文件系统，使之成为本地文件系统的一部分。采用NFS之后省去了登录的过程，方便了用户访问系统资源。
13．某/etc/fstab文件中的某行如下：/dev/had5/mnt/dosdatamsdosdefaults,usrquota12请解释其含义。
参考答案：（1）第一列：将被加载的文件系统名；（2）第二列：该文件系统的安装点；（3）第三列：文件系统的类型；（4）第四列：设置参数；（5）第五列：供备份程序确定上次备份距现在的天数；（6）第六列：在系统引导时检测文件系统的顺序。
14．Apache服务器的配置文件httpd.conf中有很多内容，请解释如下配置项：（1）MaxKeepAliveRequests200 （2）UserDirpublic_html（3）DefaultTypetext/plain （4）AddLanguareen.en（5）DocumentRoot“/usr/local/httpd/htdocs”
（6）AddTypeapplication/x-httpd-php.php.php.php4参考答案:（1）允许每次连接的最大请求数目，此为200；（2）设定用户放置网页的目录；（3）设置服务器对于不认识的文件类型的预设格式；（4）设置可传送语言的文件给浏览器；（5）该目录为Apache放置网页的地方；（6）服务器选择使用php4。
15．某Linux主机的/etc/rc.d/rc.inet1文件中有如下语句，请修正错误，并解释其内容。
/etc/rc.d/rc.inet1：……ROUTEadd –netdefaultgw192.168.0.101netmask255.255.0.0metric1ROUTEadd –net192.168.1.0gw192.168.0.250netmask255.255.0.0metric1参考答案:修正错误:（1）ROUTE应改为小写：route；（2）netmask255.255.0.0应改为:netmask 255.255.255.0；（3）缺省路由的子网掩码应改为:netmask0.0.0.0；（4）缺省路由必须在最后设定,否则其后的路由将无效。
解释内容:（1）route：建立静态路由表的命令；（2）add：增加一条新路由；（3）-net192.168.1.0：到达一个目标网络的网络地址；（4）default：建立一条缺省路由；（5）gw192.168.0.101：网关地址；（6）metric1：到达目标网络经过的路由器数（跳数）。
16．试解释apache服务器以下配置的含义：（1）port1080 （2）UserDiruserdoc（3）DocumentRoot “/home/htdocs”
（4）;OptionsIndexesFollowSymLinksAllowOverrideNoneOrderdeny,allowdenyfromallallowfrom192.168.1.5＜Directory＞;（5）ServerTypeStandlone参考答案：Apache服务器配置行含义如下：（1）将apache服务器的端口号设定为1080；（2）设定用户网页目录为userdoc；（3）设定apache服务器的网页根目录:/home/htdocs；（4）在此apache服务器上设定一个目录/home/htdocs/inside，且此目录只允许IP地址为192.168.1.5的主机访问；（5）定义apache服务器以独立进程的方式运行。
17．简述使用ftp进行文件传输时的两种登录方式？它们的区别是什么？常用的ftp文件传输命令是什么？
参考答案：（1）ftp有两种登录方式：匿名登录和授权登录。使用匿名登录时，用户名为：anonymous，密码为：任何合法email地址；使用授权登录时，用户名为用户在远程系统中的用户帐号，密码为用户在远程系统中的用户密码。
区别：使用匿名登录只能访问ftp目录下的资源，默认配置下只能下载；而授权登录访问的权限大于匿名登录，且上载、下载均可。
（2）ftp文件传输有两种文件传输模式：ASCII模式和binary模式。ASCII模式用来传输文本文件，其他文件的传输使用binary模式。
（3）常用的ftp文件传输命令为：bin、asc、put、get、mput、mget、prompt、bye。
四．编程与应用题：
1．用Shell编程，判断一文件是不是字符设备文件，如果是将其拷贝到 /dev 目录下。
参考程序：#!/bin/shFILENAME=echo“Inputfilename：”
readFILENAMEif[-c"$FILENAME"]thencp$FILENAME/dev fi
2．请下列shell程序加注释，并说明程序的功能和调用方法：#!/bin/sh#!/bin/sh# #/etc/rc.d/rc.httpd# #Start/stop/restarttheApachewebserver.
# #TomakeApachestartautomaticallyatboot,makethis#fileexecutable:chmod755/etc/rc.d/rc.httpd# case"$1"in 'start')
/usr/sbin/apachectlstart;;'stop') /usr/sbin/apachectlstop;;'restart') /usr/sbin/apachectlrestart;; *)
echo"usage$0start|stop|restart"
;; esac参考答案：（1）程序注释#!/bin/sh定义实用的shell# #/etc/rc.d/rc.httpd注释行，凡是以星号开始的行均为注释行。
# #Start/stop/restarttheApachewebserver.
# #TomakeApachestartautomaticallyatboot,makethis#fileexecutable:chmod755/etc/rc.d/rc.httpd# case"$1"in#case结构开始，判断“位置参数”决定执行的操作。本程序携带一个“位置参数”，即$1 'start')
#若位置参数为start /usr/sbin/apachectlstart;;#启动httpd进程 'stop')#若位置参数为stop/usr/sbin/apachectlstop;;#关闭httpd进程'restart')#若位置参数为stop /usr/sbin/apachectlrestart;;#重新启动httpd进程 *)#若位置参数不是start、stop或restart时echo"usage$0start|stop|restart";;#显示命令提示信息：程序的调用方法 esac#case结构结束（2）程序的功能是启动，停止或重新启动httpd进程（3）程序的调用方式有三种：启动，停止和重新启动。
3．设计一个shell程序，添加一个新组为class1，然后添加属于这个组的30个用户，用户名的形式为stdxx，其中xx从01到30。
参考答案：#!/bin/shi=1groupaddclass1while[$i-le30]do if[$i-le9];then USERNAME=stu0${i}else USERNAME=stu${i}fi useradd$USERNAMEmkdir/home/$USERNAMEchown-R$USERNAME/home/$USERNAMEchgrp-Rclass1/home/$USERNAMEi=$(($i+1)) done
4．编写shell程序，实现自动删除50个账号的功能。账号名为stud1至stud50。
参考程序：#!/bin/sh