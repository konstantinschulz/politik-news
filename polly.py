import json
import pandas as pd
from torch.utils.data import Dataset
from transformers import BatchEncoding

from config import Config
from enums import BiasLabel


class BiasItem:
    def __init__(self, text: str = "", label: BiasLabel = BiasLabel.unknown):
        self.label: BiasLabel = label
        self.text: str = text

    @classmethod
    def from_json(cls, json_dict: dict = None):
        return BiasItem(**json_dict)

    def to_json(self) -> str:
        return json.dumps(dict(text=self.text, label=self.label.value)) + "\n"


class BiasDataset(Dataset):
    def __getitem__(self, idx: int) -> BatchEncoding:
        with open(Config.DATASET_BIAS_PATH) as f:
            for i, line in enumerate(f.readlines()):
                if i == idx:
                    bi: BiasItem = BiasItem.from_json(json_dict=json.loads(line))
                    encodings: BatchEncoding
                    # TODO: tokenize text, add label
                    return encodings


def build_dataset():
    polly: pd.ExcelFile = pd.ExcelFile(Config.DATASET_POLLY_PATH)
    by_party_df: pd.DataFrame = pd.read_excel(polly, "by_party")
    by_column: str = "By"
    tweet_column: str = "Tweet"
    afd_df: pd.DataFrame = by_party_df[by_party_df[by_column] == "AfD"]
    linke_df: pd.DataFrame = by_party_df[by_party_df[by_column] == "Die Linke"]
    with open(Config.DATASET_BIAS_PATH, "a+") as f:
        for idx, row in afd_df.iterrows():
            f.write(BiasItem(text=row[tweet_column], label=BiasLabel.far_right).to_json())
        for idx, row in linke_df.iterrows():
            f.write(BiasItem(text=row[tweet_column], label=BiasLabel.far_left).to_json())

# build_dataset()
