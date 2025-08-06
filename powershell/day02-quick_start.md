# DAY 2 初识PowerShell

在32位操作系统x86中，最多只有两个powershell图标，分别是

- Windows PowerShell 32位控制台
- Windows PowerShell ISE 32位图形化控制台

在64位操作系统x64中，最多有4个powershell图标，分别是

- Windows PowerShell 64位和32位控制台
- Windows PowerShell ISE 64位和32位图形化控制台
- Windows PowerShell(x86) 64位系统上的32位控制台
- Windows PowerShell ISE(x86) 34位系统上的32位图形化控制台

即32位操作系统仅有32位的powershell，而64位操作系统可以同时有32位和64位两个版本的powershell，32位版本的会在末尾注明 `(x86)`

## 通过终端powershell控制台打开ISE

``` powershell
PS C:\Users\86183> ise
```

回车之后会自动打开集成脚本环境（Windows PowerShell ISE）

## 四种方式的Tab键补全

PowerShell控制台和集成脚本环境（ISE）都支持4中Tab补全以减少输入错误：

- 补全命令：输入 `Get-S`，通过Tab键，或shift+tab组合键可以循环显示以 `Get-S` 开头的命令
- 补全路径：输入 `Dir`，按空格，输入 `C:\`，再按Tab，会补全该目录内文件或目录的路径
- 补全选项：输入 `Dir -`，按Tab键，循环显示这个命令支持的选项
- 补全参数：在补全选项的基础上，再输入一个空格，通过按Tab键，可以循环显示这个命令的参数的合法值。这种情况下的tab补全只对预设了可用值的参数有效

ISE在支持Tab补全的基础上还支持智能提示。通过上下箭头可以滚动菜单，按tab键或回车确认选择