
import os
import re

__all__ = []
python_file_regex = re.compile(r'.+\.py')

for filename in os.listdir(f'{os.getcwd()}/sentimental_analyzer/analyzers'):
    if not python_file_regex.match(filename):
        continue
    if '__init__.py' == filename:
        continue
    __all__.append(filename.split('.')[0])