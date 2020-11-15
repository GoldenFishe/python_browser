import renderer
import parser
import tags

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
        font_family = tags.styles['h1']['font_family']
        font_size = tags.styles['h1']['font_size']
        font_weight = tags.styles['h1']['font_weight']
        renderer.draw_text(cursor_x, cursor_y, node['data'], font_family, font_size, font_weight)
        cursor_y += font_size
    if node['tag'] == 'h2':
        font_family = tags.styles['h2']['font_family']
        font_size = tags.styles['h2']['font_size']
        font_weight = tags.styles['h2']['font_weight']
        renderer.draw_text(cursor_x, cursor_y, node['data'], font_family, font_size, font_weight)
        cursor_y += font_size
    if node['tag'] == 'p':
        font_family = tags.styles['p']['font_family']
        font_size = tags.styles['p']['font_size']
        font_weight = tags.styles['p']['font_weight']
        renderer.draw_text(cursor_x, cursor_y, node['data'], font_family, font_size, font_weight)
        cursor_y += font_size
    if node['tag'] == 'span':
        font_family = tags.styles['span']['font_family']
        font_size = tags.styles['span']['font_size']
        font_weight = tags.styles['span']['font_weight']
        renderer.draw_text(cursor_x, cursor_y, node['data'], font_family, font_size, font_weight)
        cursor_y += font_size
    for child_node in node['children']:
        draw_node(child_node)
