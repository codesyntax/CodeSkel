from zopeskel.dexterity.localcommands.dexterity import DexterityContent

class DexterityContentCS(DexterityContent):
    parent_templates = ['dexterity']
                        
    _template_dir = 'templates/dexterity/content_cs'
    summary = 'A content type skeleton for Dexterity based on CS conventions'
