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

    get_var(vars, 'description').default = 'Installable theme'
    get_var(vars, 'description').modes = ()

    get_var(vars, 'empty_styles').default = True
    get_var(vars, 'empty_styles').modes = ()

    get_var(vars, 'include_doc').default = True
    get_var(vars, 'include_doc').modes = ()

    get_var(vars, 'skinname').default = '(CHANGE THIS) Custom Theme'

    def pre(self, command, output_dir, vars):
        super(Plone3Theme, self).pre(command, output_dir, vars)
        vars['description'] = 'Installable theme: %s.%s' % (vars['namespace_package'], vars['package'])

    def post(self, command, output_dir, vars):
        pass
