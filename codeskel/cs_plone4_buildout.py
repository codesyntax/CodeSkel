from codeskel.base import BaseTemplate
from codeskel.base import var

class Plone4Buildout(BaseTemplate):
    _template_dir = 'templates/cs_plone4_buildout'
    summary = "A buildout for Plone 4 projects"
    use_local_commands = False
    required_templates = []
    use_cheetah = True

    vars = [
        var('http_port',
            'HTTP port',
            default=8080),
        ]

    def pre(self, command, output_dir, vars):
        super(BaseTemplate, self).pre(command, output_dir, vars)
        vars['zeo_port'] = int(vars['http_port']) + 10
        vars['debug_instance_port'] = int(vars['zeo_port']) + 1
        vars['haproxy_port'] = int(vars['http_port']) + 20
        vars['varnish_port'] = int(vars['http_port']) + 30

    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "You probably want to run python bootstrap.py and then edit"
        print "buildout.cfg before running bin/buildout -v"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"
