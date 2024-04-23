import os
from bs4 import BeautifulSoup
import re

def load_and_preprocess(directory):
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

# Define the directory path for crawled HTML files
crawled_dir = '../books_crawler'
documents = load_and_preprocess(crawled_dir)

# Optionally, save processed text for further use
with open('processed_data/documents.txt', 'w', encoding='utf-8') as f:
    for doc in documents:
        f.write(doc + '\n')
