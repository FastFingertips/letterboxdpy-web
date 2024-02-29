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
    watchlist = List(username)

    st.json(watchlist.jsonify(), expanded=False)

    if  watchlist.count:
        st.dataframe(
            pd.DataFrame(
                [(slug, f'https://letterboxd.com/film/{title}/') for slug, title in watchlist.movies],
                columns=["Title", "LetterboxdURI"]
                ),
                hide_index=True,
                use_container_width=True,
                )
    else:
        st.write("No movies found in watchlist.")