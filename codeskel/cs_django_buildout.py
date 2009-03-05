from paste.script.templates import Template
from paste.script.templates import var
from random import choice

class DjangoBuildoutTemplate(Template):
    _template_dir = 'templates/cs_django_buildout'
    summary = 'A plain CS Django buildout'
    required_templates = []
    use_cheetah = True
    
    vars = [
        var('django_version',
            'Django version to fetch, the default is 1.0.2',
            default='1.0.2'),
    ]
    
    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"
