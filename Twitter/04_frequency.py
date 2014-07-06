import sys
import json

'''
Compute the term frequency histogram of the livestream data.
'''

counts = {}  # Counts of individual terms in all tweets
total_terms = 0

def hw(tweet_file):
    global total_terms
    for line in tweet_file:
        tweet = json.loads(line)
        utfterms = list(tweet['text'].split())
        terms = [x.encode('utf-8').lower() for x in utfterms]
        for x in terms:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
            total_terms += 1
    
def print_output():
    for x in counts:
        print x, str(counts[x]/float(total_terms))
            

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    print_output()

if __name__ == '__main__':
    main()
