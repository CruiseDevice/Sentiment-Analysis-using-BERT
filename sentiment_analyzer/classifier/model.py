import json

import torch
import torch.nn.functional as F
from transformers import BertTokenizer

from .sentiment_classifier import SentimentClassifier

import os

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, '..', '..', 'config.json')

with open(config_path) as json_file:
    config = json.load(json_file)


class Model:

    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(config["BERT_MODEL"])
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        model_path = os.path.join(current_dir, '..', '..', config['PRE_TRAINED_MODEL'])

        classifier = SentimentClassifier(len(config["CLASS_NAMES"]))
        classifier.load_state_dict(
            torch.load(model_path, map_location=self.device)
        )
        classifier = classifier.eval()
        self.classifier = classifier.to(self.device)

    def predict(self, text):
        encoded_text = self.tokenizer.encode_plus(
            text,
            max_length=config["MAX_SEQUENCE_LEN"],
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt',
        )
        input_ids = encoded_text['input_ids'].to(self.device)
        attention_mask = encoded_text['attention_mask'].to(self.device)

        with torch.no_grad():
            probabilities = F.softmax(self.classifier(input_ids, attention_mask), dim=1)
            confidence, predicted_class = torch.max(probabilities, dim=1)
            predicted_class = predicted_class.cpu().item()
            probabilities = probabilities.flatten().cpu().numpy().tolist()
            return (
                config["CLASS_NAMES"][predicted_class],
                confidence,
                dict(zip(config["CLASS_NAMES"], probabilities)),
            )

model = Model()

def get_model():
    return model