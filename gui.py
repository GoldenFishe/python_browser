import tkinter as tk
import re
from network import get_html
from application import parse


class GUI:
    def __init__(self, width, height):
        self.window = tk.Tk()
        self.frame_top = tk.Frame(self.window)
        self.frame_bottom = tk.Frame(self.window)
        self.canvas = tk.Canvas(self.frame_bottom,
                                width=width,
                                height=height,
                                scrollregion=(0, 0, 1000, 1000))
        self.horizontal_scrollbar = tk.Scrollbar(self.frame_bottom, orient=tk.HORIZONTAL)
        self.vertical_scrollbar = tk.Scrollbar(self.frame_bottom, orient=tk.VERTICAL)
        self.url_entry = tk.Entry(self.frame_top)
        self.get_url_button = tk.Button(self.frame_top, text="Ввод", command=self._get_page)

    def create_window(self):
        self._draw_scrollbars()
        self._draw_layout()
        self._draw_controls()

    def _draw_scrollbars(self):
        self.horizontal_scrollbar['command'] = self.canvas.xview
        self.vertical_scrollbar['command'] = self.canvas.yview
        self.canvas.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.canvas.configure(xscrollcommand=self.horizontal_scrollbar.set)

    def _draw_layout(self):
        self.horizontal_scrollbar.grid(column=0, row=1, sticky=(tk.W, tk.E))
        self.vertical_scrollbar.grid(column=1, row=0, sticky=(tk.N, tk.S))
        self.horizontal_scrollbar.grid(column=0, row=1, sticky="we")
        self.vertical_scrollbar.grid(column=1, row=0, sticky="ns")
        self.canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame_bottom.columnconfigure(0, weight=3)
        self.frame_bottom.rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.canvas.grid(column=0, row=0, sticky="nwes")
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

    def _draw_controls(self):
        self.url_entry.pack(side=tk.LEFT)
        self.get_url_button.pack(side=tk.LEFT)

    def _get_page(self):
        url = self.url_entry.get()
        if not re.match('^http://', url) and not re.match('^https://', url):
            url = 'http://' + url
        html = get_html(url)
        self.clear_canvas()
        if html:
            parse(html.text)
        else:
            self.draw_text(50, 50, 'Неправильный url', 'Arial', 32, 'bold')

    def loop(self):
        self.window.title("Браузер Антона Геннадьевича")
        self.frame_top.pack()
        self.frame_bottom.pack()
        self.window.mainloop()

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2)

    def draw_rect(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2)

    def draw_text(self, x, y, text, font_family, font_size, font_weight):
        self.canvas.create_text(x, y, text=text, anchor='w', font=(font_family, font_size, font_weight))

    def clear_canvas(self, ):
        self.canvas.delete('all')
