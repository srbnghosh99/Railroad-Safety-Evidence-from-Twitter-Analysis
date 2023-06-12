twarc2 search --start-time "2022-06-01" --end-time "2022-0-15" --archive "(\"#NoTrespassing\" OR \"#railsafety\" OR \"#StopTrespassing\" OR \"#TracksAreForTrains\" OR \"#RailroadSafety\" OR \"#RailTransport\" OR \"#Railroaders\" OR \"railroad trespassing\" OR \"#StayOffTheTracks\" OR \"#TracksAreForTrains\" OR \"railroad trespasser\" OR \"rail track trespassing\" OR \"rail track trespasser\")" tweets_trespassing2.json
twarc2 search --start-time "2022-06-25" --end-time "2022-07-08" --archive "(\"Missouri train accident\" OR \"Amtrak train\")" tweets_trespassing2.json
twarc2 search --archive "from:USDOTFRA" USDOTFRA.json
twarc2 search --start-time 2010-01-01 "#RailSafety" tweets.jsonl
twarc search 'railroad trespassing' > tweets.json
twarc2 search --flatten --archive "#ENDSARS" TwarcResultss2.jsonl
twarc2 search --start-time 2017-01-01 --end-time 2022-05-17 '"railroad safety"' tweets.jsonl

## count number of tweets in filename
wc -l filename.json
## convert json file to csv format
twarc2 csv tweets_trespassing2.json tweets_trespassing2.csv
