import os
import sys

#Sparse matrix implementation
from scipy.sparse import csr_matrix
from Vocab import Vocab
import numpy as np
from collections import Counter

np.random.seed(1)

class IMDBdata:
    def __init__(self, directory, vocab=None):
        """ Reads in data into sparse matrix format """
        #print directory
        pFiles = os.listdir("%s/pos" % directory)
        nFiles = os.listdir("%s/neg" % directory)

        if not vocab:
            self.vocab = Vocab()
        else:
            self.vocab = vocab

        #For csr_matrix (see http://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix)
        
        self.X_reviews = []
        X_values = []
        X_row_indices = []
        X_col_indices = []
        Y = []

        #Read positive files
        for i in range(len(pFiles)):
            f = pFiles[i]
            lines = ""
            for line in open("%s/pos/%s" % (directory, f)):
                lines += line
                wordCounts = Counter([self.vocab.GetID(w.lower()) for w in line.split(" ")])
                for (wordId, count) in wordCounts.items():
                    if wordId >= 0:
                        X_row_indices.append(i)
                        X_col_indices.append(wordId)
                        X_values.append(count)
            Y.append(+1.0)
            self.X_reviews.append(lines)

        #Read negative files
        for i in range(len(nFiles)):
            f = nFiles[i]
            lines = ""
            for line in open("%s/neg/%s" % (directory, f)):
                lines += line
                wordCounts = Counter([self.vocab.GetID(w.lower()) for w in line.split(" ")])
                for (wordId, count) in wordCounts.items():
                    if wordId >= 0:
                        X_row_indices.append(len(pFiles)+i)
                        X_col_indices.append(wordId)
                        X_values.append(count)
            Y.append(-1.0)
            self.X_reviews.append(lines)
            
        self.vocab.Lock()

        #Create a sparse matrix in csr format
        self.X = csr_matrix((X_values, (X_row_indices, X_col_indices)), shape=(max(X_row_indices)+1, self.vocab.GetVocabSize()))        
        self.Y = np.asarray(Y)

        #Randomly shuffle
        index = np.arange(self.X.shape[0])
        np.random.shuffle(index)
        self.X = self.X[index,:]
        self.Y = self.Y[index]

if __name__ == "__main__":
    data = IMDBdata("../../data/aclImdb/train/")
    print(data.X)
