from setuptools import setup, find_packages

setup(
    name='scratch_explorer',
    version='1.0',
    author='Jacob Cohen, Matt Davidson, Crystal Yu, and Faisal Alsallum',
    packages=find_packages(include=['scratch_explorer']),
    package_data={'scratch_explorer/data': ['*.csv'], 
                  'scratch_explorer/exports': ['*.sav']},
    install_requires=[
        'dash=1.17.0',
        'numpy=1.19.2',
        'pandas=1.1.3',
        'plotly=4.13.0',
        'python=3.8.5'
    ]
)