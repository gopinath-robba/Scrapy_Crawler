import os
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')
                text = soup.get_text()
                text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
                documents.append(text)
    return documents

# Load documents from the specified directory
documents = load_documents('../books_crawler')

# Continue with your existing code to create the TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Save the vectorizer and TF-IDF matrix
with open('tfidf_vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)
with open('tfidf_matrix.pkl', 'wb') as mat_file:
    pickle.dump(tfidf_matrix, mat_file)
