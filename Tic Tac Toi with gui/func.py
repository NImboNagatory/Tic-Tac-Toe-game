from tkinter import *
from PIL import Image, ImageTk
import pandas

bigBoxSize = 400 / 3


class cFrame(Frame):
    def __init__(self, master, cwidth=400, cheight=400):
        Frame.__init__(self, master, relief=RAISED, height=550, width=600)
        self.canvasWidth = cwidth
        self.canvasHeight = cheight
        self.canvas = Canvas(self, width=cwidth, height=cheight, border=0)
        self.df = None
        self.drawGridLines()
        self.create_dataframe()
        self.o_score = 0
        self.x_score = 0
        self.canvas.grid(padx=10)

    def drawGridLines(self, linewidth=4):
        self.canvas.create_line(0, bigBoxSize, self.canvasWidth, bigBoxSize, width=linewidth)
        self.canvas.create_line(0, bigBoxSize * 2, self.canvasWidth, bigBoxSize * 2, width=linewidth)
        self.canvas.create_line(bigBoxSize, 0, bigBoxSize, self.canvasWidth, width=linewidth)
        self.canvas.create_line(bigBoxSize * 2, 0, bigBoxSize * 2, self.canvasWidth, width=linewidth)

    def create_dataframe(self):
        self.df = pandas.DataFrame(
            {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})

    def declare_winner(self, figure):
        self.score(self).update()
        if figure == 'o':

            self.canvas.create_text(bigBoxSize+50, bigBoxSize, text="ⓞ\n  You Win!", font=("Castellar", 50))
            self.canvas.update()
            self.canvas.after(1500)
            self.canvas.delete("all")
        elif figure == 'x':

            self.canvas.create_text(bigBoxSize+50, bigBoxSize, text="✖\n  You Win!", font=("Castellar", 50))
            self.canvas.update()
            self.canvas.after(1500)
            self.canvas.delete("all")
        elif figure == '':

            self.canvas.create_text(bigBoxSize+50, bigBoxSize, text="ⓞ - ✖\n  Tie!", font=("Castellar", 50))
            self.canvas.update()
            self.canvas.after(1500)
            self.canvas.delete("all")

    def score(self, gui, figure=''):
        if figure == 'x':
            score_ = Label(gui, text=f'>ⓞ  {self.o_score} : {self.x_score}  ✖  ', width=15, height=2,
                           font=("Castellar", 20))
            return score_
        elif figure == 'o':
            score_ = Label(gui, text=f'  ⓞ  {self.o_score} : {self.x_score}  ✖<', width=15, height=2,
                           font=("Castellar", 20))
            return score_
        else:
            score_ = Label(gui, text=f'>ⓞ  {self.o_score} : {self.x_score}  ✖  ', width=15, height=2,
                           font=("Castellar", 20))
            return score_

    def draw_winning_line(self, line_num):
        if line_num == 7:
            self.canvas.create_line(0, 0, bigBoxSize * 3, bigBoxSize * 3, width=8)
        elif line_num == 8:
            self.canvas.create_line(0, bigBoxSize * 3, bigBoxSize * 3, 0, width=8)
        elif line_num == 1:
            self.canvas.create_line(0, bigBoxSize / 2, bigBoxSize * 3, bigBoxSize / 2, width=8)
        elif line_num == 2:
            self.canvas.create_line(0, bigBoxSize + (bigBoxSize / 2), bigBoxSize * 3, bigBoxSize + (bigBoxSize / 2),
                                    width=8)
        elif line_num == 3:
            self.canvas.create_line(0, (bigBoxSize * 2) + (bigBoxSize / 2), bigBoxSize * 3,
                                    (bigBoxSize * 2) + (bigBoxSize / 2), width=8)
        elif line_num == 4:
            self.canvas.create_line(bigBoxSize / 2, 0, bigBoxSize / 2, bigBoxSize * 3, width=8)
        elif line_num == 5:
            self.canvas.create_line(bigBoxSize + (bigBoxSize / 2), 0, bigBoxSize + (bigBoxSize / 2), bigBoxSize * 3,
                                    width=8)
        elif line_num == 6:
            self.canvas.create_line((bigBoxSize * 2) + (bigBoxSize / 2), 0, (bigBoxSize * 2) + (bigBoxSize / 2),
                                    bigBoxSize * 3, width=8)

    def check_winner(self, figure):
        if figure == 'x':
            if self.df.iloc[0].item() == 'x' and self.df.iloc[1].item() == 'x' and self.df.iloc[2].item() == 'x':
                self.draw_winning_line(1)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[3].item() == 'x' and self.df.iloc[4].item() == 'x' and self.df.iloc[5].item() == 'x':
                self.draw_winning_line(2)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[6].item() == 'x' and self.df.iloc[7].item() == 'x' and self.df.iloc[8].item() == 'x':
                self.draw_winning_line(3)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() == 'x' and self.df.iloc[3].item() == 'x' and self.df.iloc[6].item() == 'x':
                self.draw_winning_line(4)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[1].item() == 'x' and self.df.iloc[4].item() == 'x' and self.df.iloc[7].item() == 'x':
                self.draw_winning_line(5)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[2].item() == 'x' and self.df.iloc[5].item() == 'x' and self.df.iloc[8].item() == 'x':
                self.draw_winning_line(6)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() == 'x' and self.df.iloc[4].item() == 'x' and self.df.iloc[8].item() == 'x':
                self.draw_winning_line(7)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.canvas.update()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[2].item() == 'x' and self.df.iloc[4].item() == 'x' and self.df.iloc[6].item() == 'x':
                self.draw_winning_line(8)
                self.x_score = self.x_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('x')
                self.drawGridLines()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() != 'empty' and self.df.iloc[1].item() != 'empty' and self.df.iloc[2].item() != 'empty':

                if self.df.iloc[3].item() != 'empty' and self.df.iloc[4].item() != 'empty' and self.df.iloc[5].item() != 'empty':

                    if self.df.iloc[6].item() != 'empty' and self.df.iloc[7].item() != 'empty' and self.df.iloc[8].item() != 'empty':

                        self.canvas.update()
                        self.df = None
                        self.canvas.after(1500)
                        self.canvas.delete("all")
                        self.declare_winner('')
                        self.drawGridLines()
                        self.canvas.update()
                        self.df = pandas.DataFrame(
                            {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                                          'empty']})
        elif figure == 'o':
            if self.df.iloc[0].item() == 'o' and self.df.iloc[1].item() == 'o' and self.df.iloc[2].item() == 'o':
                self.draw_winning_line(1)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()
                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[3].item() == 'o' and self.df.iloc[4].item() == 'o' and self.df.iloc[5].item() == 'o':
                self.draw_winning_line(2)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[6].item() == 'o' and self.df.iloc[7].item() == 'o' and self.df.iloc[8].item() == 'o':
                self.draw_winning_line(3)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() == 'o' and self.df.iloc[3].item() == 'o' and self.df.iloc[6].item() == 'o':
                self.draw_winning_line(4)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[1].item() == 'o' and self.df.iloc[4].item() == 'o' and self.df.iloc[7].item() == 'o':
                self.draw_winning_line(5)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[2].item() == 'o' and self.df.iloc[5].item() == 'o' and self.df.iloc[8].item() == 'o':
                self.draw_winning_line(6)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() == 'o' and self.df.iloc[4].item() == 'o' and self.df.iloc[8].item() == 'o':
                self.draw_winning_line(7)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[2].item() == 'o' and self.df.iloc[4].item() == 'o' and self.df.iloc[6].item() == 'o':
                self.draw_winning_line(8)
                self.o_score = self.o_score + 1
                self.canvas.update()
                self.df = None
                self.canvas.after(1500)
                self.canvas.delete("all")
                self.declare_winner('o')
                self.drawGridLines()

                self.df = pandas.DataFrame(
                    {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']})
            elif self.df.iloc[0].item() != 'empty' and self.df.iloc[1].item() != 'empty' and self.df.iloc[2].item() != 'empty':

                if self.df.iloc[3].item() != 'empty' and self.df.iloc[4].item() != 'empty' and self.df.iloc[5].item() != 'empty':

                    if self.df.iloc[6].item() != 'empty' and self.df.iloc[7].item() != 'empty' and self.df.iloc[8].item() != 'empty':

                        self.canvas.update()
                        self.df = None
                        self.canvas.after(1500)
                        self.canvas.delete("all")
                        self.declare_winner('')
                        self.drawGridLines()

                        self.df = pandas.DataFrame(
                            {'sections': ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                                          'empty']})

    def fill_section(self, section, figure):
        if self.df is not None:
            self.df.iloc[section] = figure

    def empty_section(self, section):
        if self.df is not None:
            if self.df.iloc[section].values == 'empty':
                return True
            else:
                return False

    def draw_o(self, start_x, start_y, fin_x, fin_y, section):
        if self.df is not None:
            self.fill_section(section, 'o')
            self.canvas.create_oval(start_x, start_y, fin_x, fin_y, width=4)
            self.check_winner('o')

    def draw_x(self, start_x, start_y, fin_x, fin_y, section):
        if self.df is not None:
            self.fill_section(section, 'x')
            self.canvas.create_line(start_x, start_y, fin_x, fin_y, width=4)
            self.canvas.create_line(fin_x, start_y, start_x, fin_y, width=4)
            self.check_winner('x')

    def figures(self, section, figure):
        if self.df is not None:
            if section == 0:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(10, bigBoxSize - 10, bigBoxSize - 10, 10, section)
                    elif figure == 'o':
                        self.draw_o(10, bigBoxSize - 10, bigBoxSize - 10, 10, section)
            elif section == 1:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(bigBoxSize + 10, bigBoxSize - 10, (bigBoxSize * 2) - 10, 10, section)
                    elif figure == 'o':
                        self.draw_o(bigBoxSize + 10, bigBoxSize - 10, (bigBoxSize * 2) - 10, 10, section)
            elif section == 2:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x((bigBoxSize * 2) + 10, bigBoxSize - 10, (bigBoxSize * 3) - 10, 10, section)
                    elif figure == 'o':
                        self.draw_o((bigBoxSize * 2) + 10, bigBoxSize - 10, (bigBoxSize * 3) - 10, 10, section)
            elif section == 3:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(10, bigBoxSize + 10, bigBoxSize - 10, (bigBoxSize * 2) - 10, section)
                    elif figure == 'o':
                        self.draw_o(10, bigBoxSize + 10, bigBoxSize - 10, (bigBoxSize * 2) - 10, section)
            elif section == 4:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(bigBoxSize + 10, (bigBoxSize * 2) - 10, (bigBoxSize * 2) - 10, bigBoxSize + 10, section)
                    elif figure == 'o':
                        self.draw_o(bigBoxSize + 10, (bigBoxSize * 2) - 10, (bigBoxSize * 2) - 10, bigBoxSize + 10, section)
            elif section == 5:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x((bigBoxSize * 2) + 10, (bigBoxSize * 2) - 10, (bigBoxSize * 3) - 10, bigBoxSize + 10,
                                    section)
                    elif figure == 'o':
                        self.draw_o((bigBoxSize * 2) + 10, (bigBoxSize * 2) - 10, (bigBoxSize * 3) - 10, bigBoxSize + 10,
                                    section)
            elif section == 6:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(10, (bigBoxSize * 3) - 10, bigBoxSize - 10, (bigBoxSize * 2) + 10, section)
                    elif figure == 'o':
                        self.draw_o(10, (bigBoxSize * 3) - 10, bigBoxSize - 10, (bigBoxSize * 2) + 10, section)
            elif section == 7:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x(bigBoxSize + 10, (bigBoxSize * 3) - 10, (bigBoxSize * 2) - 10, (bigBoxSize * 2) + 10,
                                    section)
                    elif figure == 'o':
                        self.draw_o(bigBoxSize + 10, (bigBoxSize * 3) - 10, (bigBoxSize * 2) - 10, (bigBoxSize * 2) + 10,
                                    section)
            elif section == 8:
                if self.empty_section(section) is True:
                    if figure == 'x':
                        self.draw_x((bigBoxSize * 2) + 10, (bigBoxSize * 3) - 10, (bigBoxSize * 3) - 10,
                                    (bigBoxSize * 2) + 10, section)
                    elif figure == 'o':
                        self.draw_o((bigBoxSize * 2) + 10, (bigBoxSize * 3) - 10, (bigBoxSize * 3) - 10,
                                    (bigBoxSize * 2) + 10, section)


def ico(gui, state=''):
    if state == 'x':
        icon = Image.open('data/x.png')
        photo = ImageTk.PhotoImage(icon)
        return gui.wm_iconphoto(False, photo)
    elif state == 'o':
        icon = Image.open('data/o.jpg')
        photo = ImageTk.PhotoImage(icon)
        return gui.wm_iconphoto(False, photo)
    else:
        icon = Image.open('data/tictactoe.jpg')
        photo = ImageTk.PhotoImage(icon)
        return gui.wm_iconphoto(False, photo)
