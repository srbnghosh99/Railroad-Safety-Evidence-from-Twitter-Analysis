#os.environ["TOKENIZERS_PARALLELISt()"] = "false"
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
import hdbscan
import umap
import flair
from flair.embeddings import TransformerDocumentEmbeddings
from sentence_transformers import SentenceTransformer
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def topic_modeling(filename):
    df = pd.read_csv(filename)
    df['clean_tweet']=df['clean_tweet'].fillna("")
    docs = df.clean_tweet.unique()
    print(df.shape)
    #docs = df.clean_tweet
    vectorizer_model = CountVectorizer(ngram_range=(1, 2), stop_words="english")
    #roberta = TransformerDocumentEmbeddings('roberta-base')
    sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
    model = BERTopic(
        embedding_model=sentence_model,
        vectorizer_model=vectorizer_model,
        top_n_words=10,
        language='english', calculate_probabilities=True,
        verbose=True
    )
    # model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
    #model = BERTopic.load("model_full")
    topics, probs = model.fit_transform(docs)
    tweet_topic =[]
    prob = []
    for x in probs:
      y = x.tolist()
      max_index = y.index(max(y))
      tweet_topic.append(max_index)
      prob.append(max(y))

    for idx, x in enumerate(topics):
      prob1.append(probs[idx][x])
        

    #model.save("model_full1")
    #model = BERTopic.load("model_full")
    info_df = model.get_topic_info()
    info_df.to_csv('get_topic_info_(10).csv')

    top = pd.DataFrame({'Topic Lable':tweet_topic,
        'Prob':prob})

    top.to_csv('tweet_topic_with_prob_10.csv')
    df1 = df.drop_duplicates(subset=['clean_tweet'])
    #tweet_topic_df = pd.DataFrame(topics)
    #tweet_topic_df.to_csv("topics_df_10.csv")
    df_time = df[['created_at', 'text','clean_tweet']]
    df_time.drop_duplicates(subset='clean_tweet').reser_index()
    timestamps = df_time.created_at.to_list()
    tweets = df_time.clean_tweet.to_list()
    topics_over_time = model.topics_over_time(tweets, topics, timestamps, nr_bins=20)

    fig = model.visualize_topics_over_time(topics_over_time)
    fig.write_html("topics_over_time.html")

    print(top.shape)
    print(info_df.shape)
    results = pd.DataFrame({"Doc": docs, "Topic": topics})
    result.to_csv("docs_vs_topic.csv")
    print("execution ended")


def parse_args():
    parser = argparse.ArgumentParser(description="Read File")
    parser.add_argument("--filename",type = str)
    return parser.parse_args()

def main():
    inputs=parse_args()
    print(inputs.filename)
    topic_modeling(inputs.filename)
  

if __name__ == '__main__':
    main()
