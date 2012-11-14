from cs_plone3_theme import Plone3Theme

class BootstrapTheme(Plone3Theme):
    _template_dir = 'templates/bootstrap_theme'
    summary = 'A Theme for Plone 3/4 based on Twitter Bootstrap'
    skinbase = 'Bootstrap Theme'
    use_local_commands = True

    def post(self, command, output_dir, vars):
        print "-----------------------------------------------------------"
        print "Generation finished"
        print "Remember to pin plone.app.jquery = 1.7.1.1"
        print "in your buildout"
        print
        print "See README.txt for details"
        print "-----------------------------------------------------------"
