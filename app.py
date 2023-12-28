import streamlit as st
import pickle
import pandas as pd
st.title('Movie Recommender')

similarity=pickle.load(open('sim.pkl','rb'))
def recommend(movie):
    movie_index =movies[movies['title_y']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended=[]
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title_y)
    return recommended



movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

selected_movie_name= st.selectbox(
'How would you like to be contacted',
movies['title_y'].values)

if st.button('Recommend'):
    recommended=recommend(selected_movie_name)
    for i in recommended:
        st.write(i)