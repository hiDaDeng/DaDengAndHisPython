import pandas as pd
from pysentiment.base import STATIC_PATH, BaseDict


class HIV4(BaseDict):
    """
    Dictionary class for Harvard IV-4. 
    See also http://www.wjh.harvard.edu/~inquirer/
    
    The terms for the dictionary are stemmed by the default tokenizer.
    """
    
    PATH = '%s/HIV-4.csv' % STATIC_PATH
    
    def init_dict(self):
        data = pd.read_csv(self.PATH, dtype='category')
        self._posset = set(data.query('Positiv == "Positiv"')['Entry'].apply(self.tokenize_first).dropna())
        self._negset = set(data.query('Negativ == "Negativ"')['Entry'].apply(self.tokenize_first).dropna())
