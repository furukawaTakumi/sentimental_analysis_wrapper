from setuptools import setup, find_packages

install_requires = [
    'pybind11',
    'numpy',
    'neologdn',
    'asari'
]



setup(
    name='sentimental_analyzer',
    version='0.0.0',
    install_requires=install_requires,
    packages=[
        'sentimental_analyzer'
    ]
)
