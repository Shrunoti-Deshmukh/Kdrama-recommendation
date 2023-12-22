import pickle

dramas = pickle.load(open('kdrama_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

print(dramas.iloc[0]['name'])
def recommend(drama):
    index = dramas[dramas['name'] == drama].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        recommended_movie_posters.append(dramas.iloc[i[0]].poster_img_url)
        recommended_movie_names.append(dramas.iloc[i[0]].name)

    return recommended_movie_names, recommended_movie_posters

print(recommend('Glitch'))