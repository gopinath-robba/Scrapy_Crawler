# Scrapy_Crawler
We will use scrapy to download website data and images from books.toscrape.com, a demo website built for web scraping purposes, which contains data about 1000 books.  


##Summary
This report details the development of a web-based search system using Scrapy, Scikit-Learn, and Flask to crawl, index, and query web documents.
Objectives is to build an efficient search system capable of processing and responding to text-based queries with relevance ranked results.

Solution involves a three-stage solution: crawling web data, indexing the data, and setting up a query processor.

Folder structure and details 
books_crawler: scripts to crawl the webpages and get the requried html files
indexing: for indexing of crawled data using TF-IDF and FAISS 
Query_processor: Real-time query handling with JSON input validation and ranked output results.

project_root/
│
├── books_crawler/                # All files related to the Scrapy crawler
│   ├── books_crawler/      # Scrapy project directory
│   │   ├── spiders/
│   │   │   ├── __init__.py
│   │   │   └── books_spider.py  # Spider crawler
│   │   ├── __init__.py
│       └── items.py
│         
│
├── indexer/                # Directory for indexing operations
│   ├── processed_data/document.txt     # Store preprocessed documents
│   ├── tfidf_vectorizer.pkl  # Saved TF-IDF vectorizer
│   ├── tfidf_matrix.pkl    # Saved TF-IDF matrix
│   └── faiss_index.faiss   # FAISS index file
│
├── query_processor/        # Flask application for query processing
│   ├── app.py              # Flask application file



Commands to setup the project:
Crawler:
Install Scrapy
First, you need to install Scrapy, 

pip install scrapy

Create a New Scrapy Project
Create a new directory

scrapy startproject books_crawler      

scrapy crawl books

Indexer:
Install Necessary Packages
pip install numpy scikit-learn faiss-cpu beautifulsoup4
pip install faiss-cpu

python preprocess.py
python build_index.py
python create_faiss_index.py


query_processor:
pip install flask
cd query_processor
python app.py


Testing the application. Make a API call from Post Master or a curl statement from terminal. Example below: 

curl -X POST -H "Content-Type: application/json" -d '{"query": "harry porter", "k": 5}' http://localhost:5000/search



