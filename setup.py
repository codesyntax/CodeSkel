from setuptools import setup, find_packages
import sys, os

version = '1.2.4'

setup(name='CodeSkel',
      version=version,
      description="A collection of skeletons for quickstarting CS projects.",
      long_description=open('HISTORY.TXT','r').read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ], 
      keywords='web zope command-line skeleton project',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='http://code.codesyntax.com/private/CodeSkel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
         "ZopeSkel",
      ],
      entry_points="""
      [paste.paster_create_template]
      cs_plone25_theme = codeskel:Plone25Theme
      cs_plone3_theme = codeskel:Plone3Theme
      cs_plone3_buildout = codeskel:Plone3Buildout
      udalplone_buildout = codeskel:UdalPloneBuildout
      udalplone3_buildout = codeskel:UdalPlone3Buildout
      """,
      )
