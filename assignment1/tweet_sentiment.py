import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        tweet = json.loads(line)
        keys =  tweet.keys()
        if 'text' in keys:
            s = tweet['text'].lower()
            s = s.split()
            score = 0
            for w in s:
                if w in scores:
                    score += scores[w]
            print score
        else:
            print 0




if __name__ == '__main__':
    main()
