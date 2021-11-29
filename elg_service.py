from typing import Dict, Union, Tuple, Any

from elg import FlaskService
from elg.model import ClassificationResponse
from BiasPredictor import biasPredictor
from config import Config
from enums import Model


def predict(text: str):
    predictor = biasPredictor(Model.TFIDF)
    explain = False
    prediction: Union[Dict[str, float], Tuple[Dict[str, float], Any]] = predictor.predict(text=text, explain=explain)
    return prediction


class PoliticalBiasService(FlaskService):

    def convert_outputs(self, content: str) -> ClassificationResponse:
        bias_dict: Union[Dict[str, float], Tuple[Dict[str, float], Any]] = predict(content)
        return ClassificationResponse(classes=[{"class": k, "score": v} for k, v in bias_dict.items()])

    def process_text(self, content: Any) -> ClassificationResponse:
        return self.convert_outputs(content.content)


pbs: PoliticalBiasService = PoliticalBiasService(Config.LANGUAGE_SERVICE)
app = pbs.app
