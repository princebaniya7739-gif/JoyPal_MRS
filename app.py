import streamlit as st
import pandas as pd
import pickle
import requests
import time

from streamlit import divider

movie_dict= pickle.load(open("movie_dict.pkl","rb"))
movie=pd.DataFrame(movie_dict)
similarity=pickle.load(open("similarity.pkl","rb"))


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=dfe4a6aa6f306ed25933eda5d3198753&language=en-US'
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            return "https://via.placeholder.com/500x750?text=No+Image"
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed for movie_id {movie_id}: {e}")
            time.sleep(0.1)
    return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movies):
    movies_index = movie[movie['title'] == movies].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
   
    recommend_movie=[]
    recommend_movie_posters=[]
    for i in movies_list:
        movie_id=movie.iloc[i[0]].id
        recommend_movie.append(movie.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_movie, recommend_movie_posters




st.title(":rainbow[JoyPal MRS:clapper:]")

st.divider(width="stretch")
st.subheader(":red[A Movie Recommandation System]")
st.subheader(":yellow[All type of movies are Available:]")
st.markdown(
    ":violet-badge[ Action] :orange-badge[Thriller]:gray-badge[Horror]:violet-badge[Sci-fy]:red-badge[Love]:orange-badge[Romance]:yellow-badge[Comedy]"
)

st.text('Enter Your Details and Choice: ')
Name=st.text_input(":red[Name]:")
Age=st.text_input(':red[Age]:')
Language= st.selectbox(
    ":red[Language]]",
    (
       "Select Your Language","English", "Mandarin Chinese", "Hindi", "Spanish", "French",
    "Standard Arabic", "Bengali", "Portuguese", "Russian", "Urdu",
    "Indonesian", "German", "Japanese", "Swahili", "Marathi",
    "Telugu", "Turkish", "Tamil", "Yue Chinese (Cantonese)", "Vietnamese",
    "Korean", "Italian", "Thai", "Gujarati", "Persian (Farsi)",
    "Polish", "Ukrainian", "Malayalam", "Kannada", "Burmese",
    "Punjabi", "Romanian", "Dutch", "Pashto", "Amharic",
    "Hausa", "Filipino (Tagalog)", "Sindhi", "Greek", "Hebrew",
    "Nepali", "Czech", "Swedish", "Hungarian", "Zulu",
),
    
)
Country=Gender=selected_movie_name = st.selectbox(
    ":red[Country]",
    (
      "Select Your Country","Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
    "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czechia", "Democratic Republic of the Congo",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
    "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Holy See", "Honduras", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq",
    "Ireland", "Israel", "Italy", "Jamaica", "Japan",
    "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait",
    "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali",
    "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman",
    "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal",
    "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
    "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
    "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo",
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
    "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
    "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela",
    "Vietnam", "Yemen", "Zambia", "Zimbabwe",
),
)
Gender = st.selectbox(
    ":red[Gender]",
    ("Choose Gender",'Male',"Female","Transgender"),
    
)
Genres=selected_movie_name = st.selectbox(
    ":red[Genres]",
    ("Select Your Genre",'Action',"Thriller","Romance",'Horror','Sci-fy','Love','Comedy'),
    
)




selected_movie_name = st.selectbox(
    ":violet[Choose a movie for Reference]:movie_camera:",
    ( movie['title'].values),
)



if st.button(":yellow[Recommand]",type="primary",width="content",icon="🔥"):
    st.subheader(":yellow[Your Details are:]")
    st.text(Name)
    st.text(Age)
    st.text(Gender)
    st.text(Language)
    st.text(Country)
    st.subheader(":yellow[According to your given Details , You must watch these Five Movies:]")
    
    
    name,poster=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:          
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])

sentiment_mapping = [":worried:[very bad]", ":disappointed:[bad]", ":slightly_smiling_face:[Good]", ":blush:[Very Good]",":partying:[Excellent]" ]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f" {sentiment_mapping[selected]}")

