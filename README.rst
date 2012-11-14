Introduction
============

CodeSkel provides a collection of skeletons for quickstarting Plone projects personalized
after repeating many times several changes in our Plone projects

All skeletons are available as PasteScript_ templates and can be used
via the ''paster'' commandline tool. For example to create a package
for a Plone 3 theme you can do::

    paster create -t cs_plone3_theme

this will ask a few questions such as desired package name and a description
and output a complete package skeleton that you can immediately start using.

Please contribute by submitting patches for what you consider 'best of
breed' file layouts for starting Zope projects.

.. _PasteScript: http://pythonpaste.org/script/


Available templates
===================

cs_plone4_buildout
  A base template for a Plone 4 based buildout. It has a single zeo-based instance,
  zeo server configuration and also a supervisor configuration.
  It also adds an egg omelette.
  The port configuration is simplified to a single change in one place.
  It also creates a projectname variable to use it throughout the buildout file

cs_plone3_theme
  This template creates a theme package for Plone 3 and 4. This is the successor of
  ZopeSkel provided plone3_theme but without the resource directories for CSS and images
  because our designers prefer to work with skin-based folders and urls without ++ :)

bootstrap_template
  A template based on ploneteheme.bootstrap, that provides a Twitter Bootstrap
  based template for Plone.

dexterity_cs
  A dexterity based package template based on the ZopeSkel provided one but some additions
  based on archeytype template from ZopeSkel

cs_django_project
  A Django project skeleton

cs_django_buildout
  A Django buildout skeleton, with gunicorn and supervisor configuration and also
  with a project in src folder


Local commands
---------------

This package adds also a local command support for dexterity_cs to add a dexterity based content
type.

cs_dexterity_content
  This local command adds a new dexterity based content-type, with a simple view and creates all
  templates in a single folder instead of one folder per content type as done by the
  zopeskel.dexterity product's localcommand
  It also adds permission information in the same way as the contenttype localcommand does
  for archetype template

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
ZopeSkel (version < 3 of course) and zopeskel.dexterity

.. _`Mikko Ohtamaa's recommendation`: http://opensourcehacker.com/2010/04/13/using-paster-create-command-with-buildout-and-avoiding-the-infamous-dependency-issue/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
