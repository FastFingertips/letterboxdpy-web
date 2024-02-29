from letterboxdpy.user import User, user_lists
from letterboxdpy.list import List
from models.manager import Input
from models.config import Page
import streamlit as st
import pandas as pd

# Render
page = Page()

input_manager = Input()
username = st.session_state.get('username', None)

if not username:
    st.write("Please enter a username")

if username:
    user_instance = User(username)
    data = user_lists(user_instance)

    if data['count']:
        # selectbox
        list_names = [v['slug'] for v in data['lists'].values()]

        # selected
        selected_list = st.selectbox('Select a list', list_names)
        list_data = List(username, selected_list)

        list_title = list_data.title
        list_description = list_data.description
        list_count = list_data.count
        list_url = list_data.url

        list_movies = list_data.movies

        st.title(list_title)
        st.write(f"Description: {list_description}")
        st.write(f"Movies: {list_count}")
        st.write(f"URL: {list_url}")

        columns = ["Rank", "Title", "LetterboxdURI"]

        st.dataframe(
            pd.DataFrame(
                [(title, f'https://letterboxd.com/film/{slug}/') for title, slug in list_movies],
                columns=[]
                ),
                hide_index=True,
                use_container_width=True,
            )
    else:
        st.write("No lists found o_0")