import sys
import json

'''
    In this part you will be creating a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
    Here's how you might think about the problem. 
    We know we can use the sentiment-carrying words in AFINN-111.txt to deduce the overall sentiment of a tweet. 
    Once you deduce the sentiment of a tweet, you can work backwards to deduce the sentiment of the non-sentiment carrying words that do not appear in AFINN-111.txt. 
    For example, if the word soccer always appears in proximity with positive words like great and fun, then we can deduce that the term soccer itself carries a positive sentiment.
'''

scores_known = {}  # Known sentiment scores
values_unknown = {}  # Some representative value for terms with unknown sentiment scores
counts_unknown = {}  # Count of the number of tweets in which a term with unknown score occurs

def scores_read(sentiment_file):
    for line in sentiment_file:
        term, score = line.split('\t')
        scores_known[term] = int(score)


def hw(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        uterms = list(tweet['text'].split())
        terms = [x.encode('utf-8').lower() for x in uterms]
        known_terms = [x for x in terms if x in scores_known]
        unknown_terms = [x for x in terms if x not in scores_known]
        value = sum([scores_known[x] for x in known_terms])
        # print tweet['text'].encode('utf-8'), ": ", str(value)
        for x in unknown_terms:
            if x in values_unknown:
                values_unknown[x] = values_unknown[x] + value
                counts_unknown[x] = counts_unknown[x] + 1
            else:
                values_unknown[x] = value
                counts_unknown[x] = 1
    
def print_output():
    for x in values_unknown:
        # print x, str(values_unknown[x]),  str(counts_unknown[x])
        print x, str(float(values_unknown[x]) / counts_unknown[x])
            

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores_read(sentiment_file)
    hw(tweet_file)
    print_output()

if __name__ == '__main__':
    main()
