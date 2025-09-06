import turtle as t 

print(t.pos()) # (0.00,0.00)
t.forward(100)
t.clearscreen()
t.right(120)
t.forward(1000)
t.home()
t.forward(200)
print(t.pos()) # (200.00,0.00)
t.mainloop()