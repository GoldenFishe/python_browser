from html.parser import HTMLParser


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
        self.feed(html)
        return self.ast

    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            node = {
                "tag": tag,
                "data": "",
                "attrs": attrs,
                "children": []
            }
            self.queue.append(node)

    def handle_data(self, data):
        if len(self.queue) > 0:
            self.queue[-1]['data'] = data

    def handle_endtag(self, tag):
        if tag == 'body':
            last_item = self.queue.pop()
            if len(self.queue) > 0:
                self.queue[-1]['children'].append(last_item)
            else:
                self.ast['children'].append(last_item)
