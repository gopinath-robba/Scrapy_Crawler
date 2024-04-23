from flask import Flask, request, jsonify
import pickle
import numpy as np
import faiss

app = Flask(__name__)

# Load the vectorizer and FAISS index
with open('../indexer/tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

index = faiss.read_index('../indexer/faiss_index.faiss')

# Route to handle search queries
@app.route('/search', methods=['POST'])
def search():
    data = request.get_json(force=True)
    query = data.get('query')
    k = data.get('k', 10)  # Default top-k results

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Convert query to vector
    query_vec = vectorizer.transform([query])
    query_vec = query_vec.astype(np.float32).toarray()

    # Use FAISS to find the nearest neighbors
    distances, indices = index.search(query_vec, k)

    # You may want to convert indices to actual documents or return document IDs
    results = [f"Document {i+1}" for i in indices.flatten()]

    return jsonify(results=results)

if __name__ == '__main__':
    app.run(debug=True)
