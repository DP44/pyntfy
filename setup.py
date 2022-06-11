import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyntfy',
    version='0.2.0',
    author='DP44',
    
    description='A module for interacting with ntfy.sh notifications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    url='https://github.com/DP44/pyntfy',
    
    project_urls={
        'Bug Tracker': 'https://github.com/DP44/pyntfy/issues',
    },
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],

    keywords='notification notify ntfy toast android',

    install_requires=['requests'],

    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    
    python_requires='>=3.6',
)