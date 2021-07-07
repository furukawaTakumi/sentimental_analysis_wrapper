
from transformers import pipeline,AutoTokenizer,BertTokenizer,AutoModelForSequenceClassification,BertJapaneseTokenizer, BertForMaskedLM

class Analyzer:
    def __init__(self) -> None:
        model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
        tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        self.nlp = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)

    def analyze(self, text, **args):
        judge = self.nlp(text)[0]
        return self.__reconstruction(judge, text)

    def __reconstruction(self, judge, text):
        result = {}
        result['text'] = text
        self.__inflate(judge['label'], judge['score'], result)
        return result
        
    def __inflate(self, top_class: str, score: float, result: dict):
        top_label = 'positive' if top_class == 'ポジティブ' else 'negative'
        result['top_class'] = top_label
        pos_class = {
            'class_name': 'positive',
            'confidence': score if top_label == 'positive' else 1 - score
        }
        neg_class = {
            'class_name': 'negative',
            'confidence': score if top_label == 'negative' else 1 - score
        }
        result['classes'] = [
            pos_class,
            neg_class
        ]