

from docutils.parsers.rst import directives

from garbas.rst.embededservices.bliptv import directive as bliptv


bliptv.content = True
directives.register_directive('bliptv', bliptv)
