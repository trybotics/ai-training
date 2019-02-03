from textblob.classifiers import NaiveBayesClassifier as NBC
# from textblob import TextBlob
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
  ('I do not enjoy my job', 'negative'),
  ("I feel amazing!", 'positive'),
  ("I can't believe I'm doing this.", 'negative')
]
model = NBC(training) 
print(model.classify("This codes is amazing.")) 
print(model.classify("This book is not bad"))
print(model.accuracy(testing)) 
