from setuptools import setup, find_packages

version = '1.14'

setup(name='CodeSkel',
      version=version,
      description="A collection of skeletons for quickstarting CS projects.",
      long_description=open("README.rst").read() + "\n" +
                       open('HISTORY.TXT', 'r').read(),
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
      url='http://github.com/codesyntax/CodeSkel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
         'ZopeSkel <= 2.99',
         'zopeskel.dexterity',
      ],
      entry_points="""
      [paste.paster_create_template]
      bootstrap_theme = codeskel:BootstrapTheme
      cs_plone3_theme = codeskel:Plone3Theme
      cs_plone4_buildout = codeskel:Plone4Buildout
      csdexterity = codeskel:CSDexterity
      cs_django_project = codeskel:CSDjangoProject
      cs_django_buildout = codeskel:CSDjangoBuildout

      [zopeskel.zopeskel_sub_template]
      cs_dexterity_content = codeskel:DexterityContentCS
      """,
      )
