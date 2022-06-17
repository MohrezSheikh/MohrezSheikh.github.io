import streamlit as st

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Mohammad Reza Sheikh
##### *Resume* 
''')



st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I'm a Machine Learning Engineer who loves to work with Data and Machine Learning algorithms. I created some projects in Machine Learning and have the experience to deploy some projects on the backend side with Python (Flask) and work with databases (Sqlite). I am skilled in Python, Machine Learning, Deep Learning Algorithms, Linux, SQL, and Web Development. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Mohammad Reza Sheikh</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#machine-learning-projects">Machine Learning Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certificates">Certificates</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Computer Software Engineering** (Artificial Intelligence), *Islamic Azad University Tehran North Branch*, Tehran, Iran',
'2018-2022')
st.markdown('''
- GPA: `16.40/20 - 3.20/4`
- Relevant Coursework: `18.46/20 - 3.92/4`: Computer Vision, Natrual Language Processing, Network, Signal and Systems, Internet Engineering, Artificial Intelligence, Software Engineering, Data Structure, Engineering Mathematics, Algorithm Design, Automata theory, System Digital, Research and presentation methods.
- Thesis `Fully functional web app using Pre-Trained Transformer models for Sentiment Analysis and Text Summarization`
- Member of the University Artificial Intelligence Association
- `TOEFL:100  GRE:320`
''')

#####################
st.markdown('''
## Research Interests
''')
st.markdown('''
- Natural Language Processing
- Computer Vision
- Transformers
''')




#####################
st.markdown('''
## Work Experience
''')

txt('**Founder, Giftak(Startup)**, Gaming Services',
'2020-2021')
st.markdown('''
- Managing gaming product services. 
- Managing developer and designer teams.
''')

txt('**Python Developer, Giftak(Startup)**, Gaming Services',
'2020-2021')
st.markdown('''
- Create and develop the website using Flask and SQLite. 
''')

txt('**Machine Learning Engineer Intern, Arian Neural Network**,',
'2021 for 3 months')
st.markdown('''
- Work with some Machine Learning and Deep Learning models and working with data. 
''')

txt('**Machine Learning Engineer, Arian Neural Network**,',
'2021-2022')
st.markdown('''
- Work with some Machine Learning and Deep Learning models and working with data. 
''')

txt('**Technical Writer**, [Mohrez](https://medium.com/@Mohrez) on Medium.com',
'2022-Present')
st.markdown('''
- Wrote 2 article. 
''')


#####################
st.markdown('''
## Machine Learning Projects
''')
txt4('Transformers', 'Using Siebert Sentiment-Roberta-Large-English model for Sentiment Analysis and Facebook/Bart-Large-CNN for Text Summarization', 'https://github.com/MohrezSheikh/A-Dynamic-Web-App-Using-Pre-trained-Transformer-Models-for-Sentiment-Analysis-and-Text-Summarization')
txt4('SMS Spam Classifier', 'Use BOW and Naive Bayes model for Spam Classifier', 'https://github.com/MohrezSheikh/SMS-Spam-Classifier')
txt4('Stock Price Movement', 'Use BOW and Random Forest Classifier','https://github.com/MohrezSheikh/Stock-Price-Movement-Using-NLP')
txt4('PhD Seeker Bot', 'Create a telegram bot to find PhD positions', 'https://github.com/MohrezSheikh/PhD-seeker-telegram-bot')
txt4('Dataset', 'Scrape all of the Elon Musk Tweets','https://github.com/MohrezSheikh/Elon-Musk-Tweets')


#####################
st.markdown('''
## Certificates
''')
txt3('Machine Learning(Stanford University)', 'https://www.coursera.org/account/accomplishments/certificate/QW5UH7MPC74W')
txt3('Machine Learning A-Z™: Hands-On Python & R In Data Science(Udemy)', 'https://www.udemy.com/certificate/UC-dcb8d9c9-8d08-4202-9623-2e6cade036c1/')
txt3('Machine Learning(Part AI Research Center)', 'https://partdp.ai/')
txt3('SQL - MySQL for Data Analytics and Business Intelligence(Udemy)', 'https://www.udemy.com/certificate/UC-a31f0cd7-09c4-459e-a90a-22486fee30bf/')
txt3('Machine Learning, Deep Learning(Udemy)', 'https://www.udemy.com/certificate/UC-fd83bde5-aba7-4684-abf6-9c018ebd6c6c/')
txt3('Intro to Machine Learning(Kaggle)', 'https://www.kaggle.com/learn/certification/mmdation/intro-to-machine-learning')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Matlab`, `C++`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `PyTorch`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/mohammad-reza-sheikh-553095168/')
txt2('GitHub', 'https://github.com/MohrezSheikh')
txt2('Medium', 'https://medium.com/@Mohrez')
txt2('Stackoverflow', 'https://stackoverflow.com/users/14403063/mohrez')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Mohammad-Sheikh-15')
