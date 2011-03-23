
from docutils import nodes

class embed(nodes.Admonition, nodes.Element):
    pass


def visit_html(self, node):
    #import ipdb; ipdb.set_trace()
    self.body.append(self.starttag(node, 'math'))
def depart_html(self, node):
    #import ipdb; ipdb.set_trace()
    self.body.append('</math>')

def setup(app):
    app.add_node(embed, html=(visit_html, depart_html))

    from bliptv import BlipTV
    app.add_directive('embed-bliptv', BlipTV)

    # TODO: Add more services ...
