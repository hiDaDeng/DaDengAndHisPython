import sys
from scipy.sparse import csr_matrix
import numpy as np
from Eval import Eval
from math import log, exp
import time
from imdb import IMDBdata

class NaiveBayes:
    def __init__(self, data, ALPHA=1.0):
        self.ALPHA = ALPHA
        self.data = data # training data
        #TODO: Initalize parameters
        # self.vocab_len = 
        # self.count_positive = 
        # self.count_negative = 
        # self.num_positive_reviews = 
        # self.num_negative_reviews = 
        # self.total_positive_words = 
        # self.total_negative_words = 
        # self.P_positive = 
        # self.P_negative = 
        # self.deno_pos = 
        # self.deno_neg =
        self.Train(data.X,data.Y)

    # Train model - X are instances, Y are labels (+1 or -1)
    # X and Y are sparse matrices
    def Train(self, X, Y):
        #TODO: Estimate Naive Bayes model parameters
        positive_indices = np.argwhere(Y == 1.0).flatten()
        negative_indices = np.argwhere(Y == -1.0).flatten()
        
        self.num_positive_reviews = 1
        self.num_negative_reviews = 1
        
        self.count_positive = np.ones([1,X.shape[1]])
        self.count_negative = np.ones([1,X.shape[1]])
        
        self.total_positive_words = 1
        self.total_negative_words = 1
        
        self.deno_pos = 1.0
        self.deno_neg = 1.0
        
        # self.count_positive = 1
        # self.count_negative = 1
        
        return

    # Predict labels for instances X
    # Return: Sparse matrix Y with predicted labels (+1 or -1)
    def PredictLabel(self, X):
        #TODO: Implement Naive Bayes Classification
        self.P_positive = 0
        self.P_negative = 0
        pred_labels = []
        
        sh = X.shape[0]
        for i in range(sh):
            z = X[i].nonzero()
            for j in range(len(z[0])):
                # Look at each feature
                pass
                
            if True:            # Predict positive
                pred_labels.append(1.0)
            else:               # Predict negative
                pred_labels.append(-1.0)
        
        return pred_labels

    def LogSum(self, logx, logy):   
        # TO DO: Return log(x+y), avoiding numerical underflow/overflow.
        m = max(logx, logy)        
        return m + log(exp(logx - m) + exp(logy - m))

    # Predict the probability of each indexed review in sparse matrix text
    # of being positive
    # Prints results
    def PredictProb(self, test, indexes):
    
        for i in indexes:
            # TO DO: Predict the probability of the i_th review in test being positive review
            # TO DO: Use the LogSum function to avoid underflow/overflow
            predicted_label = 0
            for j in range(len(z[0])):
                row_index = i
                col_index = z[1][j]
            
            predicted_prob_positive = 0.5
            predicted_prob_negative = 0.5
            
            if sum_positive > sum_negative:
                predicted_label = 1.0
            else:
                predicted_label = -1.0
            
            #print test.Y[i], test.X_reviews[i]
            # TO DO: Comment the line above, and uncomment the line below
            print(test.Y[i], predicted_label, predicted_prob_positive, predicted_prob_negative, test.X_reviews[i])

    # Evaluate performance on test data 
    def Eval(self, test):
        Y_pred = self.PredictLabel(test.X)
        ev = Eval(Y_pred, test.Y)
        return ev.Accuracy()


if __name__ == "__main__":
    
    print("Reading Training Data")
    traindata = IMDBdata("%s/train" % sys.argv[1])
    print("Reading Test Data")
    testdata  = IMDBdata("%s/test" % sys.argv[1], vocab=traindata.vocab)    
    print("Computing Parameters")
    nb = NaiveBayes(traindata, float(sys.argv[2]))
    print("Evaluating")
    print("Test Accuracy: ", nb.Eval(testdata))

