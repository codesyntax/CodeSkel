from zopeskel.dexterity.dexterity import Dexterity
from zopeskel.plone import BasicZope


class CSDexterity(Dexterity):
    _template_dir = 'templates/dexterity_cs'

    vars = BasicZope.vars
