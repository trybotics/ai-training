import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load('en')

# Process whole documents
text = ("My Name is Peter")
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

# # Determine semantic similarities
# doc1 = nlp(u"my fries were super gross")
# doc2 = nlp(u"such disgusting fries")
# similarity = doc1.similarity(doc2)
# print(doc1.text, doc2.text, similarity)