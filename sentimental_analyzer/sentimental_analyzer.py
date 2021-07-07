

from .analyzers import *

class SentimentalAnalyzer:
    analyzer_dict = {
        'asari': asari_analyzer,
        'bert': bert_analyzer,
        'oseti': oseti_analyzer,
        'kamaboko': kamaboko_analyzer,
    }

    def __init__(self, analyzer_type: str):
        if not analyzer_type in self.analyzer_dict.keys():
            raise TypeError("'%s' is not supported." % analyzer_type)
        # TODO: 動的にモジュールをインポートするように切り替える　他のライブラリのインスタンス化に時間がかかるため
        self.__type = analyzer_type
        self.__analyzer = self.analyzer_dict[analyzer_type]

    @property
    def type(self):
        return self.__type

    def analyze(self, text, **args):
        return getattr(self.__analyzer, 'analyze')(text)
