# 网络管理
10.1 管理网络接口
计算机的基本网络参数包括那些？
1） IP 地址：一个 IP 地址标识一块网卡接口，主要有网络号和主机号组成。
2） 子网掩码：IP 地址必须和子网掩码成对出现，子网掩码用来确定网络部分的位数，在
IP 地址中对应子网掩码为 1 的位为网络部分。
3） 网关：网关的功能是跨区域通信。
4） DNS：DNS 将域名和 IP 进行映射。
1. 用 Linux 作为联网机器
1.1 为每个网络接口分配一个适当的 IP 地址和子网掩码（Netmask）；
1.2 配置默认网关（Gateway）
1.3 配置一个或一个以上的 DNS 服务器
2. 网络接口卡（Network Interface Card，NIC）
联网操作是通过机器上的 PCI（Peripheral Component Interconnect）设备，即网络接口卡
来实现。Linux 内核可以检测出所有连接的 PCI 设备，同时使用 lspci 命令可验证给出的 PCI
设备是否能被内核检测到。
3. 网络接口
Linux 内核不允许用户将 NIC 作为文件进行访问。在/dev 目录下没有直接关联 NIC 的设备
节点，但有相应的硬盘和声卡设备节点
Linux 系统通过网络接口访问 NIC，常用 Linux 接口名称和类型：
名称 类型
eth0 以太网
lo （虚拟）回环设备
ppp0 使用 PPP 协议的串口设备（调制解调器）
tr0 令牌环（token ring）
fddi0 光纤
4. 用 ifconfig -a 检测接口
ifconfig -a 命令可检测所有目前已识别的网络接口信息
ifconfig 命令不加选项，就只能报告活跃的网络接口。
5. 用 ifconfig 命令配置网络接口
ifconfig 查看相关网卡信息
6. 接口配置文件
linux 接口激活----/etc/init.d/network
linux 接口配置文件----/etc/sysconfig/network-scripts
Linux 系统采用更普遍的方法来配置网络接口，即根据目录/etc/sysconfig/network-scripts/
中 以 ifcfg-<interface> 形 式 命 名 的 配 置 文 件 来 配 置 网 络 接 口 ， 例 如 ，
/etc/sysconfig/network-scripts/ifcfg-eth0
习惯上分配给回环接口的 IP 地址和子网掩码是 127.0.0.1/255.0.0.0。
10.2 基本 IP 路由和网关
1. IP 网络 每个 IP 地址包括两个部分：网络部分和主机部分。
子网掩码的网络定义为 A 类 B 类和 C 类网络，网络地址分别对应为包含第 1 个 IP 字段，
后面 3 个 0：255.0.0.0；前两个网络地址字段：255.255.0.0；前 3 个：255.255.255.0。
2. 以太网硬件（物理）地址
每个以太网接口的地址有两个，IP 地址，硬件（MAC）地址。IP 地址用于两台主机间的
通信，MAC 地址用于同一 IP 网络中不同主机间的通信。
3. 在本地网络中与其他机器通信
过程：确认通向同一网络地址；确定目的机器的硬件地址，使用本地网络的底层 ARP 协
议（Address Resolution Protocol，地址解析协议）验证；
源机器会将找到的目的及其保留 IP 地址/MAC 地址对，即 APR 缓存。可用 arp -a 命令来
检测缓存。arp -n : 查看 ip 地址与 mac 地址的映射表
用来将以太网 MAC 地址和一个 IP 地址关联起来的网络协议是 ARP。
10.3 配置 DNS 客户机
1. 域名系统 DNS
1）将 IP 地址与主机名对应起来的表。只要输入一个主机的名字，计算机系统就会自动的
将这个名字转换成计算机了解的 IP 地址，这也是 Linux 系统中/etc/hosts 文件的由来
2）DNS 是域名系统（Domain Name System）分布式数据库，作用是使复杂难记的 IP 地址
转换成简明易记的域名，实现 主机名 与 IP 地址 的转换，在 TCP/IP 网络中有非常重要的地
位。
2. 静态查询：/etc/hosts
3. 动态查询：/etc/resolv.conf
Linux 应用程序使用通用架构来解析主机名，即 resolve 库。当解析一个主机名时，resolve
库首先试图执行静态查询；接下来 resolve 库将试着通过咨询/etc/resolv.conf 配置文件中列
出的域名服务器来进行动态查询。
10.4 DHCP 配置详解
DHCP（Dynamic Host Configuration Protocol，动态主机配置协议）是一种网络管理协议。
通过 DHCP 获得信息的机器没有固定的 IP 地址，相反，每当增加一个接口时（用 ifup 命令）
都动态地获得一个 IP 地址，每当减少一个接口时（用 ifdown 命令）就释放一个 IP 地址。
为将一台机器当作 DHCP 客户机使用，在接口配置文件中将 BOOTPROTO 变量设为 dhcp。
当使用 DHCP 配置接口时，dhclient 守护进程会自动启动来管理 DHCP 通信。所有这些由
dhclient 守护进程接收到的信息都会立即得到应用。默认网关会添加到路由表中，域名服
务器会写入/etc/resolv.conf 文件，同时 NIS 域（Network Information Service，网络信息服
务）也会自动设定
10.5 配置 Web 服务器
HTTP 协议的全称是 Hyper Text Transfer Protocol（超文本传输协议），他是起什么作用的协
议?
HTTP 协议与 TCP/IP 协议族内的其他众多协议相同，用于客户端和服务器之间的通信。
Apache 是实现 WWW 服务器功能的应用程序，通常所说的“浏览 Web 服务器”，在 服务器
端 为用户提供浏览 Web 服务 的就是 Apache 应用程序。
10.6 配置 Telnet
常用的远程控制 Web 服务器的方法
10.7 其他网络设置
1. 分配主机名
hostname 命令，可以检验机器的主机名，还可动态分配主机名。
2. /etc/sysconfig/network 文件
记录通用联网配置信息，可用来定义整合到启动过程中的 shell 变量。
3.将网络配置视为 service
网络配置可用 service 服务来管理，service network stop。。。
10.8 网络诊断工具
1.ping、host 和 traceroute 命令
1）ping 命令
可以测试网络中本机系统是否能到达 一台远程主机 ，用来测试两台机器间底层 IP 连接性
（连通性）的。最简单的情况，ping 命令接受一个主机名或者 IP 地址作为其单一参数。
2）host 命令
用来直接执行 DNS 查询。最简单的情况，只使用一个主机名作为参数，这时 host 命令会
使用在/etc/resolv.conf 配置文件中定义的域名服务器进行 DNS 查询。
3）traceroute 命令
为数据包在路由器间穿行并最终到达目的地路径提供了详尽的说明。
2.诊断网络配置问题
3.用 tcpdump 命令检测网络活性
用来直接监视网络，显示独立数据包的信息概要。会一直执行，直到 Ctrl+C 组合键取消这
个命令。
1）可列出所有当前活跃的网络接口的命令是：ifconfig。
3）习惯上分配给回环接口的 IP 地址和子网掩码是：127.0.0.1/255.255.0.0
4）定义本地主机名和 IP 地址间转换的文件是：/etc/hosts
5）可将 Linux 内核的主机名设置为 station=.example.com 的命令是
hostname station.example.com
6） 可准确定义 Linux 内核的主机名，并使其在启动时被动设定的文件是 /etc/hosts
7）可启用安装了红帽 Linux 系统的机器，使其充当路由器角色的文件是： /etc/syscfl.conf
/etc/sysctl.conf 这个文件是用来在 Linux 中开启路由功能的配置文件（这个配置文件是个
内核的配置文件，主要用来修改内核的参数，随系统重新启动而启动一些功能）
8）在适当的文件中，用来启用路由功能的参数名称是：net.ipv4.ip_forward；
https://blog.csdn.net/han156/article/details/77924734
9）用来直接执行 DNS 主机名解析的程序是：system-config-network-tui
10）用来截取使用 HTTP 协议（端口 80）的网页浏览器和网页服务器间数据传输的命令是，
只在端口 80 将数据传送给网页服务器，并将传输记录用二进制格式保存在文件
http.capture 中：tcpdump-p 80>http.capture
11）Linux 网络接口配置文件名都以 ifcfg 为前缀，文件中变量 DEVICE 用来定义该文件含
有哪个接口的配置信息
12 ） ifconfig 可 以 配 置 网 卡 的 Ip 地 址 等 参 数 ， 这 与 修 改 配 置 文 件 有 什 么 差 别 ？
ifconfig 暂时改变网络参数,并不写入配置文件，因此当计算机重新启动后,还是从配置
文件中设置网络参数。
net.ipv4.ip_forward = 0 进入这个配置文件找到第七行 ，把这个 0 改为 1 就等于开启了路
由功能。
net.ipv4.ip_forward = 1 说明 Linux 开启了路由转发功能