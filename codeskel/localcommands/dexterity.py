from zopeskel.dexterity.localcommands.dexterity import DexterityContent


class DexterityContentCS(DexterityContent):
    parent_templates = ['dexterity', 'csdexterity']

    _template_dir = 'templates/dexterity/content_cs'
    summary = 'A content type skeleton for Dexterity based on CS conventions'

    def pre(self, command, output_dir, vars):
        super(DexterityContentCS, self).pre(command, output_dir, vars)
        vars['add_permission_id'] = vars['package_dotted_name'] + '.Add' + vars['contenttype_name']
