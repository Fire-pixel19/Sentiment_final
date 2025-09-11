import chat as chat
import Filter as filter
import Gemini as GenShit
from flask import Flask, request, jsonify,render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Frontend webpage

@app.route('/topic')
def topic_based():
    return render_template('topic_based.html')  # First webpage
    

@app.route('/tweet')
def tweet_based():
    return render_template('tweet_based.html')  # Second webpage


@app.route('/analyze', methods=['POST'])
def Tweet_Based_Sentiment():     ##this function exclusively Analyzes the sentiments of the tweet given by the user

    topic = request.json.get('topic')  # Get the topic from the frontend
    tweet = request.json.get('tweet')  # Get the tweet from the frontend
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    elif not tweet:
        return jsonify({'error': 'Tweet is required'}), 400
    try:
        if not(isinstance(topic,str )and isinstance(tweet,str)): 
            raise ValueError('Please provide a query to search for tweets')
        else:
            result = GenShit.Topic_Based_Get_Response(topic,tweet)


        return jsonify({'success': True, 'data': result})
        #return render_template('TopicBased.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze1', methods=['POST'])
def Topic_Based_Sentiment():     ##this function exclusively Analyzes the sentiments of the tweet given by the user

    topic = request.json.get('topic')  # Get the topic from the frontend
    if not topic:
        return jsonify({'error': 'Topic is required'}), 400
    try:
        if not(isinstance(topic,str )): 
            raise ValueError('Please provide a query to search for tweets')
        else:
            chat.Scrape_Tweets(topic)
            filter.filter_text()
            result = GenShit.File_Based_Get_Response()


        return jsonify({'success': True, 'data': result})
        #return render_template('TopicBased.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

'''def Topic_Based_Sentiment(): ##this  function exclusively Analyzes the sentiments of the topic given by the user 
    QUERY=input("Enter a Topic: ")
    chat.Scrape_Tweets(QUERY)
    filter.filter_text()
    print(GenShit.File_Based_Get_Response())'''

if __name__ == '__main__':
    app.run()

'''def Topic_Based_Sentiment(QUERY): ##this  function exclusively Analyzes the sentiments of the topic given by the user 
    chat.Scrape_Tweets(QUERY)
    filter.filter_text()
    print(GenShit.File_Based_Get_Response())'''

    

