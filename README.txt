Introduction
============

CodeSkel provides a collection of skeletons for quickstarting Plone projects.

All skeletons are available as PasteScript_ templates and can be used
via the ''paster'' commandline tool. For example to create a package
for a Plone 3 theme you can do::

    paster create -t cs_plone3_theme

this will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.

.. _PasteScript: http://pythonpaste.org/script/
.. _Subversion repository: http://code.codesyntax.com/private/CodeSkel/trunk#egg=CodeSkel-dev


Available templates
===================

Development templates
---------------------
cs_plone2.5_theme
  A template to create a new Zope 2 products for Plone 2.5
  site. If you are targetting Plone 3 please use the cs_plone3_theme template
  instead.

cs_plone3_theme
  This template creates a theme package for Plone 3.0. This is the succesor
  to the popular DIYPloneStyle_ product.


.. _DIYPloneStyle: http://plone.org/products/diyplonestyle


Hosting / deployment templates
------------------------------

cs_plone3_buildout
  A basic buildout_ based instance for Plone 3.1.x projects. If you also need
  ZEO or caching take a look at the plone_hosting template.

udalplone_buildout
  A basic buildout to install a UdalPlone (Plone 2.5.x)

udalplone3_buildout
  A basic buildout to install a UdalPlone (Plone 3.x)

.. _buildout: http://plone.org/documentation/tutorial/buildout
.. _varnish: http://varnish.projects.linpro.no


Testing
-------

Since version 1.5, CodeSkel has tests.  It's required to run these
before checking in; they can be run like::

    $ python setup.py test

You can also set a test environment using the buildout bootstrap::

    $ python boostrap.py
    $ bin/buildout

You will then have a `test` script available::

    $ bin/test

You can even run just one test::

    $ bin/test -t silva_buildout

