import re
import spacy
import numpy as np
import pandas as pd
import argparse
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
nlp = spacy.load("en_core_web_sm")


def tag_analysis(inputfilename,outputfilename)

    df = pd.read_csv(inputfilename)
    df['OrganizationTag'] = ''
    df['OrganizationMention'] = ''
    df['Geotag'] = ''
    df['GeoMention'] = ''
    print(".....")
    for index, row in df.iterrows():
      if(row["hashtags"] != '[]'):
        hashtags = (row["hashtags"])
        text = re.findall("#([a-zA-Z0-9_]{1,50})", hashtags)
        text = str(text)[1:-1]
        doc = nlp(text)
        ents = [(e.text, e.label_) for e in doc.ents]
        org = []
        geo = []
        for i in ents:
          if(i[1] == "ORG"):
            org.append(i[0])
          if(i[1] == "GPE"):
            geo.append(i[0])
        #df['Geotag'][index]  = geo
        #df['OrganizationTag'][index]  = org
        #row["Geotag"] = geo
        df.at[index, 'Geotag'] = geo
        df.at[index, 'OrganizationTag'] = org
        #row["OrganizationTag"] = org
    print(".....")
    for index, row in df.iterrows():
      if(row["mentioned"] != '[]'):
        hashtags = (row["mentioned"])
        text = re.findall("@([a-zA-Z0-9_]{1,50})", hashtags)
        text = str(text)[1:-1]
        doc = nlp(text)
        ents = [(e.text, e.label_) for e in doc.ents]
        geo = []
        org = []
        for i in ents:
          if(i[1] == "ORG"):
            org.append(i[0])
          if(i[1] == "GPE"):
            geo.append(i[0])
        #df['GeoMention'][index]  = geo
        #df['OrganizationMention'][index]  = org
        #row["GeoMention"] = geo
        #row["OrganizationMention"] = org
        df.at[index, 'GeoMention'] = geo
        df.at[index, 'OrganizationMention'] = geo
    print(".....")
    df.to_csv(outputfilename)


def parse_args():
    parser = argparse.ArgumentParser(description="Read File")
    parser.add_argument("--inputfilename",type = str)
    parser.add_argument("--outputfilename",type = str)
    return parser.parse_args()

def main():
    inputs=parse_args()
    print(inputs.inputfilename)
    print(inputs.outputfilename)
    tag_analysis(inputs.inputfilename,inputs.outputfilename)
  

if __name__ == '__main__':
    main()
