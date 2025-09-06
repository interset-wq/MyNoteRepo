"""绘制一系列正五边形"""

import turtle as t
color = ['red','green','blue','orange','pink']
for i in range(len(color)):
    t.penup()
    t.goto(-200 + 70*i, 0)
    t.pendown()
    t.pencolor(color[i])
    t.circle(50, steps = 5)
t.done()