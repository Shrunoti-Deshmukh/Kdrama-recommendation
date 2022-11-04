import pickle
import streamlit as st
import requests

def recommend(drama):
    index = dramas[dramas['title'] == drama].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    print("index", index, "\ndistances", distances)

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(dramas.iloc[i[0]].poster_img_url)
        recommended_movie_names.append(dramas.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters
# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#2d3436'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
font = "sans serif"
st.header('Movie Recommender System')
dramas = pickle.load(open('data_drama.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


kdrama_list = dramas['title'].values
print(len(kdrama_list))
selected_movie = st.selectbox(
    "Type or select a K-Drama from the dropdown",
    kdrama_list
)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
