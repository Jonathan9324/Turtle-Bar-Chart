from turtle import *
import turtle
import pandas as pd
import random
wn = turtle.Screen() #breaks without this, something to do with graphics yadayada

turtle.screensize()


salaries = [random.randint(100,600) for i in range(7)] #yeah I could use a seed but it's funnier that it generates new salaries every time it's run
#karl_salary = int(input('Enter your salary: ')) <<<fun stuff that is too annoying to keep in :)
#salaries.append(karl_salary)

df = pd.DataFrame({'Name':['Mike','Randy','Carol','Karl','Julia','Jess','Lucas'], 'Salary':salaries}) #some data
try:
    t = turtle.Turtle()
except:
    t = turtle.Turtle() #don't fully know why I have to do this but it's a solution to my Turtle window freezing up every second time I run it.

resetscreen
t.hideturtle()
t.speed(0) #zoom

def ChartSetup(x,y): #check out this bs lmao. there MUST be a way of streamlining this process)
    clearscreen() #resets screen,
    wnh = turtle.window_height()
    wnw = turtle.window_width()
    turtle.setworldcoordinates(0,-50,wnw,wnh)
    wn.onscreenclick(ChartSetup) #below code redraws axis lines scaled to new screen size.
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.pensize(5)
    wnw=wnw*.97 #creates padding on right side.
    t.forward(wnw/2)
    t.penup()
    t.right(90)
    t.forward(40)
    t.write('Weekly Salary', align='left')
    t.backward(40)
    t.left(90)
    t.pendown()
    t.forward(wnw/2)
    t.goto(-0,-0)
    t.left(90)
    t.forward(wnh/2)
    t.penup()
    t.left(90)
    t.forward(70)
    t.write('Employees', align='left')
    t.backward(70)
    t.right(90)
    t.pendown()
    t.forward(wnh/2)
    t.penup()
    t.goto(-0,-25)
    t.right(90)
    t.write(0)
    for i in range(1,7): #writing ticks on xaxis, scaling to window size.
        t.forward(wnw/len(range(1,7)))
        t.write(i*100)
    t.penup()
    t.left(90)
    t.goto(-395,-295)
    t.pendown()
    t.pensize(1)
    t.right(90)
    bars()
   
def nextrow():
    wnh = turtle.window_height() #couldn't figure out global and was in hurry xx
    wnw = turtle.window_width()
    t.penup()
    t.back(wnh/len(df))
    t.pendown()

def bars():
    t.penup()
    t.goto(0,0)
    t.pendown()
    wnh = turtle.window_height() #couldn't figure out global and was in hurry xx
    wnw = turtle.window_width()
    col = ['red', 'yellow', 'green', 'blue','cyan', 'orange', 'pink'] 
    height = wnh/len(df)
    for index, row in df.iterrows():
        x = row['Name']
        i = row['Salary']
        t.fillcolor(col[index])
        t.begin_fill()
        t.forward(wnw/i *100)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(wnw/i *100)
        t.left(90)
        t.forward(height)
        t.write(x, False, align='left') #writing name of employee, I know it clips but it takes like 7 lines of code to fix it and cbb
        t.end_fill()
        nextrow()
        t.left(90)


ChartSetup(0,0)
bars()
#turtle.onscreenclick(ChartSetup)
col = ['red', 'yellow', 'green', 'blue', 
       'white', 'black', 'orange', 'pink'] 

wnh = turtle.window_height()
wnw = turtle.window_width()
# call method on screen click 
if turtle.window_height()+turtle.window_width() != wnh+wnw:
    ChartSetup(0,0)

wn.onscreenclick(ChartSetup)
turtle.done()


from sys import platform
if platform=='win32':
    wn.exitonclick() #lets it exit turtle without crashing the kernel lol