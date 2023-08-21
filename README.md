# Sentiment-Analysis
Welcome to the Google News Sentiment Analyzer project! This web application leverages the TextBlob library and the PyGoogleNews API to analyze the sentiment of the top 100 articles on a given topic. Users can input their desired topic, and the application will provide the percentage of positive and subjective articles among the top news stories.

## Introduction
The Google News Sentiment Analyzer is a tool designed to provide insights into the sentiment and subjectivity of news articles on a specified topic. By using the TextBlob library, the application performs sentiment analysis to determine whether articles are positive or negative, as well as subjectivity analysis to determine the extent to which articles express opinions rather than objective information.

## Features
- Topic Input: Users can enter any topic of interest to retrieve news articles.
- Sentiment Analysis: The application performs sentiment analysis on the articles to determine their positivity or negativity.
- Subjectivity Analysis: The application also calculates the subjectivity of the articles to assess the extent of opinion expressed.
- Percentage Calculation: Users receive the percentage of positive and subjective articles out of the top 100 news stories.

## Installation
- Make sure you have the latest version of python installed.
- Flask:
pip install Flask
- TextBlob:
pip install textblob
- Thank you to the creators of pygooglenews! [Make sure to give them a star!](https://github.com/kotartemiy/pygooglenews)
pygooglenews: <br>
python -m pip install "beautifulsoup4==4.9.1" <br>
python -m pip install "dateparser==0.7.6" <br>
python -m pip install "requests==2.24.0" <br>
python -m pip install "feedparser==6.0.8" <br>
python -m pip install --no-deps pygooglenews

## Usage
- Navigate to directory in terminal and type in: run app.py
- Open your web browser and navigate to http://localhost:5000 to access the application.
- Enter a topic of interest in the input field and submit the form.
- The application will display the percentage of positive and subjective articles among the top news stories on the specified topic.
