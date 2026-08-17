import streamlit as st
from streamlit_option_menu import option_menu
from llms_notes.Common_terminology import AI_AGI,LLMs,Embeddings,Training,Inference,Vector_database,ai_agent,Rags
from Introduction_notes.introduction import Intraduction


st.set_page_config(page_title='AI Engineer',page_icon='items\logo.png',layout='wide')

if 'ai_agi' not in st.session_state:
    st.session_state.ai_agi = False

if 'llms' not in st.session_state:
    st.session_state.llms = False

if 'embeddings' not in st.session_state:
    st.session_state.embeddings = False

if 'training' not in st.session_state:
    st.session_state.training = False

if 'Inference' not in st.session_state:
    st.session_state.Inference = False

if 'Vector_Databases' not in st.session_state:
    st.session_state.Vector_Databases = False

if 'AI_Agents' not in st.session_state:
    st.session_state.AI_Agents = False

if 'RAG' not in st.session_state:
    st.session_state.RAG = False

if 'Context_Window' not in st.session_state:
    st.session_state.Context_Window = False

if 'Fine_tuning' not in st.session_state:
    st.session_state.Fine_tuning = False

if 'Prompt_Engineering' not in st.session_state:
    st.session_state.Prompt_Engineering = False

if 'Context_Engineering' not in st.session_state:
    st.session_state.Context_Engineering = False


with st.sidebar:
    select = option_menu('MENU',['Home','Introduction','LLM\'s'])



if select == 'Home':
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

if select == 'Introduction':
    st.title('Introduction')
    st.divider()
    st.write(Intraduction)

if select == 'LLM\'s':
    st.title('Common terminology')
    st.divider()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        if st.button('AI VS AGI'):
            st.session_state.ai_agi = True
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False
    with col2:
        if st.button('LLM\'s'):
            st.session_state.ai_agi = False
            st.session_state.llms = True
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False

    with col3:
        if st.button('Embeddings'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = True
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False
    with col4:
        if st.button('Training'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = True
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False
    col6,col7,col8,col9 = st.columns(4)
    with col6:
        if st.button('Inference'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = True
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False

    with col7:
        if st.button('Vector Database'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = True
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False

    with col8:
        if st.button('AI Agents'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = True
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False

    with col9:
        if st.button('RAG'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = True
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False

    col10,col11,col12,col13 = st.columns(4)
    with col10:
        if st.button('Context Window'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = True
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = False
        
    with col11:
        if st.button('Fine Turning'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = True
            st.session_state.Context_Engineering = False
    with col12:
        if st.button('Prompt Engineering'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = True
            st.session_state.Context_Engineering = False
    with col13:
        if st.button('Context Engineering'):
            st.session_state.ai_agi = False
            st.session_state.llms = False
            st.session_state.embeddings = False
            st.session_state.training = False
            st.session_state.Inference = False
            st.session_state.Vector_Databases = False
            st.session_state.AI_Agents = False
            st.session_state.RAG = False
            st.session_state.Context_Window = False
            st.session_state.Fine_tuning = False
            st.session_state.Prompt_Engineering = False
            st.session_state.Context_Engineering = True
    st.divider()
    if st.session_state.ai_agi == True:
        st.write(AI_AGI)
    if st.session_state.llms == True:
        st.write(LLMs)
    if st.session_state.embeddings == True:
        st.write(Embeddings)
    if st.session_state.training == True:
        st.write(Training)
    if st.session_state.Inference == True:
        st.write(Inference)
    if st.session_state.Vector_Databases == True:
        st.write(Vector_database)
    if st.session_state.AI_Agents == True:
        st.write(ai_agent)
    if st.session_state.RAG == True:
        st.write(Rags)