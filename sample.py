
from sentimental_analyzer import SentimentalAnalyzer

asari = SentimentalAnalyzer("asari")
bert = SentimentalAnalyzer("bert")

print(asari.analyze("なんだよもう〜"))
print(bert.analyze("最低だね"))
print(bert.analyze("なんだよもう〜"))
