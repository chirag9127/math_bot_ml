import os
import pickle
os.environ['KERAS_BACKEND'] = 'theano'

from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

from singleton import Singleton

MAX_SEQUENCE_LENGTH = 100


@Singleton
class YoutubeRelevanceModel:

    def __init__(self):
        self.tokenizer = pickle.load(open('tokenizer.p', 'rb'))
        self.model = load_model('best_model.h5')

    def predict(self, data):
        query_sequences = self.tokenizer.texts_to_sequences(data['query'])
        title_sequences = self.tokenizer.texts_to_sequences(data['title'])
        desc_sequences = self.tokenizer.texts_to_sequences(data['description'])
        query_data = pad_sequences(query_sequences, maxlen=MAX_SEQUENCE_LENGTH)
        title_data = pad_sequences(title_sequences, maxlen=MAX_SEQUENCE_LENGTH)
        desc_data = pad_sequences(desc_sequences, maxlen=MAX_SEQUENCE_LENGTH)
        preds = self.model.predict([query_data, title_data, desc_data])
        return preds


yrm = YoutubeRelevanceModel.Instance()


if __name__ == '__main__':
    data = {
        "query": ["Algebra videos", "Algebra videos", "Algebra videos"],
        "title": ["Quick Math Review to Prep for Algebra 1",
                  "Algebra - Completing the square",
                  "Algebra Basics: Solving Basic Equations Part 1 "
                  "- Math Antics"],
        "description": ["This is 1 of 4 videos I custom made for an educator "
                        "in California for an experimental 1-week video "
                        "homework program. I have only edited the "
                        "beginning and ...",
                        "Hi Algebrinos! As we progress with our problem "
                        "solving prowess, we include solving by using the "
                        "nifty method of solving quadratic equations "
                        "titled, 'Completing ...",
                        "This video shows students how to solve simple 1-step "
                        "Algebra equations involving only addition or "
                        "subtraction. Part of the Algebra Basics Series: ..."]
    }
    preds = yrm.predict(data)
    print (preds)
