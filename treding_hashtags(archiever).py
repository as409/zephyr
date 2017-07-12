import codecs
import tokenizer
from collections import Counter

title='narendra modi'                                            # Change path and title accordingly
path='/home/akhil/Desktop/as409@snu.edu.in_TRENDING_HASHTAGS_TASK_11.07.17/feltso_archiever - -Narendra Modi- lang-en.tsv'

file=codecs.open(path,'r',encoding= 'utf-8')
lines=file.readlines()
tweets=[]
for line in lines:
	x=line.split('\t')
	tweets.append(x[3])


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
