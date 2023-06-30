import pandas as pd
import numpy as np
df = pd.read_csv("./cleaned_tweet.csv")
# df = pd.read_csv("./original_tweets.csv")
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
print(len(searchwords))

df2 = df.loc[~df['lower_text'].str.contains("|".join(searchwords), na=False)]
print(df2.shape)
df2 = df2[['id', 'conversation_id',
    'referenced_tweets.replied_to.id', 'referenced_tweets.retweeted.id',
    'referenced_tweets.quoted.id', 'author_id', 'in_reply_to_user_id',
    'retweeted_user_id', 'quoted_user_id', 'created_at', 'text', 'source',
    'public_metrics.like_count', 'public_metrics.quote_count',
    'public_metrics.reply_count', 'public_metrics.retweet_count',
    'author.id', 'author.created_at', 'author.username', 'author.name',
    'author.description', 'author.entities.description.cashtags',
    'author.entities.description.hashtags',
    'author.entities.description.mentions', 'retweeted', 'mentioned',
    'hashtags', 'links', 'clean_text', 'clean_tweet']]
df2 = df2[~df2['clean_tweet'].isnull()]
# df2.to_csv("removed_tweets_without_original_text.csv")
df2.to_csv("removed_tweets.csv")
# print(~df['clean_tweet'].str.contains("|".join(searchwords)))
print(df2[~df2['clean_tweet'].isnull()])
# print(df[df['text'].isnull()])