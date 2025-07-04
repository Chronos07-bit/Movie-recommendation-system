import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

# TF-IDF and cosine similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def get_recommendations(title, genre_filter=None):
    if title not in indices:
        return ["Movie not found."]
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]
    recs = []
    for i, score in sim_scores:
        movie = movies.iloc[i]
        if genre_filter:
            if genre_filter.lower() in movie['genres'].lower():
                recs.append(movie['title'])
        else:
            recs.append(movie['title'])
        if len(recs) == 5:
            break
    return recs

# Streamlit interface
st.title("🎬 Movie Recommendation System")
st.write("Get movie recommendations based on content!")
movie_input = st.text_input("Enter a movie title:")
genre_options = sorted(set(g for row in movies['genres'] for g in row.split()))
genre_filter = st.selectbox("Filter by genre (optional):", [""] + genre_options)

if st.button("Get Recommendations"):
    if movie_input:
        results = get_recommendations(movie_input, genre_filter if genre_filter else None)
        for i, title in enumerate(results, 1):
            st.write(f"{i}. {title}")
    else:
        st.warning("Please enter a movie name.")
