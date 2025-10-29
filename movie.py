import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def recommend(movie):
    movie_index = get_index_from_title(movie)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:6]
    for i in sorted_similar_movies:
        print(get_title_from_index(i[0]))

df = pd.read_csv("movies.csv")
features = ['keywords','cast','genres','director']
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

df["combined_features"] = df.apply(combine_features,axis=1)
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)
recommend("Avatar")
