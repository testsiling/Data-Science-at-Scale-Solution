import json
import sys

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    for line in tweet_file:
        tweet = json.loads(line)
        keys = tweet.keys()

        if 'text' in keys:
            s = tweet['text'].lower()
            s = s.split()
            score = 0
            for w in s:
                if w in scores:
                    print '{} {}'.format(w, scores[w])


if __name__ == '__main__':
    main()
