from twython import Twython
import tokenizer
from collections import Counter


title= 'python'



ACCESS_TOKEN = '1JErcdF8U77N5YTdI5BzA5KXL'                                    
ACCESS_SECRET = 'ei6ajSLHsDfcdG95qBdpmhHWdRYaAUHQls8SQILOzEco56d0Za' 
CONSUMER_KEY = '772785857807822848-JJftUpOKZcnvSVvVLNen3ndEUmxMK8J'
CONSUMER_SECRET = 'heJsxwsdLD4Fh7ECbWGkjooEMJOe7hJNpJCueTuUdY63a'           # I am trusting you with my access token and consumer secret :)



api = Twython(app_key=ACCESS_TOKEN, 
            app_secret=ACCESS_SECRET, 
            oauth_token=CONSUMER_KEY, 
            oauth_token_secret=CONSUMER_SECRET)


tweets =   []
attempts= 10
tweets_required=  1000

for i in range(0,attempts):

    if(tweets_required < len(tweets)):
        break 

    if(i == 0):
        results    = api.search(q=title,count='100',lang='en')    # Initial search
    else:
        results    = api.search(q=title,include_entities='true',max_id=next_max_id,lang='en',count='100')   # Subsequent searches with max_id param obtained from earlier searches

    for result in results['statuses']:
        tweet = result['text']
        tweets.append(tweet)                                      # Storing tweets


    try:
        next_results    = results['search_metadata']['next_results']         # obtaining max_id
        next_max_id        = next_results.split('max_id=')[1].split('&')[0]
 
    except:
        break



token_list=[]                                                     # tokenization
for tweet in tweets:
	tokens=tokenizer.tokenize(tweet)
	token_list.append(tokens)
	
bag_of_words=[]                                                   # flattening of list of lists
for sublist in token_list:
    for item in sublist:
        bag_of_words.append(item)



hashtags=[]                                                       # creating a list of hashtags
for word in bag_of_words:
	if (word[0]=='#'):
		hashtags.append(word.lower())

same_name=title.strip()                                           # removing white space and converting to lowercase
same_name=same_name.replace(' ','')
same_name=same_name.lower()

try:
    hashtags= [x for x in hashtags if x != (('#'+same_name))]      # removing hashatgs containing only the title
except ValueError:
    pass

count = Counter()                                                  
count.update(hashtags)

print(count.most_common(10))
