from .Bert import Bert
import torch

from transformers.tokenization_bert_japanese import BertJapaneseTokenizer
from torchtext.legacy import data  # torchtextを使用
import pickle
from tqdm import tqdm

MAX_SEQ_LEN = 256
class PredictTaskExecutor:

    def predict_task_executor(self, net, sentence_batchs):
        net.eval()
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        net = net.to(device)

        predict_list  = []
        for batch in tqdm(sentence_batchs): 
            inputs = batch.Text[0].to(device)
            with torch.set_grad_enabled(False):
                outputs = net(inputs)
                pred2 = torch.softmax(outputs, 1)
                predict_list.append(pred2)

        return predict_list

    def tokenizer_512(self, input_text):
        tokenizer = BertJapaneseTokenizer.from_pretrained(
            './KusorepCalculater/Bert/Data/tokenizer', mecab_kwargs={"mecab_option": "-d /root/local/lib/mecab/dic/mecab-ipadic-neologd"})
        return tokenizer.encode(input_text, max_length=MAX_SEQ_LEN, return_tensors='pt')[0]

    def make_batch(self, sentences):
        TEXT = data.Field(sequential=True, tokenize=self.tokenizer_512, use_vocab=False, lower=False,include_lengths=True, batch_first=True, fix_length=MAX_SEQ_LEN, pad_token=0)
        fields = [('text', TEXT)]
        batch_size = 16
        
        examples = []
        for sentence in sentences:
            examples += [data.Example.fromlist([sentence], fields)]
        train_data = data.Dataset(examples, fields)
        sentence_batch = data.Iterator(train_data, batch_size=batch_size, train=False, sort=False)
        return sentence_batch

    def main(self, sentences):

        sentence_batch = self.make_batch(sentences)
        model = Bert()

        model_path = "KusorepCalculater/Bert/Data/best_epoche5"

        model.load_state_dict(torch.load(
            model_path, map_location=torch.device('cpu')))

        return self.predict_task_executor(model, sentence_batch)
