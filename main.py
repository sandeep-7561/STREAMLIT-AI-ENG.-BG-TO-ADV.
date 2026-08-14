import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='AI Engineer',page_icon='items\logo.png',layout='wide')

with st.sidebar:
    select = option_menu('MENU',['Home','Introduction','Common terminology'])



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

if select == 'Common terminology':
    st.title('Common terminology')
    st.divider()
    st.write('''
        # Artificial Intelligence (AI) vs Artificial General Intelligence (AGI)

        ## 1. What is Artificial Intelligence (AI)?

        **Artificial Intelligence (AI)** is the field of computer science focused on creating systems that can perform tasks that normally require human intelligence.

        AI systems can be designed to **recognize patterns, understand language, analyze data, make predictions, generate content, solve problems, and make decisions**.

        Examples of AI applications include:

        * Image and face recognition
        * Speech recognition
        * Recommendation systems
        * Fraud detection
        * Machine translation
        * Chatbots
        * Autonomous systems
        * Generative AI
        * AI-powered coding assistants

        ### Narrow AI (ANI)

        Most AI systems used today can be considered **Artificial Narrow Intelligence (ANI)**. They are designed for specific tasks or a limited range of capabilities.

        For example, a recommendation system may be highly effective at predicting what content a user might like, but that does not mean it can automatically perform unrelated tasks such as teaching mathematics, designing a database, or diagnosing a computer problem.

        > **AI focuses on creating intelligent systems that can perform specific or defined tasks effectively.**

        ---

        # 2. What is Artificial General Intelligence (AGI)?

        **Artificial General Intelligence (AGI)** refers to a hypothetical form of AI with **general-purpose intelligence** that can learn, reason, adapt, and solve a broad range of intellectual problems across different domains.

        Instead of being designed primarily for one specific task, an AGI system would be expected to transfer knowledge and skills between different types of problems and adapt to new situations.

        For example, a sufficiently capable AGI could potentially:

        * Learn a programming language
        * Solve mathematical problems
        * Understand natural language
        * Analyze scientific information
        * Plan complex tasks
        * Learn from new experiences
        * Use external tools
        * Adapt to unfamiliar situations
        * Apply knowledge across different domains

        The key concept behind AGI is **generality**.

        > **AGI aims to create a system with broad, adaptable intelligence rather than intelligence limited to a particular task or domain.**

        ---

        # 3. AI vs AGI

        | AI                                                                          | AGI                                                                                  |
        | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
        | Artificial Intelligence                                                     | Artificial General Intelligence                                                      |
        | Can be designed for specific tasks or domains                               | Designed as a concept for broad, general-purpose intelligence                        |
        | Often specialized                                                           | Intended to be highly general and adaptable                                          |
        | Usually operates within defined capabilities                                | Expected to handle unfamiliar tasks and domains                                      |
        | Examples include recommendation systems, vision models, and fraud detection | AGI remains a research goal/concept                                                  |
        | Does not necessarily require human-level general intelligence               | Aims for broad intelligence comparable to or beyond human general-purpose capability |

        ### Simple Example

        Imagine an AI system trained specifically for **chess**.

        It can analyze positions, predict moves, and play chess extremely well.

        But if you ask it:

        > "Build me a website."

        Its chess expertise does not automatically transfer to web development.

        Now imagine a hypothetical AGI system.

        You could give it a goal such as:

        > "Build a complete website."

        It could potentially understand the objective, learn what it needs, plan the work, write the code, test it, fix problems, and adapt when something unexpected happens.

        That ability to **transfer knowledge, learn new skills, and adapt across different domains** is central to the idea of AGI.

        ---

        # 4. Key Capabilities Associated with AGI

        AGI is generally discussed in terms of several broad capabilities:

        ### **Learning**

        The ability to acquire new knowledge and skills from data, experience, or instruction.

        ### **Reasoning**

        The ability to analyze information, understand relationships, and reach logical conclusions.

        ### **Planning**

        The ability to break a complex goal into multiple steps and determine an effective course of action.

        ### **Adaptation**

        The ability to adjust behavior when the environment, task, or available information changes.

        ### **Generalization**

        The ability to apply knowledge or skills learned in one situation to new and different situations.

        ### **Memory**

        The ability to retain and use relevant information when solving future problems.

        ### **Tool Use**

        The ability to interact with external tools such as software, APIs, databases, browsers, or other systems.

        ### **Autonomy**

        The ability to work toward a goal with limited step-by-step human instruction.

        ---

        # 5. AGI Does Not Mean a Robot

        AGI and robotics are different concepts.

        **AGI refers to intelligence**, while a **robot is a physical machine**.

        An AGI system could theoretically exist as software running on computers or cloud infrastructure without having a physical body.

        A robot could potentially use an AGI-like system as its intelligence.

        ```text
        AGI / General Intelligence
                ↓
            Intelligence
                ↓
        ┌────────┼────────┐
        ↓        ↓        ↓
        Computer  Robot    Cloud
        ```

        Therefore:

        > **AGI ≠ Robot**

        ---

        # 6. AGI vs Superintelligence

        AGI should also be distinguished from **Artificial Superintelligence (ASI)**.

        ### AGI

        A hypothetical AI system with broad, general-purpose intelligence capable of handling a wide range of intellectual tasks.

        ### ASI

        A hypothetical AI system whose general intellectual capabilities **far exceed those of humans** across essentially all relevant cognitive domains.

        A simplified conceptual model is:

        ```text
        Narrow AI
            ↓
        Artificial General Intelligence (AGI)
            ↓
        Artificial Superintelligence (ASI)
        ```

        However, this should **not** be interpreted as a guaranteed development path.

        ---

        # 7. Is AGI Already Here?

        There is **no universally accepted definition or definitive test for AGI**, so claims about whether a particular current AI system qualifies as AGI depend heavily on the criteria being used.

        Modern AI systems can demonstrate impressive capabilities across many domains, but **highly capable AI is not automatically equivalent to AGI**.

        The central question is whether a system can reliably demonstrate the broad **learning, reasoning, generalization, and adaptation** expected from general intelligence across a sufficiently wide range of tasks and unfamiliar situations.

        ---

        # 8. The Fundamental Difference

        The simplest way to remember the distinction is:

        ### **AI**

        > **Build intelligent systems that can perform useful tasks.**

        ### **AGI**

        > **Build a general-purpose intelligent system that can learn, reason, adapt, and solve a broad range of new problems across different domains.**

        ---

        ## Final Mental Model

        ```text
                        ARTIFICIAL INTELLIGENCE
                                │
                    ┌────────────┴────────────┐
                    ↓                         ↓
                NARROW AI                    AGI
            Specific / Limited          General Purpose
                Intelligence                Intelligence
                    │                         │
            Specific Tasks            Multiple Domains
                    │                         │
            Defined Capability       Learn + Reason + Adapt
                                            │
                                            ↓
                                        AGI Concept
                                            │
                                            ↓
                                            ASI*
        ```

        * **ASI (Artificial Superintelligence)** is a hypothetical concept involving intelligence that substantially exceeds human capabilities.

        ### **In one sentence:**

        > **AI is the broader field of building intelligent machines, while AGI represents the goal of creating a general-purpose intelligence that can learn, reason, adapt, and apply its capabilities across a wide range of tasks and domains.**

        ''')