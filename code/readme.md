## How to execute Python files?

## Data preprocessing 
*This step includes stemming, lemmatization, removing punctuation, stop words, links, numeric values, etc.*

python3 proprocessing.py --filename filename(csv format)

## Data cleaning
*This step includes removing irreverent tweets using keywords*

python3 remove_keywords.py 

## User analysis 
*This step includes  irreverent tweets using keywords*

python3 user_analysis.py --filename filename(csv format)

## Emotion detection, sentiment prediction, topic modeling

pip install -r emotion_detection_requirements.txt

python3 emotion_detction.py --filename inputfilename --outputfilename filename (csv format)

python3 topic_modeling.py --filename inputfilename --outputfilename filename (csv format)

python3 twitter-emotion-recognition-master/emotion_detect.py --filename inputfilename --outputfilename filename (csv format)

## Hashtag and mention analysis
*This step used hashtag(#) and mention(@) in the tweets to extract geographical location and organizations information*

python3 hashtag_mention_analysis.py --filename inputfilename --outputfilename filename (csv format)

