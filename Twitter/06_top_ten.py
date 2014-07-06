import sys
import json

'''
Compute the ten most frequently occurring hashtags from the data you gathered in Problem 1.
'''

counts = {}  # Counts of individual terms in all tweets

def hw(tweet_file):
    global total_terms
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet and tweet['entities']['hashtags']:
            tags = [x['text'].encode('utf-8') for x in tweet['entities']['hashtags']]
            for x in tags:
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1
    
def print_output():
    i = 0
    for x in sorted(counts, key=counts.get, reverse=True):
        if i == 10: break
        print x, counts[x]
        i += 1
            

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    print_output()

if __name__ == '__main__':
    main()
