
from kamaboko import Kamaboko
from cli import install, delete

class Analyzer:
    def __init__(self) -> None:
        self.kamaboko = Kamaboko()

    def analyze(self, text, **args):
        result = self.kamaboko.analyze(text)
        class_obj = lambda class_name: {
            'class_name': class_name,
            'confidence': result[class_name]
        }
        return {
            'text': text,
            'top_class': 'positive' if result['positive'] >= result['negative'] else 'negative',
            'classes': [
                class_obj('positive'),
                class_obj('negative')
            ]
        }