import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='AI Engineer',page_icon='items\logo.png',layout='wide')

with st.sidebar:
    select1 = option_menu('Admin',['Home'])

with st.sidebar:
    select2 = option_menu('Title',['Introduction'])



if select1 == 'Home':
    col1,col2,col3 = st.columns([3.5,3,3.5])
    with col2:
        st.title("AI Engineer")
    st.divider()
    st.header('Introduction')
    st.write('''
        AI Engineer — From Beginner to Advanced,\n
        This project is a complete, structured, and practical learning platform for aspiring AI Engineers, designed to take you from absolute beginner to advanced industry-ready level.\n
        It covers the entire AI Engineering roadmap step by step, with every major concept organized line by line and layer by layer, so learners can build their knowledge progressively rather than jumping randomly between technologies.\n
        From Python, Mathematics, Data Structures, Machine Learning, Deep Learning, NLP, Computer Vision, Generative AI, LLMs, Transformers, RAG, AI Agents, Vector Databases, MLOps, APIs, Cloud Deployment, and Production AI Systems — the roadmap is designed to cover the complete journey of an AI Engineer.\n
        ''')