from tkinter import *
from func import cFrame, ico

default_fig = 'x'


def switch_turn():
    global default_fig
    if default_fig == 'x':
        default_fig = 'o'
        ico(gui, 'x')
        return default_fig
    elif default_fig == 'o':
        default_fig = 'x'
        ico(gui, 'o')
        return default_fig


def update_score(event):
    print(default_fig)
    if str(event.widget) == ".!cframe.!canvas":
        if default_fig == 'x':
            sc.destroy()
            sco = canvas.score(gui, 'x')
            sco.grid(column=0, row=0)
        elif default_fig == 'o':
            sc.destroy()
            sco = canvas.score(gui, 'o')
            sco.grid(column=0, row=0)


def action(event):
    x = event.x
    y = event.y
    if str(event.widget) == ".!cframe.!canvas":
        if 129 >= y > 0:
            if 129 > x > 0:
                if canvas.empty_section(0) is True:
                    figure = switch_turn()
                    canvas.figures(0, figure)
            elif 264 > x > 135:
                if canvas.empty_section(1) is True:
                    canvas.figures(1, switch_turn())
            elif 400 > x > 269:
                if canvas.empty_section(2) is True:
                    canvas.figures(2, switch_turn())
        elif 263 > y > 135:
            if 129 > x > 0:
                if canvas.empty_section(3) is True:
                    canvas.figures(3, switch_turn())
            elif 264 > x > 135:
                if canvas.empty_section(4) is True:
                    canvas.figures(4, switch_turn())
            elif 400 > x > 269:
                if canvas.empty_section(5) is True:
                    canvas.figures(5, switch_turn())
        elif 396 > y > 269:
            if 129 > x > 0:
                if canvas.empty_section(6) is True:
                    canvas.figures(6, switch_turn())
            elif 264 > x > 135:
                if canvas.empty_section(7) is True:
                    canvas.figures(7, switch_turn())
            elif 400 > x > 269:
                if canvas.empty_section(8) is True:
                    canvas.figures(8, switch_turn())


def click_rec(gui_):
    return gui_.bind("<ButtonPress-1>", action)


def click_rel(gui_):
    return gui_.bind("<ButtonRelease-1>", update_score)


gui = Tk()

gui.option_add('*Font', '19')

gui.title(" Tic Tac Toe")

gui.geometry("440x490")

gui.resizable(False, False)

canvas = cFrame(gui)
canvas.grid(column=0, row=1, padx=5)

sc = canvas.score(gui)
sc.grid(column=0, row=0)

ico(gui)

click_rec(gui)

click_rel(gui)

gui.mainloop()
