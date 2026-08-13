import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='AI Engineer',page_icon='items\logo.png',layout='wide')

with st.sidebar:
    select = option_menu('MENU',['Home','Introduction'])



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
    st.header('1. What is an AI Engineer?')
    st.write('''
        An AI Engineer is a software engineer who specializes in building, integrating, deploying, and maintaining applications powered by Artificial Intelligence.\n
        Unlike someone who only trains machine learning models, an AI Engineer focuses on turning AI capabilities into real-world, usable products and systems. They work across software engineering, machine learning, data, cloud infrastructure, and modern AI technologies.\n
        An AI Engineer may work with technologies such as Machine Learning, Deep Learning, Natural Language Processing (NLP), Computer Vision, Generative AI, Large Language Models (LLMs), RAG, AI Agents, Vector Databases, APIs, and MLOps.\n
        The core objective of an AI Engineer is to take an AI idea or model and transform it into a reliable, scalable, production-ready application.\n
        In simple terms: An AI Engineer builds intelligent software that can learn, understand, predict, generate, automate, and make decisions using AI technologies.\n
        ''')
    st.divider()
    st.header('2. Roles and Responsibilities of an AI Engineer')
    st.write('An AI Engineer has a broad range of responsibilities because modern AI systems require much more than just model training.')
    st.subheader('1. AI & Machine Learning Development')
    st.write('AI Engineers develop and integrate machine learning and deep learning models for tasks such as prediction, classification, recommendation, and automation.')
    st.subheader('2. Data Processing')
    st.write('They collect, clean, transform, analyze, and prepare data so that it can be effectively used by AI systems.')
    st.subheader('3. Generative AI & LLM Applications')
    st.write('Modern AI Engineers work with Large Language Models, embeddings, prompt engineering, RAG pipelines, AI Agents, and other Generative AI technologies to build intelligent applications.')
    st.subheader('4. AI System Integration')
    st.write('They connect AI models with existing software through APIs, databases, backend services, and external tools.')
    st.subheader('5. Model Deployment')
    st.write('An AI model is useful only when people can actually use it. AI Engineers deploy models and AI applications to cloud platforms, servers, containers, or production environments.')
    st.subheader('6. Performance & Scalability')
    st.write('They optimize AI systems for speed, cost, reliability, memory usage, and scalability, especially when thousands or millions of users may interact with the application.')
    st.subheader('7. Monitoring & Maintenance')
    st.write('After deployment, AI systems must be monitored and continuously improved. AI Engineers track model performance, failures, latency, data changes, and system reliability.')
    st.subheader('8. Collaboration')
    st.write('AI Engineers work closely with software engineers, data scientists, ML engineers, product managers, designers, and DevOps/MLOps teams to turn business requirements into working AI products.')
    st.divider()
    st.header('3. Impact of AI Engineering on Product Development')
    st.write('''
        AI Engineering has fundamentally changed how modern software products are designed and developed.\n
        Traditional software generally follows predefined rules:\n
        Input → Logic → Output\n
        AI-powered software can instead learn from data or use trained models to produce intelligent results:

        Data → AI Model → Intelligence → Application → User

        This allows companies to build products that can understand natural language, recognize images, generate content, predict outcomes, personalize experiences, automate tasks, and assist users in real time.

        Examples of AI-powered products:
        Chatbots and AI Assistants — understand and respond to human language.
        Recommendation Systems — recommend videos, products, music, or content.
        Computer Vision Systems — analyze images and videos.
        Fraud Detection Systems — identify suspicious transactions.
        AI Coding Assistants — help developers write and understand code.
        Generative AI Applications — generate text, images, audio, video, and code.
        AI Agents — perform multi-step tasks using models, tools, APIs, and external systems.
        Why AI Engineering matters

        AI Engineers bridge the gap between AI research and real-world software products.

        A powerful AI model by itself is not necessarily a useful product. It needs a complete engineering system around it — including APIs, databases, user interfaces, security, deployment, monitoring, scalability, and business logic.

        Therefore:

        AI Engineering transforms AI capabilities into reliable, scalable, and production-ready products that users can actually interact with.
    ''')
    st.divider()
    st.header('4. AI Engineer vs ML Engineer')
    st.write('Although AI Engineer and ML Engineer roles overlap significantly, their primary focus is different.')
    st.write('''
        | AI Engineer                                                             | ML Engineer                                                                                  |
        | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
        | Focuses on building complete AI-powered applications                    | Focuses heavily on machine learning systems and models                                       |
        | Works with LLMs, Generative AI, RAG, Agents, NLP, Computer Vision, etc. | Works extensively with ML algorithms, training pipelines, model optimization, and deployment |
        | Integrates AI models into software products                             | Builds and productionizes ML models                                                          |
        | Works heavily with APIs, applications, databases, and AI frameworks     | Works heavily with data pipelines, model training, evaluation, and ML infrastructure         |
        | Often works with pre-trained and foundation models                      | Often develops, fine-tunes, or optimizes ML models                                           |
        | Strong software engineering + AI application skills                     | Strong ML + software engineering + data skills                                               |


        ''')

    st.write('''
        Example

        Suppose a company wants to build an AI customer-support platform.

        An ML Engineer might focus on:

        Data → Model Training → Evaluation → Optimization → Model Deployment

        An AI Engineer might take that model or an existing LLM and build:

        LLM → RAG → Vector Database → Tools/APIs → Backend → Frontend → Authentication → Deployment → Production AI Assistant

        The relationship

        These roles are not completely separate. There is significant overlap, and the exact responsibilities vary from company to company.

        A strong AI Engineer should understand the fundamentals of Machine Learning and Deep Learning, while a strong ML Engineer increasingly benefits from understanding modern Generative AI and LLM-based systems.

        ML Engineering focuses more deeply on building and operating machine learning models, while AI Engineering focuses more broadly on turning AI capabilities into complete, production-ready intelligent applications.
        ''')
    