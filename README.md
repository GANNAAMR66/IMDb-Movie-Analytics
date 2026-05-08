# IMDb-Movie-Analytics
A data science project analyzing IMDb movie dataset using Python. It focuses on data cleaning, feature engineering, statistical analysis (percentiles, correlation), and normalization techniques to extract insights about movie ratings, runtime distribution, and revenue patterns.
#  IMDb Top 1000 Movies — Exploratory Data Analysis & Recommendation System

---

##  Project Overview

This project is a complete Data Analysis & Recommendation System pipeline built on the IMDb Top 1000 Movies dataset using Python.

It goes beyond basic analysis by transforming raw movie data into:

* meaningful insights 
* structured features 
* and a functional movie recommendation system 

The project simulates a real-world data science workflow: from raw data → cleaning → analysis → machine learning-based recommendation.

---

##  Project Objectives

* Perform end-to-end Exploratory Data Analysis (EDA)
* Clean and preprocess real-world messy data
* Engineer meaningful features for better interpretation
* Detect and handle outliers statistically
* Analyze relationships between movie attributes
* Build a Content-Based Movie Recommendation System
* Generate actionable insights from data storytelling

---

##  Dataset Description

The dataset contains information about the top 1000 IMDb movies, including:

| Feature      | Description                          |
| ------------ | ------------------------------------ |
| title        | Movie name                           |
| director     | Director of the movie                |
| release_year | Year of release                      |
| runtime      | Duration in minutes                  |
| genre        | Movie genres                         |
| rating       | IMDb user rating                     |
| metascore    | Critics’ score                       |
| gross        | Box office revenue (in millions USD) |

---

##  Data Preprocessing

A full data cleaning pipeline was applied:

###  Missing Values Handling

* Missing values in gross were filled using median imputation.

###  Duplicate Removal

* Duplicate movie titles were identified and removed.

###  Data Type Conversion

* Converted text-based numeric fields into proper numerical formats.

###  Outlier Detection

* Applied the Interquartile Range (IQR) method.

###  Winsorization

* Extreme values in gross and runtime were capped instead of removed to preserve data integrity.

---

##  Feature Engineering

To enhance analysis and recommendation quality, new features were created:

* primary_genre → Extracted main genre
* era → Cinematic era classification (Classic → Modern)
* rating_tier → Categorized ratings into quality levels
* gross_tier → Revenue-based segmentation
* rating_zscore → Standardized ratings
* runtime_norm → Normalized runtime values
* combined_features → Text-based feature representation for recommendation

---

##  Exploratory Data Analysis (EDA)

The project includes rich statistical and visual analysis:

###  Key Insights

* IMDb ratings are highly concentrated in a narrow high-quality range.
* Box office revenue is heavily skewed, with few blockbuster outliers.
* Weak correlation exists between rating and gross revenue.
* Genre and cinematic era influence ratings more than revenue.
* Movie runtime has a limited effect on perceived quality.

---

##  Visualizations

A full analytical dashboard was created using Matplotlib, including:

* Distribution of IMDb ratings
* Box office revenue distribution
* Relationship between rating and gross
* Movies per cinematic era
* Average rating by genre
* Runtime tier vs rating analysis
<img src="imdb_analysis.png" width="500"/>
---

##  Recommendation System

###  Approach: Content-Based Filtering

A machine learning-based recommendation engine was built using:

* TF-IDF Vectorization
* Cosine Similarity

---

###  How It Works

Each movie is converted into a feature representation using:

* Genre
* Director
* Rating tier
* Era

Then:

1. Movies are transformed into numerical vectors
2. Similarity between all movies is calculated
3. The system recommends the most similar movies

---

###  Output Example

If a user likes:

> *The Dark Knight*

The system may recommend:

* Batman Begins
* Inception
* Joker
* Interstellar

---

##  Technologies Used

* Python 
* Pandas
* NumPy
* Matplotlib
* Scikit-learn (TF-IDF, Cosine Similarity)

---

##  Key Learnings
This project helped develop strong practical skills in:

* Data cleaning & preprocessing
* Feature engineering techniques
* Statistical thinking
* Data visualization & storytelling
* Similarity-based recommendation systems
* End-to-end ML pipeline design

---

##  Conclusion

This project demonstrates a complete real-world data science workflow, transforming raw movie data into actionable insights and a functional recommendation engine.

It bridges the gap between:

> Data Analysis  → Machine Learning  → Real-world Application 

---

##  Author

>**Ganna Amr Emad  Eldin**

>Faculty of Artificial Intelligence
>Passionate about Data Science, Machine Learning, and AI-driven systems
