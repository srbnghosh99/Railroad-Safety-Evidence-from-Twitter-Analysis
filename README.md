# Railroad Trespassing and Safety: A Systematic Analysis of Twitter Data
https://doi.org/10.1016/j.cstp.2024.101154

## Overview
This is the completed version of codes for the paper "Railroad Trespassing and Safety: A Systematic Analysis of Twitter Data"
## Data
This folder contains code data_collection.ipynb is used in data collection and saved in csv file format. 
## Data Processing
The code preprocessing.py is used to preprocess data and save it in csv file format. 
## User analysis
Simple Python codes for data analysis.
## Topic modeling, Sentiment and Emotion prediction 
*We used some existing models for topic modeling, sentiment, and emotion prediction.* 

Topic modeling: "https://github.com/MaartenGr/BERTopic"

Sentiment prediction: "https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment"

Emotion prediction: "https://github.com/nikicc/twitter-emotion-recognition"

## Results
All numerical results are created in csv format
## Description of steps
The railroad-related twitter data analysis is divided into six parts:
  
  1. Data cleaning process: Remove tweets that are not related to railroad, rail, or safety.
  2. User analysis: Identify users and the type of users involved in posting rail safety-related tweets worldwide. Group the users in different subgroups. 
  3. Topic modeling: Extract topics of rail safety-related tweets.
  4. Sentiment analysis: Identify the sentiments(pos,neg,neu) of the tweets.
  5. Emotion Analysis: Identify the emotional (joy,..) of tweets.
  6. Hashtags and Mention analysis: Extract hashtags and mentions from tweets and utilize that information for extracting organizational and geographical information. 
