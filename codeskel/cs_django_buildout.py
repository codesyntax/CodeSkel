from cs_django_project import CSDjangoProject

class CSDjangoBuildout(CSDjangoProject):
    _template_dir = 'templates/cs_django_buildout'
    summary = 'A basic Django buildout with a project inside'
    use_cheetah = True