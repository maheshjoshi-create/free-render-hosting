import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
# from streamlit_ace import st_ace
# import matplotlib.pyplot as plt


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Mahesh Joshi Resume", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_iv4dsx3q.json")
lottie_summary = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_WvnLdAZwPv.json")
lottie_worklfow_automation_and_orchestration = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_BKm13KMWgV.json")
lottie_hire_me = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_PvqAQh8vzi.json")
lottie_fintech_automation_ml = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_LmW6VioIWc.json")
lottie_nlp_engine_for_unstructure_data = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_kUtZCR7Zyk.json")
lottie_credit_card = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_b5tId6.json")
lottie_facial_recognition = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_qudievat.json")
lottie_Chatbot = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_sqwEc44qxw.json")
img_skills = Image.open("images/Picture4.png")
my_image = Image.open("images/yt_contact_form.png")

# ---- HEADER SECTION ----
#with st.container():
#    left_column, right_column = st.columns(2)
#    with left_column:
#        st.title("Hi, I am Mahesh :wave:")
#        st.subheader("A Data Analyst")
#        st.write(
#            "I am passionate about finding ways to use Python and Data science tools to be more efficient and effective in business settings."
#        )
#        st.write("[Git Hub Repo >](https://github.com/maheshjoshi-create)")
#        
#    with right_column:
#        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
#        # st.image(my_image)

st.title("Hi, I am Mahesh :wave:")
st.subheader("A Data Analyst")
st.write(
    "I am passionate about finding ways to use Python and Data science tools to be more efficient and effective in business settings."
)
st.write("[Download Resume >](https://drive.google.com/file/d/1U2DzVYJN9DenK6O-SEFoPtFhunwMJsdg/view?usp=sharing)")


#------- Who Am I -------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who Am I")
        st.write("##")
        st.write(
            """
            Hi! my name is Mahesh Joshi based in India (🇮🇳), I did a Bachelors in engineering 🎓 from Pune University 🏛 India in 2016, and
            I am a data scientist 💻. Overall, 4+ years of IT experience in developing and delivering projects in several technologies of Artificial Intelligence, Machine Learning, Deep Learning, and Python applications. 
            Expertise in manipulating and analyzing complex, high-volume, high-dimensional data from varying data sources. Good knowledge of Healthcare, Fintech, and Banking domains. 
            I have worked with many companies around the world 🌍. Currently, I work as a senior data analyst at Aress Software Solutions Pvt. Ltd. 📊.
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        # st_lottie(lottie_coding, height=300, key="coding")
        st.markdown("""
                    <style>
                        .name {
                            padding-left: 250px; /* Adjust the value to move the text towards the right */
                        }
                        
                        .name strong {
                            font-weight: bold;
                        }
                    </style>
                """, unsafe_allow_html=True)
    
        st.markdown("""
                    <div class="name">
                        <p><strong> Name -</strong> Mahesh Shridhar Joshi</p>
                        <p><strong>Date Of Birth -</strong> 12 Oct 1993</p>
                        <p><strong>Nationality -</strong> India</p>
                        <p><strong>Email -</strong> maheshjoshi199@gmail.com</p>
                    </div>
                """, unsafe_allow_html=True)


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Have experience working in Iterative Agile Projects- excellent understanding of all phases of the Software Development Life Cycle (SDLC) from project definition to post-deployment. also, 4 years of industry experience as a Data Analyst. Experience in python for data science work. Experience In Machine Learning Application.
            - Technicle Skills: Python, Machine Learning, Artificial Intelligence, Deep Learning.
            - Databases: SQL, Postgress, MySQL, SqlLite, MongoDB.
            - Reporting Tools: Tableau.
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_coding, height=300, key="coding")
        
        
        
# ---- Professional Summary ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("I code Python. Because it is the shortest path from idea to production.")
        st.subheader("🦾I want to became an artificial brain behind everything🧠") 
        # st.write("##")
        st.write(
            """
            - 🔭 I’m currently working on Docker Kubernetes, MlOps and Azure cloud services for the Data Science projects.
            - 🌱 I’m currently working on Transfer Learning + Kubernetes + Data science services on different cloud.
            - 👨‍💻 Have IT experience in developing and delivering projects in several technologies of Artificial Intelligence, Machine Learning, Deep Learning, and Python applications.
            - 📚 Good knowledge of Healthcare, Fintech, and Banking domains.
            - 👯 I’m looking to collaboration on open source Saleforce automation product in Python..
            - 💬 Ask me about anything related to python, R, SQL, Machine learning concepts and projects, Databrics, Docker, etc..
            - ⚡ Fun fact: I watch World Affairs and 2 Minute paper videos a lot....
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        # st_lottie(lottie_summary, height=375, key="coding1")
        # st.subheader("Skills")
        st.image(img_skills)
        
#####################################################################################

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # st.image(img_lottie_animation)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_nlp_engine_for_unstructure_data, height=250, key="coding5")
    with text_column:
        st.subheader("NLP Engine For Unstructure Data (DxT Company)")
        st.write(
            """
            - Responsibilities : 
                - Involved in the development of the NLP engine to scrape the product and quantity for structure and semi-structured file formats. 
                - Involved in the development of the front end as well as writing the API, and Backend. 
                - Involvement in the deployment of the project on Azure with Azure web services. Code-mixed text further complicates the process with it’s unstructured and incomplete information. We propose experiments with different machine learning classification algorithms with word, character and lexical features. The algorithms we experimented with are Decision tree, Long Short-Term Memory (LSTM).
                
            - Technology Used : 
                - Python, NLP, Tesseract, Neural Network, Keras, Spacy, Azure Cloud.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # st.image(img_contact_form)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_fintech_automation_ml, height=250, key="coding4")
    with text_column:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.subheader("Fintech Automation And ML Project (NxC Company)")
        st.write(
            """
            - Responsibilities :
                - Developed automation from scratch starting with writing a Python script to create a containerized solution.
                - Wrote the script to scrap the data from specific email and put that data into Salesforce submission.
                - Wrote the script to consume provided lender’s API with Python scripts. Wrote the test framework in pytest for the project. 
                
            - Technology Used : 
                - Python, Docker, Azure, NLP, PyTest, Selenium, Imap.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(lottie_worklfow_automation_and_orchestration, height=250, key="coding3")
    with text_column:
        # st.markdown('<hr style="border: 1px solid black;">', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.subheader("Workflow Automation And Orchestration (AxxI Company)")
        st.write(
            """
            - Responsibilities :
                - Worked on writing a Python script Which will cosumed API of financial website and prepared a file cotaining missing tickers.
                - Wrote the seperate script to update the recent prices from Bloomberg for missing tickers store them into SQL database.
                - Implemented data orchestration flow using Prefect, Google form and miscorsoft power automate. 
             
            - Technology Used : 
                - Python, SQL, Azure, Git, Prefect, MS Power Automate, BBG Terminal.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")  
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_credit_card, height=250, key="coding6")
    with text_column:
        # st.markdown('<hr style="border: 1px solid black;">', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.subheader("Credit Card Fraud Detection (NxC Company)")
        st.write(
            """
            - Responsibilities :
                - Aim was to detect improper transaction- before/after the events “Detect Pattern”.
                - Used Analytic Technology and techniques + human interaction. 
                - Gathering and storing statistically relevant data and data mining for patterns, anomalies, and discrepancies.
                - Findings are translated into insights, which would allow a company to manage threats and take pre-emptive measures. 
             
            - Technology Used : 
                - Python, MySQL, Machine Learning, Streanlit, Heroku.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")   
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_facial_recognition, height=250, key="coding7")
    with text_column:
        # st.markdown('<hr style="border: 1px solid black;">', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.subheader("Facial Recognition for touchless attendance")
        st.write(
            """
            - Responsibilities :
                - Involved in the development of the backend of the attendance app.
                - Prepared the machine learning model for attendance of employees in python. 
                - Also prepared a classification model for mask detection.
                - Involved in the development of a module that takes the image as input and marks the attendance of the employee on the attendance employee assessment portal. 
             
            - Technology Used : 
                - Python and different deep learning frameworks like Pytorch,Keras, Tensorflow, OpenCV, AWS EC2.
            """
        )
        #st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")   
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st_lottie(lottie_Chatbot, height=300, key="coding8")
    with text_column:
        # st.markdown('<hr style="border: 1px solid black;">', unsafe_allow_html=True)
        # st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.subheader("Developing a Chatbot: Enhancing Customer Support and Engagement")
        st.write(
            """
            - Responsibilities :
                - Aimed at developing an intelligent virtual assistant capable of understanding and responding to user queries.
                - Leveraging natural language processing (NLP) and machine learning techniques, the chatbot provides personalized and accurate responses. 
                - The project involves skills such as conversational AI, NLU model training, dialogue management, and integration with various platforms.
                - Using Rasa we enables the creation of contextual, interactive, and personalized conversational experiences. 
             
            - Technology Used : 
                - Python, Rasa, webchat framework, Rasa-nlu.
            """
        )

########################################################################################
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)

    st.header("Get In Touch With Me!")
    st.write("##")
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/maheshjoshi199@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_hire_me, height=250, key="coding2")
