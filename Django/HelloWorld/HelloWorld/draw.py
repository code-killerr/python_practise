import turtle#海龟绘图,快捷使用代换 as t
import random
import time
def drawpicture():
    turtle.colormode(255)
    turtle.screensize(600,600,"gray")#宽高，背景色
    turtle.pensize(10)
    turtle.pencolor(random_color())
    turtle.fillcolor(random_color())
    turtle.speed(3)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(200)
        turtle.right(144)
        turtle.end_fill()
        time.sleep(2)
 
    turtle.penup()
    turtle.goto(-150,-120)
    turtle.color("violet")
    turtle.write("Done", font=('Arial', 40, 'normal'))
     
    turtle.mainloop()
    
    
    
# 获取随机颜色
def random_color():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)