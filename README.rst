Introduction
============

CodeSkel provides a collection of skeletons for quickstarting Plone projects personalized
after repeating many times several changes in our Plone projects

All skeletons are available as PasteScript_ templates and can be used
via the ''paster'' commandline tool. For example to create a package
for a Plone 4 theme you can do::

    paster create -t cs_plone_theme

this will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.

.. _PasteScript: http://pythonpaste.org/script/


Available templates
===================

cs_plone5_theme
  Diazo theme for Plone 5 based in plonetheme.barceloneta

cs_plone_buildout
  A base template for a Plone 5 based buildout. It can be used for Plone 4 too.
  It has a single zeo-based instance, zeo server configuration and also a
  supervisor configuration. It provides additional instances if needed and
  sample configuration for haproxy and varnish.
  It also creates an egg omelette.
  It creates Apache and Nginx configuration files so, you can just symlink
  those files to the configuration folder of Apache/Nginx. The domain names
  can be configured directly in the buildout file.
  The port configuration is simplified to a single change in one place.
  It also creates a projectname variable to use it throughout the buildout file

cs_plone4_theme
  This template creates a theme package for Plone 4 (it will work for 3 too).
  This is the successor of ZopeSkel provided plone3_theme but without the
  resource directories for CSS and images because our designers prefer to work
  with skin-based folders and urls without ++ :)

cs_bootstrap_theme
  A template based on ploneteheme.bootstrap, that provides a Bootstrap_
  based template for Plone.

cs_dexterity
  A dexterity based package template based on the one provided by
  `zopeskel.dexterity`_ but with some changes, such as: no traces of Grok, less
  questions when creating the page, custom permissions, ...


Local commands
---------------

This package adds also a local command support for cs_dexterity based packages
to add a dexterity based content type.

cs_dexterity_content
  This local command adds a new dexterity based content-type, with a simple
  view and creates all templates in a single folder. The content-types created
  are shown directly in the navigation.

Installation
==============

DO NOT INSTALL THIS PACKAGE IN THE SYSTEM LIBRARY. USE A VIRTUALENV TO INSTALL IT.

This suggestion follows `Mikko Ohtamaa's recommendation`_::

  The internet is full of tutorial saying easy_install ZopeSkel. If you ever encounter this
  kind of tutorial, it's wrong.

  Do not never use system paster command.

  Do not ever run sudo easy_install ZopeSkel. Do not ever run paster local commands using a
  paster command from your system-wide Python installation.

We have been fighting for long with system-wide ZopeSkel and some time ago started following
Mikko's recommendation and now we have almost zero problems when working with ZopeSkel/CodeSkel.

So, create a virtualenv_ and install CodeSkel in there, it will automatically pull
ZopeSkel_ (version < 3) and `zopeskel.dexterity`_

.. _ZopeSkel: https://pypi.python.org/pypi/ZopeSkel/2.21.2
.. _`Mikko Ohtamaa's recommendation`: http://opensourcehacker.com/2010/04/13/using-paster-create-command-with-buildout-and-avoiding-the-infamous-dependency-issue/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _`zopeskel.dexterity`: https://pypi.python.org/pypi/zopeskel.dexterity
.. _Bootstrap: https://getbootstrap.com/
