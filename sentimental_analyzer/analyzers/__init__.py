
import os
import re

__all__ = []
python_file_regex = re.compile(r'.+\.py')

for filename in os.listdir(f'{os.path.dirname(__file__)}'):
    if not python_file_regex.match(filename):
        continue
    if '__init__.py' == filename:
        continue
    __all__.append(filename.split('.')[0])