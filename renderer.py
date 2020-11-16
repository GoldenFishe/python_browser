import tkinter as tk
import re

from network import get_html
from application import parse

window = tk.Tk()
canvas = None
default_width = 1440
default_height = 696


def draw_canvas(width=default_width, height=default_height):
    global canvas, default_width, default_height
    default_width = width
    default_height = height
    canvas = tk.Canvas(width=width, height=height)
    canvas.pack()


def draw_line(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2)


def draw_rect(x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2)


def draw_text(x, y, text, font_family, font_size, font_weight):
    canvas.create_text(x, y, text=text, anchor='w', font=(font_family, font_size, font_weight))


def clear_canvas():
    canvas.delete('all')


def loop():
    window.mainloop()


def draw_ui():
    entry = tk.Entry()

    def make_request():
        url = entry.get()
        if not re.match('^http://', url):
            url = 'http://' + url
        html = get_html(url)
        clear_canvas()
        if html:
            parse(html.text)
        else:
            draw_text(50, 50, 'Неправильный url', 'Arial', 32, 'bold')

    button = tk.Button(text="Ввод", command=make_request)
    entry.pack()
    button.pack()
