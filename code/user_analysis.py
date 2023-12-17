#  <#Title#>

import pandas as csv


def user_analysis(filename):
    railroad_companies = ['AKRR',
     'Amtrak',
     'BNSFRailway',
     'CNRailway',
     'DSNGRR',
     'GoBrightline',
     'IAISRR',
     'MBTA',
     'North_Shore_RR',
     'TCWRailroad',
     'UnionPacific',
     'VaRailExpress',
     'hartfordline',
     'nscorp',
     'railnola',
     'smarttrain','MetroNorth']

    df = pd.read_csv(filename)
    railcompany_tweets = df[author.username].isin(railroad_companies)
    railcompany_tweets.to_csv("railcompany_tweets.csv")

    df1 = pd.read_csv("citinames.csv")
    city_tweets = pd.concat([df, df1], axis=1, join="inner")
    city_tweets = pd.merge(df, df1, on="author.name")
    city_tweets.to_csv("cities_tweets.csv")


    first_reponders = ['police','fire','emergency']
    first_res_tweets = df[df['author.username'].str.contains('|'.join(first_reponders))]
    first_res_tweets.to_csv("first_res_tweets_tweets.csv")


    public_safety_agency_users = ['olinational','CAOpLifeSaver','MinnesotaOL','MillerIngenuity','oplifesaver','CNRailway','OL_NC','Stayoffthetrax','USDOTFRA','oliofpa']
    public_safety_agency_tweets = df[df['author.username'].str.contains('|'.join(first_reponders))]
    public_safety_agency_tweets.to_csv("public_safety_agency_tweets.csv")


def parse_args():
    parser = argparse.ArgumentParser(description="Read File")
    parser.add_argument("--filename",type = str)
    return parser.parse_args()

def main():
    inputs=parse_args()
    print(inputs.filename)
    user_analysis(inputs.filename)
  

if __name__ == '__main__':
    main()
