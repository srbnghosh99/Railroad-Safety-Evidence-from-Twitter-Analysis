import os
os.environ['KERAS_BACKEND'] = 'theano'
import pandas as pd
import math
from emotion_predictor import EmotionPredictor


def emotion_prediction(inputfilename,):
    # Pandas presentation options
    pd.options.display.max_colwidth = 150   # show whole tweet's content
    pd.options.display.width = 200          # don't break columns
    # pd.options.display.max_columns = 7      # maximal number of columns



    # Predictor for Ekman's emotions in multiclass setting.
    model = EmotionPredictor(classification='plutchik', setting='mc', use_unison_model=True)

    df = pd.read_csv(inputfilename,outputfilename)
    # df = df.clean_senti.drop_duplicates().reset_index()
    df1 = df.drop_duplicates(subset=['clean_senti']).reset_index()
    print(df1.shape)
    batch_sentences = df1["clean_senti"].tolist()
    appended_data = []
    batch_size = 128
    num_samples = len(batch_sentences)
    num_batches = num_samples / batch_size
    num_batches = math.ceil(num_batches)
    for i in range(num_batches):
        #print(i)
        start_idx = i * batch_size
        end_idx = (i + 1) * batch_size
        if end_idx > num_samples:
            end_idx = num_samples
        x_batch = batch_sentences[start_idx:end_idx]
        predictions = model.predict_classes(x_batch)
        #print(predictions)
        appended_data.append(predictions)
    appended_data = pd.concat(appended_data)
    print(appended_data.shape)
    print(df1.shape)
#    appended_data.to_csv('tweet_emo_plutchik.csv')
#    df1.to_csv('cleaned_tweet_emo_plutchik.csv')
    result = pd.concat([df1, appended_data], axis = 1)
    #result = pd.concat([df1, appended_data.reindex(df1.index)], axis=1)

    print(result.shape)
    result.to_csv('output.csv')
    print("execution complete")


def parse_args():
    parser = argparse.ArgumentParser(description="Read File")
    parser.add_argument("--inputfilename",type = str)
    parser.add_argument("--outputfilename",type = str)
    return parser.parse_args()

def main():
    inputs=parse_args()
    print(inputs.filename)
    emotion_prediction(inputs.inputfilename, inputs.outputfilename)
  

if __name__ == '__main__':
    main()
