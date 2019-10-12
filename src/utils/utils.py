import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
import nltk
from nltk.stem.porter import PorterStemmer
# from krovetzstemmer import Stemmer as KrovetzStemmer #TODO: uncomment after installing the krovetz setmmer.
import re
import os, shutil


def encode_id(topic_id, facet_id, hisotry_ids, question_id, with_ans):
    rec_id = '{}-{}'.format(topic_id,facet_id)
    for hid in hisotry_ids:
        rec_id += '-{}'.format(hid)
    rec_id += '-{}-{}'.format(question_id, with_ans)
    return rec_id
    
    
def decode_id(rec_id):
    tokens = rec_id.split('-')
    topic_id, facet_id, question_id, with_ans = tokens[0], tokens[1], tokens[-2], tokens[-1]
    hisotry_ids = ()
    for k in range(2,2+len(tokens)-4):    
        hisotry_ids += (tokens[k],)
    return topic_id, facet_id, hisotry_ids, question_id, with_ans


def remove_symbols(input_str):
    input_str = input_str.replace('\\','')
    return input_str


def remove_stopwords(tokens):    
    return [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    # stemmer = KrovetzStemmer()
    stemmer = PorterStemmer() # TODO: comment this and uncomment the line above after installing the krovetz stemmer
    text = text.lower()
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    text = text.lower()
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens