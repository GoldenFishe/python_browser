import renderer
import parser

parser = parser.Parser()
cursor_x = 20
cursor_y = 20


def parse(html):
    ast = parser.parse(html)
    draw(ast)


def draw(ast):
    for node in ast['children']:
        draw_node(node)


def draw_node(node):
    global cursor_y
    if node['tag'] == 'h1':
        renderer.draw_text(cursor_x, cursor_y, node['data'], 22)
        cursor_y += 22
    if node['tag'] == 'h2':
        renderer.draw_text(cursor_x, cursor_y, node['data'], 16)
        cursor_y += 16
    if node['tag'] == 'p':
        renderer.draw_text(cursor_x, cursor_y, node['data'], 14)
        cursor_y += 14
    if node['tag'] == 'span':
        renderer.draw_text(cursor_x, cursor_y, node['data'], 12)
        cursor_y += 12
    for child_node in node['children']:
        draw_node(child_node)
