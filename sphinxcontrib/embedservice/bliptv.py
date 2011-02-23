

from docutils import nodes


CODE = """\
<embed src="http://blip.tv/play/%(uid)s"
       type="application/x-shockwave-flash"
       width="%(width)s"
       height="%(height)s"
       allowscriptaccess="%(allowscriptaccess)s
       allowfullscreen="%(allowfullscreen)s"></embed>
"""


def directive(name, args, options, content, lineno,
            contentOffset, blockText, state, stateMachine):
    """ Restructured text extension for inserting bliptv embedded videos """
    if len(content) == 0:
        return

    string_vars = {
        'uid': content[0],
        'width': 480,
        'height': 300,
        'allowscriptaccess': 'allways',
        'allowfullscreen': 'true', }

    for item in content[1:]:
        item = item.split('=')
        if len(item) == 2:
            key, value = item[0].strip(), item[1].strip()
            if key in string_vars.keys():
                string_vars[key] = value

    return [nodes.raw('', CODE % (string_vars), format='html')]
