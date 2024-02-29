import streamlit as st

class Page:
    config = {
        'page_config':{ 
            'page_title':'letterboxdpy web',
            'page_icon':'🎬',
            'menu_items':{
            'Get Help': 'https://github.com/FastFingertips/letterboxdpy-web',
            'Report a bug': 'https://github.com/FastFingertips/letterboxdpy-web/issues',
            'About': 'The developer behind it is [@FastFingertips](https://github.com/FastFingertips).'
            }
        },
        'background': {
            'dark':
            """
            <style>
                .stApp {
                    background-image: linear-gradient(180deg, #20272e, 14%, #14181c, #14181c, #14181c);
                }
            </style>
            """,
            'light':
            """
            <style>
                .stApp {
                    background-image: linear-gradient(180deg, #f2f2f2, 14%, #e6e6e6, #e6e6e6, #e6e6e6);
                }
            </style>
            """
        }
    }

    st.set_page_config(**config['page_config'])
    st.markdown(config['background']['dark'], unsafe_allow_html=True)

    def __init__(self):
        self.repo_slug = 'letterboxdpy-web'
        self.create_footer()

    def create_title(self, text:str=None):
        if text is None:
            text = self.config['page_config']['page_title']
        st.title(text)

    def create_footer(self):
        st.markdown(
            """
            <style>
                .footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    margin-bottom: 1em;
                    background-color: transparent;
                    color: white;
                    text-align: center;
                }
                .footer a {text-decoration: none; margin-left: 0.5em; margin-right: 0.5em;}
                .foooter img {vertical-align: middle;}
            </style>
            <div class="footer">
                <a href="https://github.com/FastFingertips/letterboxdpy-web" target="_blank" rel="noopener noreferrer">
                    <img src="https://img.shields.io/github/last-commit/fastfingertips/letterboxdpy-web?style=flat&&label=last%20update&labelColor=%2314181C&color=%2320272E"/>
                </a>
                <img src="https://visitor-badge.laobi.icu/badge?page_id=FastFingertips.letterboxdpy-web&left_color=%2314181C&right_color=%2320272E"/>
                <a href="https://letterboxd.com/fastfingertips/" target="_blank" rel="noopener noreferrer">
                    <img src="https://img.shields.io/badge/letterboxd-fastfingertips-black?style=flat&labelColor=14181C&color=20272E"/>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

"""
[0]: name
[1]: attrs
"""

paths = {
  'film_detail_list_ul': ['ul', {'class': 'js-list-entries poster-list -p70 film-list clear film-details-list'}],
  'meta_description': ['meta', {'name':'description'}],
  'last_page_articles': ['ul', {'class': 'poster-list -p70 film-list clear film-details-list'}],
  'movie_headline_element': ['h2', {'class': 'headline-2 prettify'}],
  'last_page_no': ['div', {'class': 'paginate-pages'}]
}
