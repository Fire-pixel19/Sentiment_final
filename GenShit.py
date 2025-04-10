import os
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv,find_dotenv

def File_Based_Get_Response():
    _ = load_dotenv(find_dotenv())
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    tweet_path = os.path.join(BASE_DIR, 'Filtered.csv')
    
    df = pd.read_csv(tweet_path)

      # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
    )

    chat_session = model.start_chat()
    #response = chat_session.send_message("define a goal in football ")
    response = chat_session.send_message(f"Given Below are a bunch of strings you have to tell me the sentiment of this string this{df['tweet']}and tell me the reason of why you think about the same ")
    #content = response.result[0]['text']
    content = response._result.candidates[0].content.parts[0].text

    return content  ##returns the response from the model with description in the form of string

def Topic_Based_Get_Response(topic:str, tweet:str):
    _ = load_dotenv(find_dotenv())
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    
    # Create the model
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
    )

    chat_session = model.start_chat()
    #response = chat_session.send_message("define a goal in football ")
    response = chat_session.send_message(f"Given Below is a topic and a you have to tell me the sentiment of this Topic {topic,tweet}and Structure the response")
    #content = response.result[0]['text']
    content = response._result.candidates[0].content.parts[0].text
    #prompt = f"Analyze the sentiment surrounding '{topic,tweet}' and structure the response."
    #content = chat_session.send_message(prompt)
    #raw_output = content._result.candidates[0].content.parts[0].text
    # Process the API response (assuming it returns plain text)
    #raw_output = response.text

    # Structure the output dynamically
    '''sentiment_data = {
        "title": f"Sentiment Analysis of '{topic}'",
        "summary": "",
        "categories": {},
        "conclusion": ""
    }'''

    # Splitting Gemini response into sections (assuming structured text format)
    '''sections = raw_output.split("\n\n")
    
    for section in sections:
        if "Negative Sentiment" in section:
            sentiment_data["categories"]["Negative Sentiment"] = section.split("\n")[1:]
        elif "Positive Sentiment" in section:
            sentiment_data["categories"]["Positive Sentiment"] = section.split("\n")[1:]
        elif "Neutral Sentiment" in section:
            sentiment_data["categories"]["Neutral Sentiment"] = section.split("\n")[1:]
        elif "Summary" in section:
            sentiment_data["summary"] = section.replace("Summary:", "").strip()
        elif "Conclusion" in section:
            sentiment_data["conclusion"] = section.replace("Conclusion:", "").strip()'''

    return content ##returns the response from the model with description in the form of string

