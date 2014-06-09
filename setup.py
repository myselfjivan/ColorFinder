#! /usr/bin/env python

def setup_package():
    build_requires = []
    try:
        import numpy
    except:
        build_requires = ['numpy>=1.5.1']

   	metadata = dict(
		name = 'ColorFinder',
		version = '0.1',
		description = 'A tool for finding colors in an image',
		author = 'Yigit Ozen',
		packages = ['colorfinder',],
		package_data = {
			'colorfinder': ['*.json'],
		},
		data_files = [("", ["LICENSE"])],
		license = 'MIT',
		setup_requires = build_requires,
		install_requires = [
			'Pillow',
			'numpy',
			'scipy',
			'six >= 1.3',
			'scikit-image',
			'scikit-learn',
		],
 	)

	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	setup(**metadata)


if __name__ == '__main__':
    setup_package()
