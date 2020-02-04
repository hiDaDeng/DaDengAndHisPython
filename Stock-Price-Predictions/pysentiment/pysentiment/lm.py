import pandas as pd
from pysentiment.base import STATIC_PATH, BaseDict


class LM(BaseDict):
    """
    Dictionary class for
    Loughran and McDonald Financial Sentiment Dictionaries.
    
    See also https://www3.nd.edu/~mcdonald/Word_Lists.html
    
    The terms for the dictionary are stemmed by the default tokenizer.
    """
    
    PATH = '%s/LM.csv' % STATIC_PATH
    
    def init_dict(self):
        data = pd.read_csv(self.PATH)
        self._posset = set(data.query('Positive > 0')['Word'].apply(self.tokenize_first).dropna())
        self._negset = set(data.query('Negative > 0')['Word'].apply(self.tokenize_first).dropna())
