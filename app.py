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
    # IMPORTANT: Replace the URL below with your actual raw GitHub CSV link!
    url = "https://raw.githubusercontent.com/GANNAAMR66/IMDb-Movie-Analytics/main/datasets/imdb_clean6.csv"
    try:
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None:
    # Sidebar for selection
    st.sidebar.header("Movie Selection")
    selected_movie = st.sidebar.selectbox(
        "Select a movie to get recommendations:",
        df['Series_Title'].dropna().unique()
    )

    if st.sidebar.button("Get Recommendations"):
        # Check if required columns exist
        if 'Genre' in df.columns and 'Overview' in df.columns:
            # Combine Genre and Overview for better recommendations
            df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
            
            # Calculate TF-IDF and Cosine Similarity
            tfidf = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf.fit_transform(df['combined_features'])
            cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
            
            # Get index of the selected movie
            idx = df[df['Series_Title'] == selected_movie].index[0]
            
            # Get similarity scores
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6] # Top 5
            
            # Display Results
            st.subheader(f"🎥 Top 5 Movies Similar to '{selected_movie}'")
            
            for i, (movie_idx, score) in enumerate(sim_scores):
                movie = df.iloc[movie_idx]
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown(f"**#{i+1}**")
                with col2:
                    st.markdown(f"### {movie['Series_Title']}")
                    st.markdown(f"**Similarity Score:** {score*100:.1f}%")
                    st.markdown(f"**Genre:** {movie['Genre']} | **IMDB Rating:** {movie['IMDB_Rating']}")
                    st.markdown(f"**Overview:** {movie['Overview'][:150]}...")
                    st.markdown("---")
        else:
            st.error("The dataset is missing 'Genre' or 'Overview' columns. Please check your CSV file.")
else:
    st.info("Please update the `url` variable in the code with your raw GitHub CSV link to load the data.")
