import pandas as pd
import streamlit as st

def recommend(drama):
    index = dramas[dramas['name'] == drama].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(dramas.iloc[i[0]].poster_img_url)
        recommended_movie_names.append(dramas.iloc[i[0]]['name'])
    return recommended_movie_names, recommended_movie_posters

st.header('K-Drama Recommender System')
dramas = pd.read_pickle('kdrama_list.pkl')
similarity = pd.read_pickle('similarity.pkl')


kdrama_list = dramas['name'].values
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
