import os
import pandas as pd
import numpy as np
import re
import csv
import string,time
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer

chat_word = {
    'AFAIK': 'As Far As I Know',
    'AFK': 'Away From Keyboard',
    'ASAP': 'As Soon As Possible',
    'ATK': 'At The Keyboard',
    'ATM': 'At The Moment',
    'A3': 'Anytime, Anywhere, Anyplace',
    'BAK': 'Back At Keyboard',
    'BBL': 'Be Back Later',
    'BBS': 'Be Back Soon',
    'BFN': 'Bye For Now',
    'B4N': 'Bye For Now',
    'BRB': 'Be Right Back',
    'BRT': 'Be Right There',
    'BTW': 'By The Way',
    'B4': 'Before',
    'CU': 'See You',
    'CUL8R': 'See You Later',
    'CYA': 'See You',
    'FAQ': 'Frequently Asked Questions',
    'FC': 'Fingers Crossed',
    'FWIW': "For What It's Worth",
    'FYI': 'For Your Information',
    'GAL': 'Get A Life',
    'GG': 'Good Game',
    'GN': 'Good Night',
    'GMTA': 'Great Minds Think Alike',
    'GR8': 'Great!',
    'G9': 'Genius',
    'IC': 'I See',
    'ICQ': 'I Seek you (also a chat program)',
    'ILU': 'ILU: I Love You',
    'IMHO': 'In My Honest/Humble Opinion',
    'IMO': 'In My Opinion',
    'IOW': 'In Other Words',
    'IRL': 'In Real Life',
    'IDK':'I Dont Konw',
    'KISS': 'Keep It Simple, Stupid',
    'LDR': 'Long Distance Relationship',
    'LMAO': 'Laugh My A.. Off',
    'LOL': 'Laughing Out Loud',
    'LTNS': 'Long Time No See',
    'L8R': 'Later',
    'MTE': 'My Thoughts Exactly',
    'M8': 'Mate',
    'NRN': 'No Reply Necessary',
    'OIC': 'Oh I See',
    'PITA': 'Pain In The A..',
    'PRT': 'Party',
    'PRW': 'Parents Are Watching',
    'QPSA?': 'Que Pasa?',
    'ROFL': 'Rolling On The Floor Laughing',
    'ROFLOL': 'Rolling On The Floor Laughing Out Loud',
    'ROTFLMAO': 'Rolling On The Floor Laughing My A.. Off',
    'SK8': 'Skate',
    'STATS': 'Your sex and age',
    'ASL': 'Age, Sex, Location',
    'THX': 'Thank You',
    'TTFN': 'Ta-Ta For Now!',
    'TTYL': 'Talk To You Later',
    'U': 'You',
    'U2': 'You Too',
    'U4E': 'Yours For Ever',
    'WB': 'Welcome Back',
    'WTF': 'What The F...',
    'WTG': 'Way To Go!',
    'WUF': 'Where Are You From?',
    'W8': 'Wait...',
    '7K': 'Sick:-D Laugher',
    'TFW': 'That feeling when',
    'MFW': 'My face when',
    'MRW': 'My reaction when',
    'IFYP': 'I feel your pain',
    'TNTL': 'Trying not to laugh',
    'JK': 'Just kidding',
    'IDC': "I don't care",
    'ILY': 'I love you',
    'IMU': 'I miss you',
    'ADIH': 'Another day in hell',
    'ZZZ': 'Sleeping, bored, tired',
    'WYWH': 'Wish you were here',
    'TIME': 'Tears in my eyes',
    'BAE': 'Before anyone else',
    'FIMH': 'Forever in my heart',
    'BSAAW': 'Big smile and a wink',
    'BWL': 'Bursting with laughter',
    'BFF': 'Best friends forever',
    'CSL': "Can't stop laughing"
}
def filter_text():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(BASE_DIR, 'tweets.csv')
    
    df = pd.read_csv("csv_path")
    #train_data = pd.read_csv("C:\\Users\\Yash\\Desktop\\Major Project\\twitter_validation.csv")
    with open('Filtered.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['tweet','Sentiment'])

    df.isna().sum()

    df['tweet']=df['tweet'].str.lower()

    def remove_html_tags(text):
        pattern = re.compile('<.*?>')
        return pattern.sub('',text)

    def remove_url(text):
        pattern= re.compile(r"https?://\S+|www\.\S+")
        return pattern.sub(r'',text)
    exclude= string.punctuation

    def remove_punc(text):
        for char in exclude:
            text = text.replace(char,'')
        return text

    def short_conv(text):
        new_text = []
        for w in text.split():
            if w.upper() in chat_word:
                new_text.append(chat_word[w.upper()])
            else:
                new_text.append(w)
        return " ".join(new_text)

    def spell_correct(text):
        textblb=TextBlob(text)
        return textblb.correct().string

    def remove_emoji(text):
        emoji_pattern=re.compile("["
                                u"\U0001F600-\U0001F64F" #emoticons
                                u"\U0001F300-\U0001F5FF" #symbols, pictograph
                                u"\U0001F680-\U0001F6FF" #transport and map symbol
                                u"\U0001F1E0-\U0001F1FF" # flags(IOS)
                                u"\U00002702-\U000027B0"
                                u"\U00002FC2-\U0001F251"
                                "]+",flags=re.UNICODE)
        return emoji_pattern.sub(r'',text)

    df['tweet']=df['tweet'].apply(remove_html_tags)

    df['tweet']=df['tweet'].apply(remove_url)

    df['tweet']=df['tweet'].apply(remove_punc)

    df['tweet']=df['tweet'].apply(short_conv)

    df['tweet']=df['tweet'].apply(remove_emoji)

    for tweet in df['tweet']:
            tweet_data = [tweet]
            with open('Filtered.csv', 'a', newline='',encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(tweet_data)
    
            #pd.DataFrame(tweet_data, columns=['Tweet'])
    return True

filter_text()
