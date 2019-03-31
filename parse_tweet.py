#parse tweet
import re

#tweet = "#ECE4564T19 p:Squires+Wishes\"I wish I had gotten their number."
#tweet = "c:Library+Noise #ECE4564T19"
tweet = "p:Goodwin+Classrooms #ECE4564T19 \"NetApps is in a crummy room.\""
hashtag = "#ECE4564T19"
print(tweet)
s = re.sub("\s*"+hashtag+"\s*","",tweet)
print(s)
command = s.split(':')[0]
command = command.strip() #strip removes whitespace from beginning or end of a character
print(command)
therest = s.split(':')[1]
Place = therest.split('+')[0]
Place = Place.strip()
therest = therest.split('+')[1]
print(Place)
if (command == 'p'):
    Subject = therest.split('\"')[0]
    Subject = Subject.strip()
    print(Subject)
    Message = therest.split('\"')[1]
    Message.strip()
    print(Message)
elif (command == 'c'):
    Subject = therest.strip()
    Message = None
    print(Subject)

