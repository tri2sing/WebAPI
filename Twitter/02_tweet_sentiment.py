import sys
import json

''' 
    The file AFINN-111.txt contains a list of pre-computed sentiment scores. 
    Each line in the file contains a word or phrase followed by a sentiment score. 
    Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0.
'''

def scores_read(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores

def hw(tweet_file, scores):
    for line in tweet_file:
        tweet = json.loads(line)
        terms = list(tweet['text'].split())
        value = sum([scores[x.encode('utf-8')] if x.encode('utf-8') in scores else 0 for x in terms])
        print value

def main():
    sent_file = open(sys.argv[1])  # Using AFINN-111.txt as the sentiment file
    tweet_file = open(sys.argv[2]) # File downloaded using 01_download_stream.py
    scores = scores_read(sent_file)
    hw(tweet_file, scores)

if __name__ == '__main__':
    main()
