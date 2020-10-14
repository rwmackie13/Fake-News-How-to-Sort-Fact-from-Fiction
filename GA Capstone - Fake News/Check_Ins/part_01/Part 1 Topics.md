# Part 1: Roundtable Lightning Talks

## Overview

In this section, you will be presenting three potential topics to your coursemates (and fellow well-wishers!)  

## Topics

**Predicting Market Values of Privately Held Companies**

Problem Statement:

- Many times when a privately held company comes into the public domain it is hard for investors to know the true worth of the company.  The majority have been overvalued and this can lead to potential problems when ivesting.

- Our goal would be to analyze the financial performance of the top privately held companies, and then predict their market values (or just classifying where they would be large, mid, small-cap) based on past performance.  In turn we are hoping to provide investors with an upper hand when investing in new to market companies.

- For this project, I would need to scrape filing data from the SEC website and read to a csv file.  Data is available from 1994 through the present, and each public filing directory contains 3 file forms: HTML, XML, and JSON so we can easily pull this data from our source.

- working with the edgar system that the SEC uses could be a challenge

- should be able to complete in the timeframe

**Tracking COVID-19/News/Political Disinformation through Social Media**

- As we are all aware, disinformation tactics are rampant in our news/media outlets.  How are we as uninformed participants to decide what is and isn't true in the moment.  For us to make this distinction, we would need to spend time (which many of us don't have) and do our own research in order to come up pwith our own conclusion. 

- Our goal in this project would be to analyze social media posts, specifically Twitter, and determine whether or not the post is true.  This is a major point of emphasis right now among many social media companies as it allows users the ability to see if a post is true or false, or even potentially true/false.  

- For this project, I would need to scrape posts from Twitter using their free API (or if I am going the covid route, there is already a covid-19 stream developed by twitter for developers - the problem with this is it is giving upwards of ten million tweets per day).  Try using PassiveAggressiveClassifier on this project - You cannot store so much data in your memory. A Passive Aggressive algorithm learns from these examples and discards them right away after use, without storing them in the memory.

- never used PA before

- this may take a lot of time, not sure until i were to try

**Predicting Stock Prices**

- Trying to predict stocks is an enticing proposition for many - who doesn't want to know that the stock they are about to buy is a surefire winner.  When robinhood came into the market and began offering free brokerage services that had always been elusive to your everyday american, we began to see many people start investing their mpeny - no matter how much ($1 - $10,000). With this also comes the risk of normal people not understanding why stocks move the way they do. 

- Our goal for this project would be to analyze stock performance over a period of time, and predict if they are going to be a good buy or not.  Hopefully, this allows our average investor easily find stocks that are predicted to be good buys moving forward.

- For this project, I would need to scrape stock data from the Yahoo Finance which is in HTML.

- biggest challenge is that stocks are not very predictive - which is why this is a fun challenge!

- i think it's reasonable to have a model, but not sure if it will be close to good




