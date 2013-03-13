from setuptools import setup, find_packages
import sys, os

version = '0.9'

setup(
	name='ckanext-test',
	version=version,
	description="Test Plugin",
	long_description="""\
	An almost empty CKAN extension plugin for testing purposes.
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Knud M\xc3\xb6ller',
	author_email='knud@datalysator.com',
	url='https://github.com/knudmoeller/ckanext-berlin',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.test'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	         test=ckanext.test.plugin:TestPlugin
	""",
)
