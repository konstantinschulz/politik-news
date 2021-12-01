from enum import Enum


class BiasLabel(Enum):
    unknown = 0
    far_left = 1
    center_left = 2
    center = 3
    center_right = 4
    far_right = 5


class Model(Enum):
    BERT = "bert"
    TFIDF = "tfidf"
