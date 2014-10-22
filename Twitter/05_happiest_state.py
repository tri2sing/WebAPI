import sys
import json

'''
Your script should print the two letter state abbreviation of the state with the highest average tweet sentiment to stdout.
'''

shorttofull = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

fulltoshort = {
    'Washington': 'WA',
    'Wisconsin': 'WI',
    'West Virginia': 'WV',
    'Florida': 'FL',
    'Wyoming': 'WY',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'National': 'NA',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Nebraska': 'NE',
    'New York': 'NY',
    'Rhode Island': 'RI',
    'Nevada': 'NV',
    'Guam': 'GU',
    'Colorado': 'CO',
    'California': 'CA',
    'Georgia': 'GA',
    'Connecticut': 'CT',
    'Oklahoma': 'OK',
    'Ohio': 'OH',
    'Kansas': 'KS',
    'South Carolina': 'SC',
    'Kentucky': 'KY',
    'Oregon': 'OR',
    'South Dakota': 'SD',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Hawaii': 'HI',
    'Puerto Rico': 'PR',
    'Texas': 'TX',
    'Louisiana': 'LA',
    'Tennessee': 'TN',
    'Pennsylvania': 'PA',
    'Virginia': 'VA',
    'Virgin Islands': 'VI',
    'Alaska': 'AK',
    'Alabama': 'AL',
    'American Samoa': 'AS',
    'Arkansas': 'AR',
    'Vermont': 'VT',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Arizona': 'AZ',
    'Idaho': 'ID',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Utah': 'UT',
    'Missouri': 'MO',
    'Minnesota': 'MN',
    'Michigan': 'MI',
    'Montana': 'MT',
    'Northern Mariana Islands': 'MP',
    'Mississippi': 'MS'
}

cumulative = {}  
counts = {}
scores = {}

def scores_read(sentiment_file):
    for line in sentiment_file:
        term, score = line.split('\t')
        scores[term] = int(score)


def hw(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        if 'place' in tweet and tweet['place'] and tweet['place']['country_code'] == 'US':
            city, state = tweet['place']['full_name'].split(', ')
            if state == 'USA' and city in fulltoshort:  # Sometimes the data does not adhere to the pattern
                state = fulltoshort[city]
            if state != 'USA':
                terms = list(tweet['text'].split())
                value = sum([scores[x.encode('utf-8')] if x.encode('utf-8') in scores else 0 for x in terms])
                if state in cumulative:
                    cumulative[state] += value
                    counts[state] += 1
                else:
                    cumulative[state] = value
                    counts[state] = 1
                
    
def print_output():
    maximum = -9
    state = ''
    for x in cumulative:
        current = float(cumulative[x])/counts[x]
        if current > maximum:
            maximum = current
            state = x
    print state
            

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores_read(sentiment_file)
    hw(tweet_file)
    print_output()

if __name__ == '__main__':
    main()


