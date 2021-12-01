import os.path
import pickle

from sklearn.ensemble import RandomForestClassifier


class Config:
    DATA_DIR: str = os.path.abspath("data")
    DATASET_POLLY_PATH: str = os.path.join(DATA_DIR, "POLLY.xlsx")
    DATASET_BIAS_PATH: str = os.path.join(DATA_DIR, "bias_dataset.jsonl")
    DOCKER_IMAGE_LANGUAGE_SERVICE = "konstantinschulz/political-bias-identification:v1"
    DOCKER_PORT_CREDIBILITY = 8000
    HOST_PORT_CREDIBILITY = 8000
    LANGUAGE_SERVICE: str = "political-bias-service"
    MODELS_DIR: str = os.path.abspath("models")
    TFIDF_DIR: str = os.path.join(MODELS_DIR, "TFIDF")
    TFIDF_MODEL: RandomForestClassifier = pickle.load(open(os.path.join(TFIDF_DIR, "model.bin"), 'rb'))
    TFIDF_VECTORIZER = pickle.load(open(os.path.join(TFIDF_DIR, "vectorizer.bin"), 'rb'))
