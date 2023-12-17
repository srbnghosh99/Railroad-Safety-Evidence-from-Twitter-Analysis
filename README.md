# Railroad Trespassing and Safety: A Systematic Analysis of Twitter Data

## Overview
This is the completed version of codes for the paper "Railroad Trespassing and Safety: A Systematic Analysis of Twitter Data"
## Data
This folder contains code data_collection.ipynb is used in data collection and save in csv file format. 
## Data Processing
The code preprocessing.py is used preprocess data and save in csv file format. 
# User analysis
Simple Python codes for data analysis.
## Topic, Sentiment, Emotion and 
We used some existing models for topic modeling, sentiment and emotion prediction. 
Topic modeling: "https://github.com/MaartenGr/BERTopic"
Sentiment prediction: "https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment", 
Emotion prediction "https://github.com/nikicc/twitter-emotion-recognition"


## Results
All numerical results can be found here in .npy format.
## Model
The Python code for simulation of clique networks and their analysis.



The railroad safety related twitter data analysis divided into six parts:
  
  1. Data cleaning process: to remove tweets which are not related to railroad, rail, railsafety
  2. User analysis: identify users and type of users involved into posting rail safety related tweets from all over the world
  3. Topic modeling: extract the topics on railsafety related tweets
  4. Sentiment analysis: identify the sentments(pos,neg,neu) of the tweets
  5. Emotion Analysis: identify emotional (joy,..) of tweets
  6. Hashtags and Mention analysis: extract hashtags and mentions from tweets and utilize that information for exracting organizational and geographical informaiton 
