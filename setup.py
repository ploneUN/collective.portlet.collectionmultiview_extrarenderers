from setuptools import setup, find_packages
import sys, os

version = '0.2.dev0'

setup(name='collective.portlet.collectionmultiview_extrarenderers',
      version=version,
      description="Extra renderers for collective.portlet.collectionmultiview",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='collective.portlet.collectionmultiview',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='http://svn.plone.org/',
      license='GPLv2+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      namespace_packages=['collective','collective.portlet'],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
