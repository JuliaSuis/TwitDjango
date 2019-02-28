Python 2.7 (Possible to run in Python3, just add some changes. Notices can be found in the code files.)

▫ Database driven Django application that collects data from Twitter analyzes it and provides a graphical representation of the results
▫ Technologies: Sentiment analysis, Naive Bayes classifier, Data mining
▫ Tools: Python, Pandas, Django, jQuery, Ajax


Virttualenv (myvenv)

Packages:

    Tweepy
    UrlLib
    TextBlob
    AFINN
    BeautifulSoup
    NumPy
    URLLib
    Pandas
    NLTK
    MatPlotLib
    WorldCloud

    Django packages

Steps:

1) Create a virtual environment and run it
>> python3 -m venv myvenv
>> source myvenv/bin/activate

2) Install Django
>> pip install django (used vers. 1.10)

3) The programm has to be run from terminal from the project directory with manage.py
>> python manage.py runserver

4) Open the browser http://127.0.0.1:8000/sentiment/

*) Don't forget your ckey, csecret, atoken, asecret to auth.py file
*) Install all requirement packages in myvenv





