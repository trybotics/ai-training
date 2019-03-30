from flask import Flask, request, jsonify, render_template
import os
import requests
import json
from textblob.classifiers import NaiveBayesClassifier as NBC
import random
# random.choice([1, 2, 3])
training = [
  ('I love TechBhubaneswar.', 'positive'),
  ('this is an amazing place!', 'positive'),
  ('I feel very good about these event.', 'positive'),
  ("what an awesome view", 'positive'),
  ('this is my best work.', 'positive'),
  ('this is not bad work.', 'positive'),
  ('I do not like this restaurant', 'negative'),
  ('I am hate this kind of stuff.', 'negative'),
  ('Mark is a friend of mine.', 'negative'),
  ("I can't deal with this", 'negative'),
  ('my boss is horrible.', 'negative')
]
testing = [
  ('the beer was good.', 'positive'),
  ('the beer was not good.', 'positive'),
  ('I do not enjoy my job', 'negative'),
  ("I feel amazing!", 'positive'),
  ("I can't believe I'm doing this.", 'negative')
]
model = NBC(training) 
print(model.classify("This codes is amazing.")) 
print(model.classify("This book is not bad"))
print(model.accuracy(testing)) 

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

@app.route('/')
def chat():
    return render_template('chat.html')

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
              
    return jsonify({ "message":  model.classify(request.form['message']) })

# run Flask app
if __name__ == "__main__":
    app.run()