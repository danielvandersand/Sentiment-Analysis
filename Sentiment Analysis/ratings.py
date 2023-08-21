from textblob import TextBlob
from pygooglenews import GoogleNews


'''''''''''''''
For non-mac: 
pip install pygooglenews 

For mac users
python -m pip install "beautifulsoup4==4.9.1"
python -m pip install "dateparser==0.7.6"
python -m pip install "requests==2.24.0"
python -m pip install "feedparser==6.0.8"
python -m pip install --no-deps pygooglenews

Thank you to this awesome person that created pygooglenews API
https://github.com/kotartemiy/pygooglenews
'''''''''''''''


def get_ratings(search):
    gn = GoogleNews()
    search = gn.search(search)
    newsitem = search['entries']
    subjectivity_rating = 0
    polarity_rating = 0
    number_positive = 0
    for item in newsitem:
        blob = TextBlob(str(item.title))
        subjectivity_rating += blob.sentiment.subjectivity
        polarity_rating += blob.sentiment.polarity
        if blob.sentiment.polarity > 0.1:
            number_positive += 1
    return [int(subjectivity_rating), int(polarity_rating), int(number_positive)]