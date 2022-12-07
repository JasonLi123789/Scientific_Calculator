# Authors: Shichun Nie, Wenbo Li, Yvonne Li
# Assignment: Group Project
# Conmpleted(or last version): 12/05/2022

def equal():
    global formula

    try:

        total = str(eval(formula))

        print_formula(total)

        formula = total

    except SyntaxError:

        print_formula("SyntaxError")

        formula = ''

    except ZeroDivisionError:

        print_formula("ZeroDivisionError")

        formula = ''



Button1 = Button(Frame, text=1, width=5, height=4, font=30, command=lambda: clickbutton(1))
Button1.grid(row=2, column=0)
Button2 = Button(Frame, text=2, width=5, height=4, font=30, command=lambda: clickbutton(2))
Button2.grid(row=2, column=1)
Button3 = Button(Frame, text=3, width=5, height=4, font=30, command=lambda: clickbutton(3))
Button3.grid(row=2, column=2)
Minus = Button(Frame, text='-', width=5, height=4, font=30, command=lambda: clickbutton('-'))
Minus.grid(row=2, column=4)