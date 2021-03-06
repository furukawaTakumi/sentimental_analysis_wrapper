
from sentimental_analyzer import SentimentalAnalyzer

asari = SentimentalAnalyzer("asari")
print(asari.analyze("なんだよもう〜"))

bert = SentimentalAnalyzer("bert")
print(bert.analyze("最低だね"))
print(bert.analyze("なんだよもう〜"))

oseti = SentimentalAnalyzer("oseti")
print(oseti.analyze("なんだよもう〜"))
print(oseti.analyze("遅刻したけど楽しかったし嬉しかった。"))
print(oseti.analyze("誕生日プレゼント嬉しいな。"))

kamaboko = SentimentalAnalyzer("kamaboko")
print(kamaboko.analyze("なんだよもう〜"))
print(kamaboko.analyze("遅刻したけど楽しかったし嬉しかった。"))
print(kamaboko.analyze("誕生日プレゼント嬉しいな。"))
