from turtle import *
import turtle
import pandas as pd
import random
wn = turtle.Screen() #breaks without this, something to do with graphics yadayada

salaries = [random.randint(100,600) for i in range(4)] #yeah I could use a seed but it's funnier that it generates new salaries every time it's run
#karl_salary = int(input('Enter your salary: ')) <<<fun stuff that is too annoying to keep in :)
#salaries.append(karl_salary)

df = pd.DataFrame({'Name':['Mike','Randy','Carol','Karl'], 'Salary':salaries}) #some data
try:
    t = turtle.Turtle()
except:
    t = turtle.Turtle() #don't fully know why I have to do this but it's a solution to my Turtle window freezing up every second time I run it.

resetscreen
t.hideturtle()
t.speed(0) #zoom

def ChartSetup(): #check out this bs lmao. there MUST be a way of streamlining this process)
    t.penup()
    t.goto(-400,-300)
    t.pendown()
    t.pensize(5)
    t.forward(300)
    t.penup()
    t.right(90)
    t.forward(50)
    t.write('Weekly Salary', align='left')
    t.backward(50)
    t.left(90)
    t.pendown()
    t.forward(300)
    t.goto(-400,-300)
    t.left(90)
    t.forward(300)
    t.penup()
    t.left(90)
    t.forward(70)
    t.write('Employees', align='left')
    t.backward(70)
    t.right(90)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(-400,-320)
    t.right(90)
    t.write(0)
    for i in range(1,7): #writing ticks on xaxis
        t.forward(100)
        z=i*100
        t.write(z)
    t.penup()
    t.left(90)
    t.goto(-395,-295)
    t.pendown()
    t.pensize(1)
    t.right(90)
   
def nextrow():
    t.penup()
    t.back(100)
    t.pendown()

def bars():
    height = 50
    for index, row in df.iterrows():
        x = row['Name']
        i = row['Salary']
        t.forward(i)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(i)
        t.left(90)
        t.forward(height)
        t.write(x, False, align='left') #writing name of employee, I know it clips but it takes like 7 lines of code to fix it and cbb
        nextrow()
        t.left(90)

ChartSetup()
bars()
turtle.done()

from sys import platform
if platform=='win32':
    wn.exitonclick() #lets it exit turtle without crashing the kernel lol