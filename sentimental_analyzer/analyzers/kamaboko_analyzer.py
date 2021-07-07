
from kamaboko import Kamaboko
from cli import install, delete

def analyze(text, **args):
    kamaboko = Kamaboko()
    result = kamaboko.analyze(text)
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