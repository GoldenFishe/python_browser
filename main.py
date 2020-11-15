import renderer
import parser

parser = parser.Parser()
cursor_x = 20
cursor_y = 20


renderer.draw_ui()
renderer.draw_canvas(1440, 696)
renderer.loop()
