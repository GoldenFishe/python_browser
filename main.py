import renderer
import parser

parser = parser.Parser()
cursor_x = 20
cursor_y = 20


renderer.draw_ui()
renderer.draw_canvas(300, 300)
renderer.loop()
