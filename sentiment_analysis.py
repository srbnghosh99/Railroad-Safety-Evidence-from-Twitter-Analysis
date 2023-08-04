from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import pandas as pd
# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []


    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

# Tasks:
# emoji, emotion, hate, irony, offensive, sentiment
# stance/abortion, stance/atheism, stance/climate, stance/feminist, stance/hillary

task='sentiment'
#MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
MODEL = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)

# download label mapping
labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
#mapping_link = f"tweeteval-main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]

# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
#model.save_pretrained(MODEL)
df = pd.read_csv("revised/clean_senti.csv")
#df1 = df.drop_duplicates(subset=['tweet_senti'])
batch_sentences = df["clean_senti"].tolist()

positive = []
neutral = []
negative = []
batch_size = 128
num_samples = len(batch_sentences)
num_batches = num_samples / batch_size
num_batches = round(num_batches)

for i in range(num_batches):
    print(i)
    start_idx = i * batch_size
    end_idx = (i + 1) * batch_size
    if end_idx > num_samples:
        end_idx = num_samples
    x_batch = batch_sentences[start_idx:end_idx]
    encoded_input = tokenizer(x_batch, padding=True, truncation=True, return_tensors="pt")
    output = model(**encoded_input)
    for i in range(0,len(x_batch)):
      scores = output[0][i].detach().numpy()
      #print(len(scores))
      scores = softmax(scores)
      positive.append(scores[2])
      neutral.append(scores[1])
      negative.append(scores[0])

#df1["positive"] = positive
#df1["neutral"] = neutral
#df1["negative"] = negative

print(len(positive))
print(len(negative))
#encoded_input = tokenizer(batch_sentences, padding=True, truncation=True, return_tensors="pt")
#output = model(**encoded_input)
#logis_output=output[0].tolist()
df['positive'] = positive
df['negative']=negative
df['neutral']=neutral

#df2 = pd.DataFrame(positive,negative,neutral,columns =['positive','negative','neutral'])
df.to_csv("revised/score_clean_senti.csv")
