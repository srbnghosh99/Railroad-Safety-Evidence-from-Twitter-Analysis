#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:31:38 EDT 2023

@author: shrabanighosh
"""
import pandas as pd

df = pd.read_csv("/content/tweet_topic_info_37K.csv")
irr = pd.read_csv("/content/get_topic_info_latest 2.csv")
irr["Comments"]=irr["Comments"].values.astype(str)
# irr = irr[0:178]
# irr.shape
# com = str(All tweets are relevant)
irr_topic = irr[~irr["Comments"].str.contains('All tweets are relevant')]
irr_topic_list =  irr_topic['Topic'].tolist()

irr = pd.read_csv("/content/get_topic_info_latest 2.csv")
irr["Comments"]=irr["Comments"].values.astype(str)
irr = irr[0:178]
# irr.shape
# com = str(All tweets are relevant)
irr_topic = irr[~irr["Comments"].str.contains('All tweets are relevant')]
irr_topic_list =  irr_topic['Topic'].tolist()

searchwords = ['baseball','ball','basketball','sports','football',
               'innings','inning','game','match','score','monarchs',
               'saltdogs','hoppers','coach','coaches','players',
               'bombers','rookie','crewe','bradford','cheifs',
               'lament','hoosic','panthers','gonuts','wingnuts',
               'redhawks','blackhawks','whitehall','jumponthetra',
               'waynoka','garrett','fulton','sparksride','sparks',
               'airhogs','gamechanger','newton','cougars',
               'railcats','altoona','brunswick','concert','durand',
               'hornets','cleburne','soccer','hockey','softball','crrbaseball','wedigbaseball',
               'busco_baseball','luersbaseball','roster','ladyrr','eagles','victory','knights',
                'horseshoe','milkmen','unemployment','retirement']

appended_data1 = []
# irr_topic_list = list(range(177,416))
for i in irr_topic_list:
    df1 = df[df["Topic"] == i]
    df1["clean_text"] = df1["clean_text"].astype(str)
    # print(df1)
    temp = df1[~df1['clean_text'].str.contains('|'.join(searchwords))]
    # print(temp)
    if(temp.shape[0] > 1):
      appended_data1.append(temp)
# print(len(appended_data))

appended_data2 = []

irr_topic_list = list(range(177,416))
for i in irr_topic_list:
    df1 = df[df["Topic"] == i]
    df1["clean_text"] = df1["clean_text"].astype(str)
    # print(df1)
    temp = df1[~df1['clean_text'].str.contains('|'.join(searchwords))]
    # print(temp)
    if(temp.shape[0] > 1):
      appended_data2.append(temp)

appended_data3 = []
rel_topic = irr[irr["Comments"].str.contains('All tweets are relevant')]
rel_topic_list =  rel_topic['Topic'].tolist()
for i in rel_topic_list:
    df1 = df[df["Topic"] == i]
    appended_data3.append(df1)


appended_data1 = pd.concat(appended_data1) 
appended_data2 = pd.concat(appended_data2) 
appended_data3 = pd.concat(appended_data3) 
appended_data1.shape,appended_data2.shape,appended_data3.shape
frames = [appended_data1, appended_data2, appended_data2]
result = pd.concat(frames)

result.to_csv('removed_tweets.csv')

