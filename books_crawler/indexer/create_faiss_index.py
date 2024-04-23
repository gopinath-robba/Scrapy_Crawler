import faiss
import numpy as np
import pickle

# Load TF-IDF matrix from file
with open('tfidf_matrix.pkl', 'rb') as mat_file:
    tfidf_matrix = pickle.load(mat_file)

# Convert to FAISS compatible format
tfidf_array = tfidf_matrix.astype(np.float32).toarray()
index = faiss.IndexFlatL2(tfidf_array.shape[1])  # or IndexFlatIP for cosine similarity
index.add(tfidf_array)

# Save the FAISS index
faiss.write_index(index, 'faiss_index.faiss')
