from .Bert import Bert
import torch

from transformers.tokenization_bert_japanese import BertJapaneseTokenizer

import pickle

MAX_SEQ_LEN = 256
class PredictTaskExecutor:

    def predict_task_executor(self, net, sentence):
        net.eval()
        tokenizer = BertJapaneseTokenizer.from_pretrained(
            '/mnt/lambda/variable/tokenizer', mecab_kwargs={"mecab_option": "-d /mnt/lambda/lib/mecab/dic/mecab-ipadic-neologd"})


        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        sentence = tokenizer.encode(sentence, return_tensors='pt').to(device)
        tokens = torch.zeros(MAX_SEQ_LEN, dtype=torch.long).to(device)
        net = net.to(device)
        for i in range(len(sentence[0])):
            tokens[i] = round(sentence[0][i].item())

        with torch.set_grad_enabled(False):
            outputs = net(tokens.unsqueeze(0))
            _, preds = torch.max(outputs, 1)  # ラベルを予測
            pred2 = torch.softmax(outputs, 1)

        return pred2[0].tolist()

    def main(self, sentence):

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        model = Bert()

        model_path = "/mnt/lambda/model/best_epoche20"

        model.load_state_dict(torch.load(
            model_path, map_location=torch.device('cpu')))

        return self.predict_task_executor(model, sentence)
