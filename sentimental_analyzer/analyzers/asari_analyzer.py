
from asari.api import Sonar


class Analyzer:
    def __init__(self) -> None:
        self.sonar = Sonar()

    def analyze(self, text, **args):
        return self.sonar.ping(text=text)
