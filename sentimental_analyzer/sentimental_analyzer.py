

from sentimental_analyzer.analyzers import *

class SentimentalAnalyzer:
    analyzer_dict = {
        'asari': asari_analyzer,
        'bert': bert_analyzer,
        'oseti': oseti_analyzer,
    }

    def __init__(self, analyzer_type: str):
        if not analyzer_type in self.analyzer_dict.keys():
            raise TypeError("'%s' is not supported." % analyzer_type)
        # TODO: 動的にモジュールをインポートするように切り替える　他のライブラリのインスタンス化に時間がかかるため
        self.analyzer = self.analyzer_dict[analyzer_type]

    def analyze(self, text, **args):
        return getattr(self.analyzer, 'analyze')(text)
