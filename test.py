import chat as chat
import Filter as filter
import GenShit as GenShit
from flask import Flask, request, jsonify,render_template 

def Topic_Based_Sentiment(): ##this  function exclusively Analyzes the sentiments of the topic given by the user 
    QUERY=input("Enter a Topic: ")
    chat.Scrape_Tweets(QUERY)
    if  filter.filter_text():
        print(GenShit.File_Based_Get_Response())


print(GenShit.Topic_Based_Get_Response("Narendra modi","Hes a good Prime minister"))