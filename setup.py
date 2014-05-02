from setuptools import setup, find_packages
import sys, os

version = '0.2dev'

setup(
	name='ckanext-publicamundi',
	version=version,
	description="A collection of CKAN plugins developed for PublicaMundi project",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Michail Alexakis',
	author_email='alexakis@imis.athena-innovation.gr',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.publicamundi'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
        "jsonpickle",
	],
	entry_points=\
	"""
        [ckan.plugins]

        publicamundi_dataset = ckanext.publicamundi.plugins:DatasetForm

        publicamundi_package = ckanext.publicamundi.plugins:PackageController

        publicamundi_errorware = ckanext.publicamundi.plugins:ErrorHandler

        [paste.paster_command]

        publicamundi-greet = ckanext.publicamundi.commands:Greet

        publicamundi-setup = ckanext.publicamundi.commands:Setup

        publicamundi-cleanup = ckanext.publicamundi.commands:Cleanup

        [fanstatic.libraries]

	""",
)