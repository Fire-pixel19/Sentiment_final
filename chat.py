import asyncio
from twikit import Client, TooManyRequests
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint
import pandas as pd
from textblob import TextBlob

def Scrape_Tweets(QUERY):
    if QUERY==None:
            raise ValueError('Please provide a query to search for tweets')
    else:
            QUERY=QUERY
            

    # Load configuration
    config = ConfigParser()
    config.read('C://Users//Yash//Documents//Code//Python//Sentiment_Analysis//config.ini')



    #MINIMUM_TWEETS = int(config['DEFAULT']['MINIMUM_TWEETS'])
    MINIMUM_TWEETS = 30
    # Initialize client
    client = Client(language='en-US')

    # Sentiment analysis function
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    # Function to fetch and process tweets asynchronously
    async def get_tweets(tweets):
        if tweets is None:
            print(f'{datetime.now()} - Getting tweets...')
            tweets = await client.search_tweet(QUERY, product='Top')
        else:
            wait_time = randint(5, 10)
            print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds...')
            await asyncio.sleep(wait_time)
            tweets = tweets.next()

        tweet_data = []
        for tweet in tweets:
            sentiment = analyze_sentiment(tweet.text)
            tweet_data.append({'tweet': tweet.text, 'sentiment': sentiment})
        
        return pd.DataFrame(tweet_data)

    # Main function
    async def main():
        tweet_count = 0
        tweets = None

        # Create CSV
        with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['tweet', 'sentiment'])
            writer.writeheader()

        # Load cookies
        client.load_cookies('cookies.json')

        while tweet_count < MINIMUM_TWEETS:
            try:
                tweets_df = await get_tweets(tweets)
                if tweets_df.empty:
                    print(f'{datetime.now()} - No more tweets found')
                    break

                # Append to CSV
                tweets_df.to_csv('tweets.csv', mode='a', index=False, header=False)

                tweet_count += len(tweets_df)
            except TooManyRequests as e:
                rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
                print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
                wait_time = rate_limit_reset - datetime.now()
                await asyncio.sleep(wait_time.total_seconds())
            except Exception as ex:
                print(f"Error: {ex}")
                break

        print(f'{datetime.now()} - Done! {tweet_count} tweets fetched.')
    asyncio.run(main())


        
