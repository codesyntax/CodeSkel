from zopeskel import Plone3Theme as ZSPlone3Theme
from zopeskel.base import get_var
import copy

class Plone3Theme(ZSPlone3Theme):
    _template_dir = 'templates/plone3_theme'
    summary = 'A Theme for Plone 3/4 with no browser resources'
    skinbase = 'Sunburst Theme'
    use_local_commands = True

    vars = copy.deepcopy(ZSPlone3Theme.vars)

    get_var(vars, 'version').default = '1.0'
    get_var(vars, 'version').modes = ()

    get_var(vars, 'description').default = 'Installable theme: %s.%s' % (get_var(vars, 'namespace_package'), get_var(vars, 'package'))
    get_var(vars, 'description').modes = ()

    get_var(vars, 'empty_styles').default = True
    get_var(vars, 'empty_styles').modes = ()

    get_var(vars, 'include_doc').default = True
    get_var(vars, 'include_doc').modes = ()


    def post(self, command, output_dir, vars):
        pass
