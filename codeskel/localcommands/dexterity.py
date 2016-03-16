from zopeskel.dexterity.localcommands.dexterity import DexterityContent
from zopeskel.base import var


class DexterityContentCS(DexterityContent):
    parent_templates = ['dexterity', 'csdexterity']

    _template_dir = 'templates/dexterity/content_cs'
    summary = 'A content type skeleton for Dexterity based on CS conventions'

    vars = [
        var('contenttype_name', 'Content type name ', default='Example Type'),
        var('folderish', 'True/False: Content type should act as a container ',
            default=False),
    ]

    def pre(self, command, output_dir, vars):
        super(DexterityContentCS, self).pre(command, output_dir, vars)
        vars['add_permission_id'] = vars['package_dotted_name'] + '.Add' + vars['contenttype_name']
        vars['global_allow'] = True
        vars['allow_discussion'] = False
        vars['contenttype_description'] = 'Description of this type'
