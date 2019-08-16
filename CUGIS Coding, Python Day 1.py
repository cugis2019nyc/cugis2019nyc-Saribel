# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello World") #greeting
print("My name is Saribel")
print(6) 
5*2
5/2
5-2
5**2
8/9*3
def add(a,b):
    add= a+b
    print(add)
add(4,9)

def division(a,b):
    division= a/b
    print ("the answer is", division)
division(2,5)
def triangle(b,h):
    triangle= 1/2*b*h
    print("the area of the triangle with the base and height of", b,h, "would be", triangle)
triangle(4,6)
chocolate1 = "milk"
chocolate2 = "white"
chocolate3 = "dark"
milk = 5
white = 8
dark = 6

milk= milk+3
milk
milk=10
milk
import math
dir(math)
math.factorial(7)
math.sqrt(350)
math.exp(5)
math.exp(1)
math.pow(2.718281828459045,2)
math.pow(35,9)
35**9
math.pi
chocolate1= {"milk":5}
chocolate2= {"dark":6}
chocolate3= {"white":8}
chocolatebox = {"milk":5,"dark":6,"white":8}

student1 = ["Steve",32,"M"]
student2 = ["Lia",28,"F"]
student3 = ["Vin",45,"M"]
student4 = ["Katie",38,"F"]

student1[0]
student1[1]
student1[2]

print(student1, student2, student3, student4)

students =[student1, student2, student3, student4]
students
studentsinfo = [["Steve",32,"M"],["Lisa",28,"F"],["Vin",45,"M"],["Katie",38,"F"]]
import plotly
dir(pandas)
wodf = pd.read_ex

dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentsdf["name"], y=studentsdf["age"])
milk = 5
milk = {5:"chocolate"}

import pandas
dir ("pandas")

studentsdf = pandas.DataFrame(studentsinfo,columns=("Name","Age","Gender"))
studentsdf
studentsdf["Name"]
chocolate1 = ["milk",5]
chocolate2 = ["dark",6]
chocolate3 = ["white",8]
chocolatebox =[chocolate1,chocolate2,chocolate3]
chocolatebox
chocolateboxdf=pandas.DataFrame(chocolatebox,columns=("type","quality"))
chocolateboxdf

import plotly
dir ("plotly")
from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentsdf["Name"], y=studentsdf["Age"])
plot([studentbar])
wodf = pandas.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")

womenoccupation = go.Bar(x=wodf["occupation"], y=wodf["women"],
                         marker = {"color": wodf["women"],
                                   "colorscale":"Rainbow"})
plot([womenoccupation])
titles = go.Layout(title = "Percentage of Women Employed by Occupation",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                        )
                    ),
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                            )
                        ),
                    )
    plot([womenoccupation])
    
