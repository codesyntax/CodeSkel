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
        vars['instance2_port'] = int(vars['http_port']) + 1
        vars['instance3_port'] = int(vars['http_port']) + 2
        vars['instance4_port'] = int(vars['http_port']) + 3
        vars['instance5_port'] = int(vars['http_port']) + 4
        vars['haproxy_port'] = int(vars['http_port']) + 20
        vars['varnish_port'] = int(vars['http_port']) + 30

    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print " Generation finished"
        print
        print " See README.txt for details"
        print "-----------------------------------------------------------"
        print ""
        print "              NEXT STEPS "
        print "-----------------------------------------------------------"
        print "              $ cd " + output_dir
        print "              $ ~/buildout.python/bin/virtualenv-2.7 ."
        print "              $ ./bin/pip install zc.buildout"
        print "              $ ./bin/buildout -vv"
        print ""
