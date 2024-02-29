from letterboxdpy.user import User
from models.manager import Input
from models.config import Page
import streamlit as st


# Render
page = Page()

input_manager = Input()
username = st.session_state.get('username', None)

if not username:
    st.write("Please enter a username")

if username:
    user_instance = User(username)

    user_info = user_instance.jsonify()
    st.json(user_info, expanded=False)

    # Creating the table
    table_content = f"""
    <table>
        <tr>
            <td rowspan="6" style="vertical-align: top;">
                <img src="{user_info['avatar']['url']}" alt="Avatar" width="200">
            </td>
            <th>Bio</th>
            <td>{user_info['bio'] if 'bio' in user_info else '?'}</td>
        </tr>
        <tr>
            <th>Films</th>
            <td>{user_info['stats']['films'] if 'films' in user_info['stats'] else '?'}</td>
        </tr>
        <tr>
            <th>Following</th>
            <td>{user_info['stats']['following'] if 'following' in user_info['stats'] else '?'}</td>
        </tr>
        <tr>
            <th>Followers</th>
            <td>{user_info['stats']['followers'] if 'followers' in user_info['stats'] else '?'}</td>
        </tr>
        <tr>
            <th colspan>Favorite Films</th>
            <td colspan>{' | '.join([v['name'] for v in user_info['favorites'].values()]) if user_info['favorites'] else "?"}</td>
        </tr>
    </table>
    """

    st.markdown(table_content, unsafe_allow_html=True)