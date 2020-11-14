import tkinter as tk

from network import get_url
from application import parse

window = tk.Tk()
canvas = None


def draw_canvas(width, height):
    global canvas
    canvas = tk.Canvas(width=width, height=height)
    canvas.pack()


def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2)


def draw_rect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2)


def draw_text(x, y, text, size):
    canvas.create_text(x, y, text=text, anchor='w', font="Verdana " + str(size))


def loop():
    window.mainloop()


def draw_ui():
    entry = tk.Entry()

    def make_request():
        html = get_url(entry.get())
        # html = '<h1>test</h1>'
        # print(html)
        parse(html)

    button = tk.Button(text="Ввод", command=make_request)
    entry.pack()
    button.pack()
