
from asari.api import Sonar

sonar = Sonar()

def analyze(text, **args):
    return sonar.ping(text=text)
