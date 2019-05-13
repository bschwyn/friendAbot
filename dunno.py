#split and prepare tweets.json
#tweets.json has format [{},{}, {}, {},...]
#read array and print tweet to file line by line.
#load portion of array (figure out how to do this)
#for array split portion
#get array chunk,

#turn json to list of strings

#download Karpathy charRNN

import json


def json_to_tweets():
    json_array = json.load(open('tweets.json'))
    tweets = list(map((lambda x: x["text"]), json_array))
    f = open('tweetstxt.txt', 'w')
    for tweet in tweets:
        f.write(tweet)
        f.write("\n\n")
    f.close()
json_to_tweets()




#for item in json_array:



#for item in thelist:
#    thefile.write("%s\n" % item)


#def tweet_dict_to_string(dictionary):
#    d = dictionary


def test_json_parse():
    json_array = [{"fullname": "Aella", "timestamp": "2012-09-01T20:07:31", "retweets": "0", "id": "241990690286993408", "user": "Aella_Girl", "replies": "1", "likes": "0", "text": "First tweet and I am hungover! I hate you all."}, {"fullname": "Aella", "timestamp": "2012-09-04T11:09:12", "retweets": "0", "id": "242942382608371712", "user": "Aella_Girl", "replies": "0", "likes": "0", "text": "Time to pass out and have really weird dreams involving incredibly illogical advances in technology. That's been a dream fad of mine lately."}]
    bla = list(map((lambda x: x["text"]),json_array))
    text = ["First tweet and I am hungover! I hate you all.","Time to pass out and have really weird dreams involving incredibly illogical advances in technology. That's been a dream fad of mine lately."]
    print(bla == text)

test_json_parse()