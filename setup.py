from setuptools import setup, find_packages

version = '0.1'

setup(name='sphinxcontrib-embedservice',
      version=version,
      description="Include different services (youtube, blip.tv, ...) in Sphinx",
      long_description=open("README.rst").read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
        ],
      keywords='sphinx embed extensions plugin youtube bliptv vimeo',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='https://github.com/collective/sphinxcontrib-embedservice',
      license='BSD',
      packages=find_packages(),
      namespace_packages=['sphinxcontrib'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Sphinx',
      ],
      )
