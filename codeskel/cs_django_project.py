from zopeskel.base import get_var, BaseTemplate
from zopeskel.vars import StringVar
import copy

class CSDjangoProject(BaseTemplate):
    _template_dir = 'templates/cs_django_project'
    summary = 'A basic Django Project'
    use_cheetah = True

    vars = copy.deepcopy(BaseTemplate.vars)
    vars += [
        StringVar('package', 'Enter the package name (no spaces, no dashes, no dots'),
        StringVar('version', 'Version (like 0.1)'),
        StringVar('description', 'One-line description of the package'),
        StringVar('keywords', 'Space-separated keywords/tags'),
        StringVar('author', 'Author name'),
        StringVar('author_email', 'Author email'),
        StringVar('url', 'URL of homepage'),
        StringVar('license_name', 'License name'),
        StringVar('zip_safe', 'True/False: if the package can be distributed as a .zip file', default=False),
        ]

    get_var(vars, 'version').default = '1.0'
    get_var(vars, 'version').modes = ()

    get_var(vars, 'description').default = 'Django project. '
    get_var(vars, 'description').modes = ()

    get_var(vars, 'keywords').default = 'django'
    get_var(vars, 'keywords').modes = ()

    get_var(vars, 'author').default = ''
    get_var(vars, 'author').modes = ()

    get_var(vars, 'author_email').default = ''
    get_var(vars, 'author_email').modes = ()

    get_var(vars, 'url').default = 'http://code.codesyntax.com/private/'
    get_var(vars, 'url').modes = ()

    get_var(vars, 'license_name').default = 'GPL'
    get_var(vars, 'license_name').modes = ()

    get_var(vars, 'zip_safe').default = 'False'
    get_var(vars, 'zip_safe').modes = ()


