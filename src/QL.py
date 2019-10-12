import pandas as pd
import numpy as np
import re
import nltk
from utils.utils import *
import time
from ql_score import ql_score
import pickle

class QL:
    alpha = 0.5
    mu=1500.

    _inverted_index = {}
    
    # data_root = './'

    # _term_stats_path = data_root + 'clueweb_stats/term_stats.pkl'
    # _term_stats_porter_path = data_root + 'clueweb_stats/term_stats.porter.pkl'
    # _term_stats_krovetz_path = data_root + 'clueweb_stats/term_stats.krovetz.pkl'
    # _doc_stats_path = data_root + 'clueweb_stats/doc_lengths'
    # _index_path = data_root + 'data/topic_indexes/{}.pkl'
    
    _mean_doc_len = 770.4786222801615
    _total_docs = 33836981
    _total_terms = 0
    
    
    def __init__(self, do_stemming, do_stopword_removal, data_root = './', load_stats=True):
        self.do_stemming = do_stemming
        self.do_stopword_removal = do_stopword_removal
        self.data_root = data_root
        self._stopwords = nltk.corpus.stopwords.words('english')

        self._term_stats_path = self.data_root + 'clueweb_stats/term_stats.pkl'
        self._term_stats_porter_path = self.data_root + 'clueweb_stats/term_stats.porter.pkl'
        self._term_stats_krovetz_path = self.data_root + 'clueweb_stats/term_stats.krovetz.pkl'
        self._doc_stats_path = self.data_root + 'clueweb_stats/doc_lengths'
        self._index_path = self.data_root + 'topic_indexes/{}.pkl'

        if load_stats and self.do_stemming:
            self._term_stats = pd.read_pickle(self._term_stats_krovetz_path)[1].to_dict()
        elif load_stats:
            self._term_stats = pd.read_pickle(self._term_stats_path)[1].to_dict()   
        
        for k in self._term_stats:
            self._total_terms += self._term_stats[k]
        
        if self.do_stopword_removal:
            for stopw in self._stopwords:
                self._total_terms -= self._term_stats[stopw] if stopw in self._term_stats else 0

    
    def _stopword_removal(self, tokens):    
        return [word for word in tokens if word not in self._stopwords]
    
    
    def load_doc_stats(self):
        doc_lengths = pd.read_csv(self._doc_stats_path, sep='\t', header=None)
        self._mean_doc_len = doc_lengths[2].mean()
        self._total_docs = len(doc_lengths.index)
        
    
    def load_topic_index(self, topic_id):
        with open(self._index_path.format(topic_id), 'rb') as inp:
            self._inverted_index = pickle.load(inp)
        if self.do_stopword_removal:            
            for doc in self._inverted_index:
                for stopw in self._stopwords:
                    if stopw in self._inverted_index[doc]['terms']:
                        self._inverted_index[doc]['length'] -= self._inverted_index[doc]['terms'][stopw]
        
        
    def update_query_lang_model(self, query, question, answer):   
        output = {}
        
        query_tokens, qlen = self._preprocess(query)
        if type(question) == str:
            other_tokens, other_len = self._preprocess(question + ' ' + answer)
        else:
            other_tokens, other_len = self._preprocess(question + answer)
#         answer_tokens, ans_len = self._preprocess(answer)

        all_tokens = set(list(query_tokens.keys()) + list(other_tokens.keys()))        
        
        for t in all_tokens:
            try:
                qfreq = float(query_tokens[t]) / qlen
            except KeyError:
                qfreq = 0
            try:
                qafreq = float(other_tokens[t]) / other_len
            except KeyError:
                qafreq = 0            
            output[t] = self.alpha * qfreq + (1 - self.alpha) * qafreq                       
#             print(t, output[t])
        
        self._query_lm = output
    
    
    def _preprocess(self, text):
        if type(text) == str:
            if self.do_stemming:
                text_tokens = tokenize_and_stem(text)           
            else:
                text_tokens = tokenize_only(text)          
            
            if self.do_stopword_removal:
                text_tokens = self._stopword_removal(text_tokens) 
        else:
            text_tokens = text                                  
        
        output = dict()
        for t in text_tokens:
            if t not in output:
                output[t] = 0.
            output[t] += 1.
        
        return output, len(text_tokens)
    
    
    def _add_doc_to_inverted_index_if_not_existing(self, document_id, document):
        if document_id not in self._inverted_index:
            document_tokens, length = self._preprocess(document)
            self._inverted_index[document_id] = {'terms': document_tokens,
                                                 'length': length}
#             try:
# #                 print(document_tokens)
#                 self._inverted_index[document_id]['terms'] = document_tokens
#             except KeyError:
#                 self._inverted_index[document_id]['terms'] = {}
#             self._inverted_index[document_id]['length'] = len(document_tokens)
    
    
    def get_result_list(self):
        output = []
        for doc_id in self._inverted_index:        
            output.append((doc_id, self.get_interpolated_score(doc_id))) 
        return output
    
        
    def get_result_df(self, topk, query_id):        
        df = pd.DataFrame(self.get_result_list()).sort_values(1, ascending=False).head(topk)
        df['record_id'] = query_id
        return df

    
    def get_interpolated_score(self, document_id):       
        doc_inf  = self._inverted_index[document_id]        
        doc_len = doc_inf['length']
        
        score = 0.
        for t in self._query_lm:    
            try:
                dfreq = doc_inf['terms'][t]
            except KeyError:
                dfreq = 0
            try:
                nq = self._term_stats[t]
            except KeyError:
                nq = 0.
#             qafreq = float(other_tokens.count(t)) / len(other_tokens)
# #             print(t, qfreq, qafreq)
            
            
# #             q_score = self.alpha * qfreq + (1 - self.alpha) * qafreq
# #             print('qscore', q_score)
#             d_score = float(dfreq) / (self.mu + doc_len)
#             d_score += (self.mu / (self.mu + doc_len)) * (float(nq) / self._total_terms)
# #             print('dscore',d_score)
#             if d_score > 0:
#                 score += q_score * np.log(d_score)
#             else:
#                 print('This terms returns zero document frequency: ', t)    nq = 0 
                
            q_score = self._query_lm[t] #float(query_tokens.count(t)) / len(query_tokens)                   
#             
            score += ql_score.ql_score_f(q_score, dfreq, self.mu, doc_len, nq, self._total_terms)        

#             qafreq = float(other_tokens.count(t)) / len(other_tokens)
# #             print(t, qfreq, qafreq)
            
            
# #             q_score = self.alpha * qfreq + (1 - self.alpha) * qafreq
# #             print('qscore', q_score)

#             print(dfreq,self.mu, doc_len,nq, self._total_terms)
# #old
#             d_score = float(dfreq) / (self.mu + doc_len)
#             d_score += (self.mu / (self.mu + doc_len)) * (float(nq) / self._total_terms)

#             d_score = (float(dfreq) + (self.mu *(float(nq)/self._total_terms))/(doc_len+)            

# #             print('dscore',d_score)
#             print(d_score)
#             if d_score > 0:
#                 score += q_score * np.log(d_score)
#             else:
#                 print('This terms returns zero document frequency: ', t)
        
        return score