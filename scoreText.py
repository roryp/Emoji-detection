# -*- coding: utf-8 -*-

""" Use DeepMoji to score texts for emoji distribution.

The resulting emoji ids (0-63) correspond to the mapping
in emoji_overview.png file at the root of the DeepMoji repo.

Writes the result to a csv file.
"""
from __future__ import print_function, division
import example_helper
import json
import csv
import numpy as np
import tensorflow as tf
import emoji
from localdeepmoji.sentence_tokenizer import SentenceTokenizer
from localdeepmoji.model_def import deepmoji_emojis

PRETRAINED_PATH = './model/deepmoji_weights.hdf5'
VOCAB_PATH = './model/vocabulary.json'

maxlen = 30
batch_size = 32

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

print('Tokenizing using dictionary from {}'.format(VOCAB_PATH))
with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)
st = SentenceTokenizer(vocabulary, maxlen)

model = deepmoji_emojis(maxlen, PRETRAINED_PATH)
model._make_predict_function()
graph = tf.get_default_graph()

def score(sentence):

    TEST_SENTENCES = [sentence]

    tokenized, _, _ = st.tokenize_sentences(TEST_SENTENCES)

    print('Loading model from {}.'.format(PRETRAINED_PATH))
    model.summary()

    # model.save("deepmoji_akif")
    
    with graph.as_default():
        print('Running predictions.')
        prob = model.predict(tokenized)

        # Find top emojis for each sentence. Emoji ids (0-63)
        # correspond to the mapping in emoji_overview.png
        # at the root of the DeepMoji repo.
        # print('Writing results to {}'.format(OUTPUT_PATH))
        scores = []
        for i, t in enumerate(TEST_SENTENCES):
            t_tokens = tokenized[i]
            t_score = {
                'sentence' : [t],
                'prob' : prob[i],
                'top5' : top_elements(prob[i], 5)
            }
            scores.append(t_score)
            print(t_score)

        return scores;

    # with open(OUTPUT_PATH, 'wb') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    #     writer.writerow(['Text', 'Top5%',
    #                     'Emoji_1', 'Emoji_2', 'Emoji_3', 'Emoji_4', 'Emoji_5',
    #                     'Pct_1', 'Pct_2', 'Pct_3', 'Pct_4', 'Pct_5'])
    #     for i, row in enumerate(scores):
    #         try:
    #             writer.writerow(row)
    #         except Exception:
    #             print("Exception at row {}!".format(i))
