import streamlit as st
import pickle
import pandas as pd
import requests

with st.sidebar:
    st.header("MOVIE RECOMMENDATION SYSTEM")
    with st.expander("About application"):
        st.markdown("A content based movie recommendation system which recommends similar movies to user based on his search and interest. ")
        st.markdown("Implemented using KNN Model and cosine similarity ")
        st.markdown("This project is built under Microsoft Engage Mentorship program '22")
    with st.expander("Features"):
        st.markdown("A search bar which fetches movies from TDMB API and provide suggestion to user to watch similar kind of movies which he may like. ")
    with st.expander("About Me"):
        st.markdown('''Hi, I am Tanya Bharti, a second-year undergraduate pursuing my Bachelor’s degree in the field of Computer Science from the Indian Institute of Information Technology, Lucknow.''')
        st.markdown('''I am a tech-enthusiast, actively exploring this vast ocean and its practical applications, to find what interests me the most. I love problem-solving and taking up new challenges in life.''')
        st.markdown("You will find me trying to up-skill myself every day! :)")
        st.caption("GITHUB: https://github.com/tanyabharti")
        st.caption("LINKEDIN: https://www.linkedin.com/in/tanya-bharti/")

    st.caption("GitHub Repository: https://github.com/tanyabharti/the-movie-station")





def extract_poster(movie_id):
    api_url = 'https://api.themoviedb.org/3/movie/{}?api_key=8769a12bf1747be7fb26da3e11d74f9a&language=en-US'.format(movie_id)
    response_data = requests.get(api_url)
    collect_data = response_data.json()
    full_data = "https://image.tmdb.org/t/p/w500/" + collect_data['poster_path']
    return  full_data

def suggest(movie):
    index = movies_set[movies_set['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetching the movie posters from TMDB API
        movie_id = movies_set.iloc[i[0]].movie_id
        recommended_movie_posters.append(extract_poster(movie_id))
        recommended_movie_names.append(movies_set.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.title(" 🎬 Movie Station 🎬")
st.markdown("Movie Station is an online movie recommendation system which recommends user alike movies based on his search and interest.")
movies_data = pickle.load(open('movie_recommendation_system.pkl', 'rb'))
movies_set = pd.DataFrame(movies_data)
similarity=pickle.load(open("similarity.pkl","rb"))

fetched_movie = st.selectbox(
     'Type  the movie name  to get recommendation of similar movies',
       movies_set['title'].values
)

if st.button('Show Recommendations'):
    st.markdown("Movies which you may like:")
    movie_names,movie_posters = suggest(fetched_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        col1.image(movie_posters[0])
        st.markdown(movie_names[0])
    with col2:
        col2.image(movie_posters[1])
        st.markdown(movie_names[1])
    with col3:
        col3.image(movie_posters[2])
        st.markdown(movie_names[2])
    with col4:
        col4.image(movie_posters[3])
        st.markdown(movie_names[3])
    with col5:
        col5.image(movie_posters[4])
        st.markdown(movie_names[4])

