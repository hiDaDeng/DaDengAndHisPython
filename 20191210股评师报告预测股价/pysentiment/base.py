"""
This module contains base classes for dictionaries.
"""

import abc
import os
import numpy as np
from pysentiment.utils import Tokenizer


STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')


class BaseDict(object):
    """
    A base class for sentiment analysis. 
    For now, only 'positive' and 'negative' analysis is supported.
    
    Subclasses should implement ``init_dict``, 
    in which ``_posset`` and ``_negset`` are initialized.
    
    ``Polarity`` and ``Subjectivity`` are calculated in the same way of Lydia system.
    See also http://www.cs.sunysb.edu/~skiena/lydia/
    
    The formula for ``Polarity`` is,
    
    .. math::
    
        Polarity= \\frac{N_{pos}-N_{neg}}{N_{pos}+N_{neg}}
    
    The formula for ``Subjectivity`` is,
    
    .. math::
    
        Subjectivity= \\frac{N_{pos}+N_{neg}}{N}
    
    :type tokenizer: obj    
    :param tokenizer: An object which provides interface of ``tokenize``. 
        If it is ``None``, a default tokenizer, which is defined in ``utils``, will be assigned.
    """
    
    __metaclass__ = abc.ABCMeta

    TAG_POL = 'Polarity'
    TAG_SUB = 'Subjectivity'
    TAG_POS = 'Positive'
    TAG_NEG = 'Negative'
    
    EPSILON = 1e-6
    
    def __init__(self, tokenizer=None):
        self._posset = set()
        self._negset = set()
        if tokenizer is None:
            self._tokenizer = Tokenizer()
        else:
            self._tokenizer = tokenizer
        self.init_dict()
        
        assert len(self._posset) > 0 and len(self._negset) > 0
        
    def tokenize(self, text):
        """
        :type text: str
        :returns: list
        """

        return self._tokenizer.tokenize(text)

    def tokenize_first(self, x):
        """
        :type x: str
        :returns: str
        """
        tokens = self.tokenize(x)
        if tokens:
            return tokens[0]
        else:
            return None

    @abc.abstractmethod
    def init_dict(self):
        pass
    
    def _get_score(self, term):
        """Get score for a single term.

        - +1 for positive terms.
        - -1 for negative terms.
        - 0 for others. 
        
        :returns: int
        """
        if term in self._posset:
            return +1
        elif term in self._negset:
            return -1
        else:
            return 0
        
    def get_score(self, terms):
        """Get score for a list of terms.
        
        :type terms: list
        :param terms: A list of terms to be analyzed.
        
        :returns: dict
        """
        assert isinstance(terms, list) or isinstance(terms, tuple)
        score_li = np.asarray([self._get_score(t) for t in terms])
        
        s_pos = np.sum(score_li[score_li > 0])
        s_neg = -np.sum(score_li[score_li < 0])
        
        s_pol = (s_pos-s_neg) * 1.0 / ((s_pos+s_neg)+self.EPSILON)
        s_sub = (s_pos+s_neg) * 1.0 / (len(score_li)+self.EPSILON)
        
        return {self.TAG_POS: s_pos,
                self.TAG_NEG: s_neg,
                self.TAG_POL: s_pol,
                self.TAG_SUB: s_sub}
