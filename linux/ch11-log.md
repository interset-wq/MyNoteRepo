# 系统服务与日志

## Linux 系统服务

Linux系统服务有时也称为守护程序，是在Linux系统启动时自动加载并在Linux系统退出时自动停止的系统任务。常驻在内存中的进程，且可以提供一些系统或网络功能，就是服务（Service）。实现这个服务的程序就是守护程序（Daemon）。

Linux系统的大多数服务就是通过守护程序实现的。Linux系统中的服务数量非常多，在服务器上，安装Linux系统之后一步重要的工作就是服务优化，也就是关闭不需要的服务，只开启需要的服务。因为服务启动得越多，占用的系统资源就越多，而且被攻击的可能性也就越大。如果要进行服务优化，就需要知道这些服务都有什么作用，常见的守护程序包括系统日志进程sys-logd、Web服务器httpd、邮件服务器sendmail和数据库服务器mysqld等。

## 启动和关闭服务

如果依据守护程序的启动与管理方式来区分，基本上可以将守护程序分为可独立启动的服务（StandAlone）和通过一个总管程序（SuperDaemon）来统一管理的服务这两大类。

- StandAlone：此类型的守护程序可以自行启动而不必通过其他机制管理；守护程序启动并加载到内存后就一直占用内存与系统资源。因为一直存在内存中持续提供服务，因此响应速度较快。
- SuperDaemon：这一种启动方式是通过一个统一的守护程序来负责唤起系统，这个特殊的守护程序被称为SuperDaemon。当没有客户端请求时，各项服务都是未启动状态，等到有来自客户端的请求时，SuperDaemon才唤醒相对应的服务。当客户端请求结束后，被唤醒的这个服务也会关闭并释放系统资源。这种机制的好处是：由于SuperDaemon负责唤醒各项服务，因此SuperDaemon可以具有安全控管的机制，就是类似于网络防火墙的功能；由于服务在客户端的连接结束后就关闭，因此不会一直占用系统资源。但缺点就是服务的响应速度较慢。

独立的服务要想启动，主要有两种方法：

### 使用/etc/init.d/目录中的启动脚本来启动独立的服务

所有独立服务的启动脚本都存放在/etc/init.d/目录中，调用这些脚本就可以启动独立的服务了。这种启动方式是推荐启动方式，命令格式如下：

``` bash
$ /etc/init.d/独立服务名 start|stop|status|restart
```

参数：

- start：启动服务。
- stop：停止服务。
- status：查看服务状态。
- restart：重启服务

以httpd服务为例：

安装httpd：



启动httpd服务命令如下：

``` bash
$ /etc/init.d/httpd start
```

查询httpd服务状态，并能够看到httpd服务的PID：
[root@ localhost~]#/etc/init.d/httpd status
httpd（pid13313)
停止httpd服务：
[root@ localhost -]#/etc/init.d/httpd stop
重启httpd服务：
[root@ localhost]#/etc/init.d/httpd restartH


11.3 查看日志
1. 系统中绝大多数日志文件由 rsyslogd 服务 来统一管理
2. Apache 服务日志有 Apache 软件自己产生并记录，但其日志文件格式和系统默认
日志的格式是一致的。
1. /var/ 用来保存系统动态数据的目录，/var/log/目录 就是系统日志文件的保存位置。
11.4 管理日志
rsyslogd 服务依赖其配置文件 /etc/rsyslogd.conf 来确定各个服务不同等级的日志信息
会被记录的位置