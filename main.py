import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='AI Engineer',page_icon='items\logo.png',layout='wide')


if 'Introduction' not in st.session_state:
    st.session_state.Introduction = False

st.sidebar.title('TOPICS')
Introduction = st.sidebar.button('Introduction')
col1,col2,col3 = st.columns([3.5,3,3.5])
with col2:
    st.title("AI Engineer")

if st.button('Introduction'):
    st.session_state.Introduction = True

if st.session_state.Introduction == True:
    st.write('s')
