from zopeskel import Plone3Theme as ZSPlone3Theme
from zopeskel.base import get_var
import copy


class Plone5Theme(ZSPlone3Theme):
    _template_dir = 'templates/cs_plone5_theme'
    summary = 'A Theme for Plone 5 using Diazo and Barceloneta'
    skinbase = 'Default'
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

    get_var(vars, 'skinname').modes = ()

    def pre(self, command, output_dir, vars):
        super(Plone5Theme, self).pre(command, output_dir, vars)
        vars['description'] = 'Installable theme: %s.%s'.format(
            vars['namespace_package'],
            vars['package'])
        vars['skinname'] = '{}.{} Custom Theme'.format(
            vars['namespace_package'],
            vars['package'])

        vars['author'] = 'CodeSyntax'
        vars['author_email'] = 'info@codesyntax.com'
        vars['url'] = 'https://github.com/codesyntax/{}.{}'.format(
            vars['namespace_package'],
            vars['package'])

    def post(self, command, output_dir, vars):
        pass
