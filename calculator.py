# Authors: Shichun Nie, Wenbo Li, Yvonne Li
# Assignment: Group Project
# Conmpleted(or last version): 12/05/2022

# How to run:
# ·Run our program in the compiler:
#     -Open calculator.py file in the compiler
#     -Click “Run”
# 
# ·Run our program as a small app:
#     -Open calculator.py file in the compiler
#     -Open Terminal and enter “pip” or “pip3” to check your computer has one of those commands.
#         if your computer does not have the command, then please check this url to install pip or pip3,
#         https://www.geeksforgeeks.org/how-to-install-pip-in-macos/
#     -Make sure the current path in the terminal is the path that the .py file is at and type those commands into terminal one by one.
#         $ pip(pip3) install pyinstaller
#         $ pyinstaller --onefile -w calculator.py (this is our python file)
#     -It will auto generate a folder called “dist”, find it and open it.
#     -Click the calculator.exe file. Then the program will be run as an app.
#



from tkinter import *
from tkinter import ttk
from math import pow
from math import sin
from math import cos
from math import tan
from math import pi
from math import e
from math import sinh
from math import cosh
from math import tanh
from math import log10
from math import log


MAX_SIZE = 64.0
MIN_SIZE = 1.0
INCREMENT = 2.0

COMPUTATION_DISTANCE = 0.001
ASYMPTOTE = 2.0

input = ""
view_size = 6.0    #quadrant size

def equal():
    global input

    try:
        total = str(eval(input))
        print_input("="+total)
        input = total

    except SyntaxError:
        print_error("Syntax Error")
        input = ''

    except ZeroDivisionError:
        print_error("ZeroDivisionError")
        input = ''


def print_input(pre_text):
    Label(root, text=input + pre_text, relief=RIDGE,
          width=10).grid(row=1, column=0, columnspan=5, sticky=W + E)

def print_error(input):
    Label(root, text= input,relief=RIDGE,
         width=10).grid(row=1, column=0, columnspan=5, sticky=W + E)


def translate(x_current, y_current):
    tc = [0, 0]
    x_mul = int(canvas["width"]) / (view_size * 2)
    y_mul = (int(canvas["height"]) / (view_size * -2))
    x_current = (x_current + view_size) * x_mul
    y_current = (y_current + view_size) * y_mul + int(canvas["height"])
    tc[0] = x_current
    tc[1] = y_current
    return tc


def line(x_from, y_from, x_to, y_to, colour):
    from_coord = translate(x_from, y_from)
    to_coord = translate(x_to, y_to)
    if y_to - y_from > view_size * ASYMPTOTE or y_from - y_to > view_size * ASYMPTOTE:
        from_coord = to_coord
    canvas.create_line(from_coord[0], from_coord[1], to_coord[0], to_coord[1], fill=colour)


def draw_grid():
    line(view_size, 1, 0, 1, "white")     #(1,0)
    line(-view_size, 1, 0, 1, "white")
    line(view_size, 2, 0, 2, "white")     #(2,0)
    line(-view_size, 2, 0, 2, "white")     #(2,0)
    line(view_size, 3, 0, 3, "white")     #(3,0)
    line(-view_size, 3, 0, 3, "white")     #(3,0)
    line(view_size, 4, 0, 4, "white")     #(4,0)
    line(-view_size, 4, 0, 4, "white")     #(4,0)
    line(view_size, 5, 0, 5, "white")     #(5,0)
    line(-view_size, 5, 0, 5, "white")     #(5,0)

    line(0, -1, view_size, -1, "white")     #(-1,0)
    line(0, -1, -view_size, -1, "white")
    line(0, -2, view_size, -2, "white")     #(-2,0)
    line(0, -2, -view_size, -2, "white")
    line(0, -3, view_size, -3, "white")     #(-3,0)
    line(0, -3, -view_size, -3, "white")
    line(0, -4, view_size, -4, "white")     #(-4,0)
    line(0, -4, -view_size, -4, "white")
    line(0, -5, view_size, -5, "white")     #(-5,0)
    line(0, -5, -view_size, -5, "white")


    line(1, view_size, 1, 0, "white")    #(0,1)
    line(1, -view_size, 1, 0, "white")    #(0,1)
    line(2, view_size, 2, 0, "white")    #(0,2)
    line(2, -view_size, 2, 0, "white")    #(0,2)
    line(3, view_size, 3, 0, "white")    #(0,3)
    line(3, -view_size, 3, 0, "white")    #(0,3)
    line(4, view_size, 4, 0, "white")    #(0,4)
    line(4, -view_size, 4, 0, "white")    #(0,4)
    line(5, view_size, 5, 0, "white")    #(0,5)
    line(5, -view_size, 5, 0, "white")    #(0,5)

    line(-1, 0, -1, view_size, "white")    #(0,-1)
    line(-1, 0, -1, -view_size, "white")    #(0,-1)
    line(-2, 0, -2, view_size, "white")    #(0,-2)
    line(-2, 0, -2, -view_size, "white")    #(0,-2)
    line(-3, 0, -3, view_size, "white")    #(0,-3)
    line(-3, 0, -3, -view_size, "white")    #(0,-3)
    line(-4, 0, -4, view_size, "white")    #(0,-4)
    line(-4, 0, -4, -view_size, "white")    #(0,-4)
    line(-5, 0, -5, view_size, "white")    #(0,-5)
    line(-5, 0, -5, -view_size, "white")    #(0,-5)

    line(view_size * -1, 0, view_size, 0, "black")
    line(0, view_size * -1, 0, view_size, "black")

def first_graph(event):
    canvas.delete("all")
    draw_grid()
    y_previous = 0.0
    x = view_size * -1
    print_input("Welcome")

def graph(event):

    canvas.delete("all")
    draw_grid()
    y_previous = 0.0
    x = view_size * -1
    while x <= view_size:
        try:
            y = eval(input)
        except ValueError:
            y = 1000000000
            x = COMPUTATION_DISTANCE * view_size
            if eval(input) < 0:
                y *= -1
        except:
            print_error("Syntax Error")
            break
        try:
            line(x - COMPUTATION_DISTANCE * view_size, y_previous, x, y, "blue")
        except:
            print_error("NON-INT PWR (dbl click ^)   ")
            break
        y_previous = y
        x += COMPUTATION_DISTANCE * view_size


def append(thing):
    global input
    if input.endswith('.') and thing == '.':
        input = input[:-1]
        input += ","
    else:
        input += thing
    print_input("")


def clear():
    global input
    while input != "":
        delete()
    print_input("")


def delete():
    global input
    input = input[:-1]
    print_input("")


def zoom_in():
    global view_size, btn_zoom_in, btn_zoom_out
    btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out())#.grid(row=9, column=3)
    if view_size > MIN_SIZE:
        view_size /= INCREMENT
        graph("event")
    if view_size == MIN_SIZE:
        btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in(), state=DISABLED)#.grid(row=9, column=2)
    graph(None)


def zoom_out():
    global view_size, btn_zoom_out, btn_zoom_in
    btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in())#.grid(row=9, column=2)
    if view_size < MAX_SIZE:
        view_size *= INCREMENT
        graph("event")
    if view_size == MAX_SIZE:
        btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out(),
                                  state=DISABLED)#.grid(row=9, column=3)
    graph(None)


def correct_ending_no_number(name):
    return name.endswith('x') or name.endswith('e') or (name.endswith('i') and name[-2:] != "si") or name.endswith(')')


def correct_ending(thing):
    return thing[-1:].isdigit() or correct_ending_no_number(thing)


def append_implicit(thing):
    global input
    if correct_ending(input):
        if thing == "**":
            input += thing
        else:
            input += "*" + thing
    elif input[-2:] == "**" and thing == "**":
        input = input[:-2]
        if correct_ending(input):
            input += "*pow(x,"
        else:
            input += "pow(x,"
    else:
        input += thing
    print_input("")


def append_number(thing):
    global input
    if correct_ending_no_number(input) and thing.isdigit():
        input += "*"
    input += thing
    print_input("")


def append_closing_parentheses_input(thing):
    global input
    if correct_ending(input) and thing == '(':
        input += "*"
    input += thing
    print_input("")


root = Tk()

root.wm_title("Graphing Scientific Calculator")
root.resizable(width=None, height=None)


canvas = Canvas(root)

print_input("")

ttk.Button(root, text="0", command=lambda: append_number("0")).grid(row=6, column=0)
ttk.Button(root, text="1", command=lambda: append_number("1")).grid(row=6, column=1)
ttk.Button(root, text="2", command=lambda: append_number("2")).grid(row=6, column=2)
ttk.Button(root, text="3", command=lambda: append_number("3")).grid(row=6, column=3)
ttk.Button(root, text="4", command=lambda: append_number("4")).grid(row=6, column=4)

ttk.Button(root, text="5", command=lambda: append_number("5")).grid(row=7, column=0)
ttk.Button(root, text="6", command=lambda: append_number("6")).grid(row=7, column=1)
ttk.Button(root, text="7", command=lambda: append_number("7")).grid(row=7, column=2)
ttk.Button(root, text="8", command=lambda: append_number("8")).grid(row=7, column=3)
ttk.Button(root, text="9", command=lambda: append_number("9")).grid(row=7, column=4)

ttk.Button(root, text="sin", command=lambda: append_implicit("sin(")).grid(row=2, column=0)
ttk.Button(root, text="cos", command=lambda: append_implicit("cos(")).grid(row=2, column=1)
ttk.Button(root, text="tan", command=lambda: append_implicit("tan(")).grid(row=2, column=2)
ttk.Button(root, text="π", command=lambda: append_implicit("pi")).grid(row=2, column=3)
ttk.Button(root, text="e", command=lambda: append_implicit("e")).grid(row=2, column=4)

ttk.Button(root, text="sinh", command=lambda: append_implicit("sinh(")).grid(row=3, column=0)
ttk.Button(root, text="cosh", command=lambda: append_implicit("cosh(")).grid(row=3, column=1)
ttk.Button(root, text="tanh", command=lambda: append_implicit("tanh(")).grid(row=3, column=2)
ttk.Button(root, text="log", command=lambda: append_implicit("log10(")).grid(row=3, column=3)
ttk.Button(root, text="ln", command=lambda: append_implicit("log(")).grid(row=3, column=4)

ttk.Button(root, text="+", command=lambda: append("+")).grid(row=5, column=0)
ttk.Button(root, text="-", command=lambda: append("-")).grid(row=5, column=1)
ttk.Button(root, text="*", command=lambda: append("*")).grid(row=5, column=2)
ttk.Button(root, text="/", command=lambda: append("/")).grid(row=5, column=3)
ttk.Button(root, text="^", command=lambda: append_implicit("**")).grid(row=5, column=4)

ttk.Button(root, text="(", command=lambda: append_closing_parentheses_input("(")).grid(row=4, column=0)
ttk.Button(root, text=")", command=lambda: append(")")).grid(row=4, column=1)
ttk.Button(root, text=".", command=lambda: append(".")).grid(row=4, column=2)
ttk.Button(root, text="\u221ax", command=lambda: append_implicit("*0.5")).grid(row=4, column=4)

ttk.Button(root, text="Delete", command=lambda: delete()).grid(row=8, column=0)
ttk.Button(root, text="Clear", command=lambda: clear()).grid(row=9, column=0)

ttk.Button(root, text="=", command=lambda: equal()).grid(row=8, column=3)

ttk.Button(root, text="x", command=lambda: append_implicit("x")).grid(row=4, column=3)
btn_enter = ttk.Button(root, text="Graph")
btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in()).grid(row=9, column=2)
btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out()).grid(row=9, column=3)
ttk.Button(root, text="Exit App", command=lambda: exit(0)).grid(row=9, column=4)

btn_enter.bind('<Button-1>', graph)

btn_enter.grid(row=8, column=2)
canvas.grid(row=0, column=0, columnspan=5)

draw_grid()
first = True
if first:
    first_graph(None)
    first = False
else:
    graph("event")

root.mainloop()
