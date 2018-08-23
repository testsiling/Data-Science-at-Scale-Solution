import json
import sys

def main():

    #tweet_file = open('./output.txt')
    tweet_file = open(sys.argv[1])

    hashtags = {}

    for line in tweet_file:
        tweet = json.loads(line)
        keys = tweet.keys()

        if 'entities' in keys:
            entities = tweet['entities']
            tags = entities['hashtags']

            if tags is []:
                continue

            for tag in tags:
                t = tag['text']
                if t not in hashtags:
                    hashtags[t] = 1
                else:
                    hashtags[t] += 1

    top10 = sorted(hashtags, key = hashtags.get)[::-1]
    top10 = top10[0:10]

    for t in top10:
        print '{} {}'.format(t.encode('utf-8'), hashtags[t])
        #print(t, hashtags[t])


if __name__ == '__main__':
    main()
