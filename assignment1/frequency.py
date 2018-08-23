import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    frequency = {}

    for line in tweet_file:
        tweet = json.loads(line)
        keys = tweet.keys()

        if 'text' in keys:
            s = tweet['text']
            s = s.split()

            # each word in one tweet
            for w in s:
                if w not in frequency:
                    frequency[w] = 1
                else:
                    frequency[w] += 1

    for key in frequency.keys():
        print '{} {}'.format(key.encode('utf-8'), frequency[key])


if __name__ == '__main__':
    main()