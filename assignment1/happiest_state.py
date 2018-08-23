import sys
import json
import re


def main():
    #sent_file = open('./AFINN-111.txt')
    #tweet_file = open('./output.txt')
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    states = 'AK|Alaska|AL|Alabama|AR|Arkansas|AS|American Samoa|AZ|Arizona|CA|California|CO|Colorado|CT|Connecticut|DC|District of Columbia|DE|Delaware|FL|Florida|GA|Georgia|GU|Guam|HI|Hawaii|IA|Iowa|ID|Idaho|IL|Illinois|IN|Indiana|KS|Kansas|KY|Kentucky|LA|Louisiana|MA|Massachusetts|MD|Maryland|ME|Maine|MI|Michigan|MN|Minnesota|MO|Missouri|MP|Northern Mariana Islands|MS|Mississippi|MT|Montana|NA|National|NC|North Carolina|ND|North Dakota|NE|Nebraska|NH|New Hampshire|NJ|New Jersey|NM|New Mexico|NV|Nevada|NY|New York|OH|Ohio|OK|Oklahoma|OR|Oregon|PA|Pennsylvania|PR|Puerto Rico|RI|Rhode Island|SC|South Carolina|SD|South Dakota|TN|Tennessee|TX|Texas|UT|Utah|VA|Virginia|VI|Virgin Islands|VT|Vermont|WA|Washington|WI|Wisconsin|WV|West Virginia|WY|Wyoming'
    p = re.compile(states)  # pattern match states

    states_scores = {}  # en + has location

    states_abb = getStatesDic()

    for i, line in enumerate(tweet_file):
        tweet = json.loads(line)
        keys = tweet.keys()

        if 'user' in keys:
            user = tweet['user']
            location = user['location']
            if location is not None:

                if p.search(location):
                    state = p.search(location).group()

                    score = getScore(tweet['text'], scores)

                    if state not in states_abb:
                        state = getStateAbb(states_abb, state)

                    if state is None:
                        continue

                    # if haven't record
                    if state not in states_scores:
                        states_scores[state] = score
                    else:
                        states_scores[state] += score

                    # print()

    print(whichHappiest(states_scores))


def getStateAbb(states, text):
    #get the state abbreviation
    for abb, full in states.items():
        if full is text:
            return abb

def whichHappiest(allScore):
    max = 0
    happy = ''
    for states, score in allScore.items():
        if score > max:
            max = score
            happy = states
    return happy

def getStatesDic():
    states = {
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
    return states


def getScore(text, scores):
    #return the score of a tweet
    # build up an english dictionary

    s = text.lower()
    s = s.split()
    res = 0
    for w in s:
        if w in scores:
            res += scores[w]

    return res

if __name__ == '__main__':
    main()
