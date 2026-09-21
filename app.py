import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page Configuration
st.set_page_config(page_title="IMDb Recommendation System", page_icon="🎬", layout="wide")

# Title and Header
st.title(" IMDb Movie Recommendation System")
st.markdown("Built by **Ganna Amr Emad** | AI & Data Engineer")
st.markdown("---")

# Load Data 
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/GANNAAMR66/IMDb-Movie-Analytics/main/datasets/imdb_clean6.csv"
    try:
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None and not df.empty:
    # Sidebar for selection
    st.sidebar.header("Movie Selection")
    selected_movie = st.sidebar.selectbox(
        "Select a movie to get recommendations:",
        df['title'].dropna().unique()
    )

    if st.sidebar.button("Get Recommendations"):
        # Create combined features for recommendation (Since there is no 'overview', we use genre and director)
        df['combined_features'] = (
            df['genre'].fillna('') + ' ' +
            df['primary_genre'].fillna('') + ' ' +
            df['director'].fillna('')
        )
        
        # Calculate TF-IDF and Cosine Similarity
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(df['combined_features'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Get index of the selected movie
        idx = df[df['title'] == selected_movie].index[0]
        
        # Get similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6] # Top 5
        
        # Display Results
        st.subheader(f"🎥 Top 5 Movies Similar to '{selected_movie}'")
        
        for i, (movie_idx, score) in enumerate(sim_scores):
            movie = df.iloc[movie_idx]
            st.markdown(f"### {i+1}. {movie['title']}")
            st.markdown(f"**Similarity Score:** {score*100:.1f}%")
            st.markdown(f"**Director:** {movie['director']} | **Genre:** {movie['genre']}")
            st.markdown(f"**Rating:** {movie['rating']} | **Year:** {movie['release_year']}")
            st.markdown("---")
else:
    st.error("Failed to load the dataset. Please check the CSV link.")
