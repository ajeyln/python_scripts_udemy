from turtle import *
import time
import webbrowser

forward(150)
left(150)
forward(150)
right(150)
circle(150)
time.sleep(2)

# to open any url using python
#webbrowser.open("https://github.com/ajeyanayk")

# if we want to open URL using mozilla firefox
chrome = webbrowser.get('chrome %s').open("https://github.com/ajeyanayk/")