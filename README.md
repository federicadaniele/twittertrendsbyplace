# twittertrendsbyplace
Gets twitter trends for a set of Where on Earth ID and plots a few summarizing statistics on map

The order of execution for the files is the following:

1. trendingtopicsplace.py:
I have assembled a list of Yahoo WOEID (see http://woeid.rosselliot.co.nz/). Each woeid in woeid,csv goes as an argument of the tweepy method api.trends_place (for info on tweepy module see http://docs.tweepy.org/en/v3.5.0/api.html).

2. getstats.do:
the list of trends per place is saved into a csv file and imported into Stata (yes, sorry, so far still faster on Stata for certain things, but currently updating this project to have everything on Python), and used to merge information on coordinates (woeidpop.xlsx) and compute some statistics, e.g. the index of disagreement consisting of the average squared deviation of a given trend ranking per place from the average ranking for the same trend across places. Notice that this is not a weighted average: so we do not expect places like LA or NYC to “disagree” less because they are larger…

3. plottwittertrends.py:
the output file — finalplot22112017.csv — is then used back into python to produce a map. the required module is basemap and for those that use a Mac like I do here is a link on how to install it
https://stackoverflow.com/questions/42299352/installing-basemap-on-mac-python

Notice a couple of things: 
- it seems like the tweet volume that you get per each trend when you use Twitter api is the aggregate volume, not the location specific one… so the rank of each topic (on a scale from 1 to 50) is used as proxy for location specific social preferences.
- when you download trending topics, not only you get hashtags, but also pages, people or mentions (e.g., “trump” is a recurring result). I focused throughout on hashtags cause they seem to get closer to Twitter designation for trending topic https://blog.bufferapp.com/five-twitter-secrets-about-censored-trending-topics#1 although this might just be my taste. 

More stuff is coming on how to scrape the Where on Earth ID given a location name.
