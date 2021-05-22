
import oseti

oseti = oseti.Analyzer()

def analyze(text, **args):
    all_count = 0
    summary = {
        'positive': 0,
        'negative': 0,
    }
    for sent_polarity in oseti.count_polarity(text):
        summary['positive'] += sent_polarity['positive']
        summary['negative'] += sent_polarity['negative']
    all_count = summary['positive'] + summary['negative']
    return restructure(text, summary, all_count)

def restructure(text: str, summary: dict, all_count: int):
    confidence = lambda cls_cnt: 0.5 if 0 == all_count else cls_cnt / all_count
    class_obj = lambda cls_name, cls_cnt: {
        'class_name': cls_name,
        'confidence': confidence(cls_cnt)
    }
    return {
        'text': text,
        'top_class': 'positive' if summary['positive'] >= summary['negative'] else 'negative',
        'classes': [
            class_obj('positive', summary['positive']),
            class_obj('negative', summary['negative'])
        ]
    }
