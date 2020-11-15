from html.parser import HTMLParser
import tags


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ast = {
            "tag": "root",
            "data": "",
            "attrs": [],
            "children": []
        }
        self.queue = []

    def error(self, message):
        print(message)
        pass

    def parse(self, html):
        formatted_html = html.replace('\n', '').strip()
        self.feed(formatted_html)
        return self.ast

    def handle_starttag(self, tag, attrs):
        if tag in tags.available_tags:
            node = {
                "tag": tag,
                "data": "",
                "attrs": attrs,
                "children": []
            }
            self.queue.append(node)

    def handle_data(self, data):
        if self.lasttag in tags.available_tags:
            if not data.isspace():
                self.queue[-1]['data'] = data

    def handle_endtag(self, tag):
        if tag in tags.available_tags:
            last_item = self.queue.pop()
            if len(self.queue) > 0:
                self.queue[-1]['children'].append(last_item)
            else:
                self.ast['children'].append(last_item)
