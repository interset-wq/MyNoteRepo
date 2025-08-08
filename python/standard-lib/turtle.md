---
title: turtle
subtitle: 海龟绘图, 海龟的爬行足迹
---

[turtle官方文档](https://docs.python.org/zh-cn/3.13/library/turtle.html#module-turtle)

## 导入

    import turtle as t

## 海龟移动和方向

海龟的起始位置是坐标原点, 数学平面直角坐标系. 海龟在图形中用三角箭头表示, 箭头的指向就是海龟前进的方向

- `t.forward(distance)` 函数 传入数字float类型,单位是像素 海龟前进(海龟的初始方向是X轴正方向)
- `t.backward(distance)` 函数 传入数字float类型,单位是像素 海龟后退
- `t.left(angle)` 函数 传入数字float类型,单位角度 海龟朝逆时针方向转向
- `t.right(angle)` 函数 传入数字float类型,单位角度 海龟朝顺时针方向转向
- `t.color()` 传入表示颜色的字符串，切换爬行路径的颜色
- `t.width()` 传入整数，调整线宽
- `t.up()` 抬起画笔，不绘制路径
- `t.down()` 放下画笔，继续绘制路径
- `t.home()` 走直线回到起点
- `t.pos()` 返回当前位置的坐标
- `t.clearscreen()` 清空足迹，回到起点
- `t.fillcolor()` 传入颜色，设置填充色
- `t.begin_fill()` 开始使用填充色
- `t.end_fill()` 结束使用填充色