import tkinter as tk
import re

from network import get_html
from application import parse

window = tk.Tk()
# window.geometry('300x200-40+40')
frame_top = tk.Frame(window)
frame_bottom = tk.Frame(window, bg="green")
default_width = 600
default_height = 400
canvas = None

frame_top.pack()
frame_bottom.pack()

window.title("Браузер Антона Геннадьевича")


def draw_canvas(width=default_width, height=default_height):
    global canvas, default_width, default_height
    default_width = width
    default_height = height

    h = tk.Scrollbar(frame_bottom, orient=tk.HORIZONTAL)
    v = tk.Scrollbar(frame_bottom, orient=tk.VERTICAL)
    canvas = tk.Canvas(frame_bottom,
                       width=width,
                       height=height,
                       scrollregion=(0, 0, 1000, 1000),
                       yscrollcommand=v.set,
                       xscrollcommand=h.set)
    h['command'] = canvas.xview
    v['command'] = canvas.yview
    canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    h.grid(column=0, row=1, sticky=(tk.W, tk.E))
    v.grid(column=1, row=0, sticky=(tk.N, tk.S))
    frame_bottom.columnconfigure(0, weight=3)
    frame_bottom.rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    canvas.grid(column=0, row=0, sticky="nwes")
    h.grid(column=0, row=1, sticky="we")
    v.grid(column=1, row=0, sticky="ns")
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)


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
    entry = tk.Entry(frame_top)

    def make_request():
        url = entry.get()
        if not re.match('^http://', url) and not re.match('^https://', url):
            url = 'http://' + url
        html = get_html(url)
        clear_canvas()
        if html:
            parse(html.text)
        else:
            draw_text(50, 50, 'Неправильный url', 'Arial', 32, 'bold')

    button = tk.Button(frame_top, text="Ввод", command=make_request)
    button.pack(side=tk.LEFT)
    entry.pack(side=tk.LEFT)
