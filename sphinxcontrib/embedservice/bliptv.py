
from docutils import nodes
from sphinx.util.compat import make_admonition
from sphinx.util.compat import Directive
from sphinxcontrib.embedservice import embed

class BlipTV(Directive):

    has_content = True
    template = """
        <embed src="http://blip.tv/play/%(uid)s"
               type="application/x-shockwave-flash"
               width="%(width)s"
               height="%(height)s"
               allowscriptaccess="%(allowscriptaccess)s
               allowfullscreen="%(allowfullscreen)s"></embed>"""

    def run(self):
        if len(self.content) == 0:
            # TODO: raise nice error that something is missing
            return

        string_vars = {
            'uid': self.content[0],
            'width': 480,
            'height': 300,
            'allowscriptaccess': 'allways',
            'allowfullscreen': 'true', }

        # TODO: need to redo this
        #for item in self.content[1:]:
        #    item = item.split('=')
        #    if len(item) == 2:
        #        key, value = item[0].strip(), item[1].strip()
        #        if key in string_vars.keys():
        #            string_vars[key] = value

        env = self.state.document.settings.env
        targetid = "bliptv-%d" % env.new_serialno('embed')
        targetnode = nodes.target('', '', ids=[targetid])

        ad = make_admonition(embed, self.name, ['Todo'], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        return [targetnode] + ad
