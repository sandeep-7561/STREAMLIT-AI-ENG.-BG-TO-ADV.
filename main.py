import streamlit as st
from streamlit_option_menu import option_menu

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
                                                ASI
            ```

            * **ASI (Artificial Superintelligence)** is a hypothetical concept involving intelligence that substantially exceeds human capabilities.

            ### **In one sentence:**

            > **AI is the broader field of building intelligent machines, while AGI represents the goal of creating a general-purpose intelligence that can learn, reason, adapt, and apply its capabilities across a wide range of tasks and domains.**

        ''')
        st.divider()

    if st.session_state.llms == True:
        st.write('''
        # Large Language Models (LLMs)

        ## 1. What is an LLM?

        **LLM stands for Large Language Model.**

        A Large Language Model is a type of **deep learning model** designed to understand and generate human language. LLMs are trained on very large amounts of text and other data so they can learn patterns, relationships, structures, and representations within language.

        Modern LLMs are primarily based on the **Transformer architecture**.

        Examples of well-known LLMs include:

        * GPT
        * Claude
        * Gemini
        * Llama
        * Mistral

        The fundamental idea behind an LLM is:

        > **Given the context, predict the next token and use that prediction repeatedly to generate a response.**

        ---

        # 2. Why is it called a "Large" Language Model?

        The word **Large** refers mainly to the scale of the model and its training process.

        Large models can have:

        * Billions or more parameters
        * Very large training datasets
        * Large computational requirements
        * Large neural network architectures

        A **parameter** is a numerical value learned during training that helps the neural network determine how information should be processed.

        In simple terms:

        > **More parameters and larger training systems can allow a model to learn much more complex patterns, although bigger does not automatically mean better.**

        ---

        # 3. How Does an LLM Work?

        A simplified LLM pipeline looks like this:

        ```text
        User Prompt
            ↓
        Tokenization
            ↓
        Token IDs
            ↓
        Embeddings
            ↓
        Transformer Layers
            ↓
        Self-Attention
            ↓
        Neural Network Computation
            ↓
        Next-Token Probability
            ↓
        Next Token
            ↓
        Repeat
            ↓
        Final Response
        ```

        Let's understand the important stages.

        ---

        # 4. Tokenization

        An LLM does not directly process raw text like a human.

        The input text is first converted into **tokens**.

        For example:

        ```text
        "Python is powerful"
        ```

        may be represented approximately as:

        ```text
        ["Python", " is", " powerful"]
        ```

        Depending on the tokenizer, a word may also be split into smaller pieces.

        Each token is then converted into a numerical **token ID** that the model can process.

        ---

        # 5. Embeddings

        Token IDs are converted into numerical vectors called **embeddings**.

        Conceptually:

        ```text
        Python
        ↓
        [0.21, -0.73, 0.44, 0.91, ...]
        ```

        These vectors provide a mathematical representation of tokens that the neural network can process.

        Embeddings allow the model to represent relationships and patterns between different tokens.

        ---

        # 6. Transformer Architecture

        Most modern LLMs use the **Transformer architecture**.

        A Transformer contains multiple neural network layers that process the input context.

        A simplified representation is:

        ```text
        Input Embeddings
            ↓
        Self-Attention
            ↓
        Feed-Forward Network
            ↓
        Normalization
            ↓
        Next Transformer Layer
            ↓
        ...
            ↓
        Output
        ```

        Large LLMs can contain many Transformer layers.

        ---

        # 7. Self-Attention

        **Self-attention** is one of the most important mechanisms in a Transformer.

        It allows the model to determine which parts of the input context are more relevant to each other.

        For example:

        > **"The developer opened the laptop because it was slow."**

        The model needs to understand what **"it"** refers to.

        Self-attention helps the model calculate relationships between the tokens in the sentence.

        Technically, attention uses:

        * **Query (Q)**
        * **Key (K)**
        * **Value (V)**

        A simplified attention equation is:

        [
        Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
        ]

        The resulting attention weights determine how information from different tokens contributes to the current representation.

        ---

        # 8. Next-Token Prediction

        The core generation mechanism of an LLM is **next-token prediction**.

        Suppose the input is:

        > **"The capital of France is"**

        The model calculates probabilities for possible next tokens.

        Conceptually:

        ```text
        Paris     → 0.97
        London    → 0.01
        Berlin    → 0.005
        Madrid    → 0.003
        ```

        The model selects a token according to its decoding strategy.

        The sequence then becomes:

        ```text
        The capital of France is Paris
        ```

        The model predicts the next token again.

        This process continues until the response is complete.

        > **An LLM generates text sequentially, token by token.**

        ---

        # 9. How is an LLM Trained?

        During training, the model processes huge amounts of data and repeatedly attempts to predict missing or subsequent tokens.

        For example:

        ```text
        "The sun rises in the ___"
        ```

        The model may initially produce an incorrect prediction.

        The correct target is:

        > **east**

        The difference between the model's prediction and the expected target contributes to the **loss**.

        The training process then uses:

        ```text
        Prediction
            ↓
        Loss Calculation
            ↓
        Backpropagation
            ↓
        Gradient Calculation
            ↓
        Weight Update
        ```

        This process is repeated across a very large number of training examples.

        Over time, the model learns complex patterns in language and other training data.

        ---

        # 10. What Does an LLM Learn?

        An LLM does not simply memorize a collection of question-and-answer pairs.

        During training, its neural network parameters are adjusted to represent learned patterns and relationships.

        These can include patterns related to:

        * Grammar
        * Syntax
        * Semantics
        * Language structure
        * Programming
        * Reasoning patterns
        * General knowledge
        * Relationships between concepts

        This learned representation allows the model to generate new combinations of information rather than only returning exact stored sentences.

        ---

        # 11. LLMs Are Not Traditional Databases

        An LLM should not be thought of as a normal database.

        ### Database

        ```text
        Query
        ↓
        Search stored records
        ↓
        Return matching data
        ```

        ### LLM

        ```text
        Prompt
        ↓
        Neural Network Computation
        ↓
        Probability Distribution
        ↓
        Token Generation
        ↓
        Response
        ```

        Because an LLM generates text probabilistically, it can sometimes produce information that is incorrect.

        This is commonly referred to as an **AI hallucination**.

        ---

        # 12. Example of LLM Generation

        Suppose the user asks:

        > **"Explain Python loops."**

        The LLM receives the prompt and processes it through its Transformer architecture.

        It then generates tokens progressively:

        ```text
        Python
        ↓
        Python loops
        ↓
        Python loops are
        ↓
        Python loops are used
        ↓
        Python loops are used to
        ↓
        Python loops are used to repeat
        ↓
        ...
        ```

        Eventually, these tokens form the complete response.

        ---

        # 13. LLMs and Context

        An LLM uses the available **context** to generate its next tokens.

        For example:

        ```text
        User:
        What is Python?

        Assistant:
        Python is a programming language...

        User:
        What is it used for?
        ```

        The model uses the previous conversation context to interpret what **"it"** refers to.

        However, context handling has limits, which are related to the model's **context window**.

        ---

        # 14. What is a Context Window?

        A **context window** is the amount of text or tokens that an LLM can process as context during an interaction.

        Conceptually:

        ```text
        Context Window
        ┌───────────────────────────────┐
        │ System Instructions           │
        │ Previous Conversation         │
        │ User Prompt                   │
        │ Documents / Retrieved Data    │
        └───────────────────────────────┘
                        ↓
                    LLM
                        ↓
                    Response
        ```

        Larger context windows allow models to work with more information in a single interaction.

        ---

        # 15. LLM vs Traditional Machine Learning

        Traditional machine learning models are often designed for specific tasks.

        For example:

        ```text
        Input Data
        ↓
        ML Model
        ↓
        Prediction
        ```

        An LLM is a **general-purpose language model** that can be adapted to many language-based tasks.

        For example, the same LLM can potentially be used for:

        * Question answering
        * Summarization
        * Translation
        * Code generation
        * Classification
        * Content generation
        * Information extraction
        * Conversational assistants

        ---

        # 16. LLMs in Real-World AI Applications

        An LLM is often only one component of a complete AI system.

        A production AI application may look like:

        ```text
        User
        ↓
        Frontend
        ↓
        Backend
        ↓
        LLM
        ├── RAG
        ├── Vector Database
        ├── APIs
        ├── Tools
        └── Memory
        ↓
        Response
        ```

        This is where **AI Engineering** becomes important.

        AI Engineers take models such as LLMs and integrate them with software systems to create useful applications.

        ---

        # 17. LLM + RAG

        A standalone LLM may not know your private company documents or the latest information.

        **RAG (Retrieval-Augmented Generation)** can provide relevant external information to the model.

        Simplified flow:

        ```text
        User Question
            ↓
        Retrieve Relevant Documents
            ↓
        Relevant Context
            ↓
        LLM
            ↓
        Generated Answer
        ```

        This allows an LLM application to answer questions using information retrieved from external knowledge sources.

        ---

        # 18. LLM + Tools

        LLMs can also be connected to external tools.

        For example:

        ```text
        User
        ↓
        LLM
        ├── Calculator
        ├── Web Search
        ├── Database
        ├── Python
        ├── APIs
        └── File System
        ↓
        Final Response
        ```

        This allows an AI application to perform actions rather than only generating text.

        ---

        # 19. Key Limitations of LLMs

        LLMs are powerful, but they are not perfect.

        Common limitations include:

        * Hallucinations
        * Outdated knowledge depending on the model and setup
        * Limited context
        * Reasoning failures
        * Sensitivity to prompts
        * Computational cost
        * Latency
        * Bias in training data
        * Lack of guaranteed factual accuracy

        Therefore, production AI systems often require **retrieval, validation, tool use, monitoring, evaluation, and guardrails**.

        ---

        # 20. LLM — Key Takeaway

        > **A Large Language Model is a large neural network, typically based on the Transformer architecture, trained on massive datasets to learn patterns in language and generate responses by predicting the next token from the available context.**

        The most important concepts to remember are:

        ```text
        LLM
        │
        ├── Tokenization
        ├── Embeddings
        ├── Transformer
        ├── Self-Attention
        ├── Training
        ├── Parameters
        ├── Context Window
        ├── Next-Token Prediction
        ├── Fine-Tuning
        ├── RAG
        ├── Tool Use
        └── AI Applications
        ```

        ### **One-line definition**

        > **An LLM is a Transformer-based neural network trained on large-scale data that generates language by predicting tokens based on the context it receives.**

        ''')

    if st.session_state.embeddings == True:
        st.write('''
        # Embeddings in Artificial Intelligence

        ## 1. What are Embeddings?

        **Embeddings are numerical vector representations of data such as text, images, audio, or other information.**

        They convert complex data into a mathematical form that AI systems can process, compare, search, and analyze.

        For example:

        ```text
        "Python programming"
                ↓
        Embedding Model
                ↓
        [0.21, -0.54, 0.87, 0.14, ...]
        ```

        The resulting list of numbers is called an **embedding vector**.

        > **An embedding represents information in a numerical vector space where relationships and similarities can be measured mathematically.**

        ---

        # 2. Why Do We Need Embeddings?

        Computers cannot naturally understand the meaning of human language in the same way humans do.

        Consider:

        ```text
        "I love Python programming."

        "I enjoy coding in Python."
        ```

        These sentences use different words, but their meanings are very similar.

        Embeddings convert them into vectors so that an AI system can mathematically determine that they are semantically related.

        Conceptually:

        ```text
        Sentence A → [0.12, 0.45, -0.32, ...]
        Sentence B → [0.15, 0.42, -0.29, ...]
        ```

        Because their representations are similar, the vectors can be close to each other in the embedding space.

        ---

        # 3. Embedding Vector

        An embedding is represented as a vector containing many numerical values.

        For example:

        ```text
        "Cat"
            ↓
        [0.21, -0.43, 0.76, 0.18, -0.09, ...]
        ```

        Real embedding vectors can contain **hundreds or thousands of dimensions**, depending on the embedding model.

        Each dimension is not normally interpreted as one simple human-readable feature. Instead, information is distributed across many dimensions.

        ---

        # 4. Semantic Similarity

        One of the most important properties of embeddings is that they can represent **semantic relationships**.

        For example:

        ```text
        "Dog"
        "Cat"
        "Pet"
        ```

        may have relatively similar representations because they are semantically related.

        Whereas:

        ```text
        "Dog"
        "Database"
        ```

        would generally be much less similar.

        Conceptually:

        ```text
                Dog
                ●
            /   \
            ●     ●
            Cat    Pet


                            Database
                                ●
        ```

        The actual embedding space is usually hundreds or thousands of dimensions rather than a simple 2D diagram.

        ---

        # 5. How Embeddings Work

        A simplified embedding pipeline is:

        ```text
        Input Data
            ↓
        Embedding Model
            ↓
        Numerical Vector
            ↓
        Vector Representation
            ↓
        Similarity / Search / Retrieval
        ```

        For text:

        ```text
        Text
        ↓
        Tokenizer / Text Processing
        ↓
        Embedding Model
        ↓
        Vector
        ```

        The embedding model is trained to produce representations that are useful for particular semantic or similarity-based tasks.

        ---

        # 6. Embeddings vs Tokenization

        These two concepts are related but different.

        ### Tokenization

        Tokenization breaks text into smaller units called **tokens**.

        ```text
        "Python is powerful"
                ↓
        ["Python", " is", " powerful"]
        ```

        ### Embedding

        An embedding converts text or tokens into a numerical vector representation.

        ```text
        "Python programming"
                ↓
        [0.21, -0.54, 0.87, ...]
        ```

        A simplified pipeline is:

        ```text
        Text
        ↓
        Tokenization
        ↓
        Tokens / Token IDs
        ↓
        Embedding
        ↓
        Vectors
        ```

        ---

        # 7. Similarity Search

        One of the most important applications of embeddings is **semantic similarity search**.

        Suppose you have thousands of documents.

        The user searches:

        > **"How can I learn Python?"**

        A document may contain:

        > **"A beginner's guide to Python programming."**

        The exact words are different, but the meaning is similar.

        Embedding-based search works like this:

        ```text
        User Query
            ↓
        Query Embedding
            ↓
        Query Vector
            ↓
        Compare with Document Vectors
            ↓
        Find Most Similar Vectors
            ↓
        Retrieve Relevant Documents
        ```

        This is called **semantic search**.

        ---

        # 8. Measuring Similarity

        AI systems can compare embedding vectors mathematically.

        One commonly used method is **Cosine Similarity**.

        The formula is:
    
        Cosine Similarity=A⋅B​/
                        ∥A∥∥B∥

        It measures the angle between two vectors.

        Conceptually:

        ```text
        High similarity
                ↓
        Vectors point in similar directions
        ```

        ```text
        Low similarity
                ↓
        Vectors point in different directions
        ```

        Cosine similarity is widely used in semantic search and retrieval systems, although other distance or similarity metrics can also be used.

        ---

        # 9. Embeddings and Vector Databases

        Embedding vectors are often stored in a **vector database**.

        Examples include:

        * Pinecone
        * Qdrant
        * Weaviate
        * Milvus
        * Chroma

        A simplified structure is:

        ```text
        Document A → Embedding Vector
        Document B → Embedding Vector
        Document C → Embedding Vector
        ```

        When a user asks a question:

        ```text
        User Query
            ↓
        Query Embedding
            ↓
        Vector Database
            ↓
        Similarity Search
            ↓
        Most Relevant Documents
        ```

        The retrieved information can then be passed to an LLM.

        ---

        # 10. Embeddings in RAG

        Embeddings are a fundamental component of **RAG (Retrieval-Augmented Generation)** systems.

        Suppose a company has thousands of private documents.

        The system can process them like this:

        ```text
        Company Documents
            ↓
        Chunking
            ↓
        Embedding Model
            ↓
        Document Embeddings
            ↓
        Vector Database
        ```

        When the user asks:

        > **"What is our company's leave policy?"**

        The system performs:

        ```text
        User Question
            ↓
        Query Embedding
            ↓
        Vector Search
            ↓
        Relevant Document Chunks
            ↓
        LLM
            ↓
        Final Answer
        ```

        The embeddings help the system **find the most relevant information** before the LLM generates the answer.

        ---

        # 11. Embeddings Are Not Only for Text

        Embeddings can represent different types of data.

        ### Text Embeddings

        ```text
        "Machine Learning"
                ↓
        Vector
        ```

        ### Image Embeddings

        ```text
        Image
        ↓
        Vector
        ```

        ### Audio Embeddings

        ```text
        Audio
        ↓
        Vector
        ```

        This makes embeddings useful for **multimodal AI systems** as well.

        ---

        # 12. Embeddings in Recommendation Systems

        Embeddings can also represent users and items.

        For example:

        ```text
        User Preferences
            ↓
        User Embedding
        ```

        and:

        ```text
        Movie
        ↓
        Movie Embedding
        ```

        The system can compare these representations to identify items that may be relevant to the user.

        A similar approach can be used for:

        * Movies
        * Music
        * Products
        * Videos
        * Articles
        * Courses

        ---

        # 13. Embeddings in LLMs

        There are two related concepts that should not be confused.

        ### Token Embeddings

        LLMs internally convert tokens into vector representations before processing them through the Transformer.

        ```text
        Token
        ↓
        Token ID
        ↓
        Embedding Vector
        ↓
        Transformer
        ```

        ### Dedicated Embedding Models

        Separate embedding models are designed primarily to generate useful vectors for:

        * Semantic search
        * RAG
        * Retrieval
        * Similarity detection
        * Clustering
        * Recommendation
        * Classification

        Therefore:

        > **Token embeddings help an LLM process language, while dedicated embedding models are commonly used to create vector representations for downstream AI applications.**

        ---

        # 14. Embeddings vs Traditional Keyword Search

        Traditional keyword search looks primarily for matching words.

        For example:

        ```text
        Query:
        "How to learn Python?"
        ```

        A keyword system focuses on terms such as:

        ```text
        learn
        Python
        ```

        An embedding-based search can identify related meaning such as:

        ```text
        "Beginner's guide to Python programming"
        ```

        even when the exact wording is different.

        Therefore:

        > **Keyword search focuses heavily on matching terms, while semantic search using embeddings focuses on similarity in meaning and representation.**

        ---

        # 15. Real-World AI Engineering Example

        Imagine you are building an AI learning assistant.

        You have:

        ```text
        10,000
        PDFs + Notes + Tutorials + Documentation
        ```

        You want students to ask questions about them.

        Your architecture could be:

        ```text
        Documents
        ↓
        Chunking
        ↓
        Embedding Model
        ↓
        Vector Database
        ↓
                ↑
        User Question
                ↓
        Query Embedding
                ↓
        Similarity Search
                ↓
        Relevant Chunks
                ↓
            LLM
                ↓
            Answer
        ```

        Here, embeddings solve the **information retrieval problem**, while the LLM handles **language generation and response construction**.

        ---

        # 16. Important Limitations

        Embeddings are powerful, but they are not perfect.

        Their quality depends on factors such as:

        * The embedding model
        * The quality of the input data
        * Chunking strategy
        * Similarity metric
        * Vector database configuration
        * Query formulation
        * Domain-specific vocabulary

        A poor embedding or poor document chunking strategy can lead to irrelevant retrieval.

        ---

        # 17. Key Applications of Embeddings

        ```text
        Embeddings
        │
        ├── Semantic Search
        ├── RAG
        ├── Vector Databases
        ├── Recommendation Systems
        ├── Similarity Detection
        ├── Duplicate Detection
        ├── Document Retrieval
        ├── Clustering
        ├── Classification
        └── Multimodal Search
        ```

        ---

        # 18. Embeddings — Complete Flow

        The most important flow to remember is:

        ```text
                    DATA
                    ↓
                Embedding Model
                    ↓
                Vector Representation
                    ↓
                Vector Database
                    ↓
            Similarity Search
                    ↓
            Relevant Information
                    ↓
                    LLM
                    ↓
                Final Response
        ```

        ## Final Definition

        > **An embedding is a numerical vector representation of data that captures useful semantic or contextual relationships, allowing AI systems to compare, search, retrieve, organize, and process information mathematically.**

        ### One-line takeaway

        > **Embeddings convert information into vectors so that AI systems can understand relationships and measure similarity mathematically.**
            
        ''')

    if st.session_state.training == True:
        st.write('''

        ''')