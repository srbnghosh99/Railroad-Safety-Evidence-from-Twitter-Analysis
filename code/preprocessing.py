#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:58:59 2023

@author: shrabanighosh
"""
import pandas as pd
import re
from emoji import demojize
from html import unescape
from wordsegment import segment
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# nltk.download('stopwords')

# preprocessing
def find_retweeted(tweet):
    '''This function will extract the twitter handles of retweed people'''
    return re.findall('(?<=RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)

def find_mentioned(tweet):
    '''This function will extract the twitter handles of people mentioned in the tweet'''
    return re.findall('(?<!RT\s)(@[A-Za-z]+[A-Za-z0-9-_]+)', tweet)  

def find_hashtags(tweet):
    '''This function will extract hashtags'''
    return re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet)  

def find_links(tweet):
    '''This function will extract hashtags'''
    return re.findall('(https?://[^\s]+)', tweet)

def remove_links(tweet):
    '''Takes a string and removes web links from it'''
    tweet = re.sub(r'http\S+', '', tweet) # remove http links
    tweet = re.sub(r'bit.ly/\S+', '', tweet) # rempve bitly links
    tweet = tweet.strip('[link]') # remove [links]
    return tweet

def remove_users(tweet):
    '''Takes a string and removes retweet and @user information'''
    tweet = re.sub('(RT\s@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet) # remove retweet
    tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet) # remove tweeted at
    tweet = re.sub(r'\n', '', tweet)  # remove newlines
    return tweet

def clean_text(tweet):
    www_exp = r'www.[^ ]+'
    http_exp = r'https?[^\s]+'
    text = re.sub('|'.join((www_exp, http_exp)), r'', tweet)
    text = unescape(text)
    text = re.sub(r'@[\w\-]+', r'', text)
    text = re.sub(r'#([\w\-]+)', r'', text) 
    text = demojize(text, delimiters=(' :', ': '))
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\\n', '', text)  # remove newlines
    return text.strip()

def lower_case(tweet):
    return tweet.lower()




# cleaning master function
def clean_tweet(tweet, bigrams=False):
    my_stopwords = nltk.corpus.stopwords.words('english')
    word_rooter = nltk.stem.snowball.PorterStemmer(ignore_stopwords=False).stem
    my_punctuation = '!"$%&\'()*+,-./:;<=>?[\]^_`{|}~•@'
    tweet = remove_users(tweet)
    tweet = remove_links(tweet)
    tweet = tweet.lower() # lower case
    tweet = re.sub('['+my_punctuation + ']+', ' ', tweet) # strip punctuation
    tweet = re.sub('\s+', ' ', tweet) #remove double spacing
    tweet = re.sub('([0-9]+)', '', tweet) # remove numbers
    tweet_token_list = [word for word in tweet.split()
                            if word not in my_stopwords] # remove stopwords

    # tweet_token_list = [word_rooter(word) if '#' not in word else word
    #                     for word in tweet_token_list] # apply word rooter
    if bigrams:
        tweet_token_list = tweet_token_list+[tweet_token_list[i]+'_'+tweet_token_list[i+1]
                                            for i in range(len(tweet_token_list)-1)]
    tweet = ' '.join(tweet_token_list)
    return tweet
    

def parse_args():
   
    parser = argparse.ArgumentParser(description="Read File")

    parser.add_argument("--filename",type = str)
    
    return parser.parse_args()

def main():
    inputs=parse_args()
    print(inputs.filename)
    df = pd.read_csv(inputs.filename)
    print(df.shape)
    print(df.columns)
    # print(df)
    df['retweeted'] = df.text.apply(find_retweeted)
    df['mentioned'] = df.text.apply(find_mentioned)
    df['hashtags'] = df.text.apply(find_hashtags)
    df['links'] = df.text.apply(find_links)
    df['clean_text'] = df.text.apply(clean_text)
    df['clean_tweet'] = df.clean_text.apply(clean_tweet)
    df['clean_tweet']=df['clean_tweet'].fillna("")
    df['lower_text'] = df.text.apply(lower_case)
    df = df.dropna(subset=['clean_tweet'])
    # df1 =  df.drop_duplicates(subset = "clean_tweet").reset_index()
    df = df[['id', 'conversation_id',
    'referenced_tweets.replied_to.id', 'referenced_tweets.retweeted.id',
    'referenced_tweets.quoted.id', 'author_id', 'in_reply_to_user_id',
    'retweeted_user_id', 'quoted_user_id', 'created_at', 'text', 'source',
    'public_metrics.like_count', 'public_metrics.quote_count',
    'public_metrics.reply_count', 'public_metrics.retweet_count',
    'author.id', 'author.created_at', 'author.username', 'author.name',
    'author.description', 'author.entities.description.cashtags',
    'author.entities.description.hashtags',
    'author.entities.description.mentions', 'retweeted', 'mentioned',
    'hashtags', 'links', 'clean_text', 'clean_tweet', 'lower_text']]
    df.to_csv("./cleaned_tweet.csv")
    print("file size",df.shape)
    print("file save as clean_tweet.csv")
    print(df)
  

if __name__ == '__main__':
    main()
