from codeskel.base import BaseTemplate
from codeskel.base import var

class Plone3Buildout(BaseTemplate):
    _template_dir = 'templates/cs_plone3_buildout'
    summary = "A buildout for Plone 3 projects"
    required_templates = []
    use_cheetah = True

    vars = [
        var('http_port',
            'HTTP port',
            default=8080),
        ]

    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"



