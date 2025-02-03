import streamlit as st
from document_parse import get_file_details
#from get_hr_questions import get_hr_questions
#from get_technical_questions import get_technical_questions
from langchainmemory.technicalmemory import get_technical_questions
from langchainmemory.hrmemory import get_hr_questions
from langchainmemory.user_with_memory import get_user_questions

# Initialize session state variables
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'file_details' not in st.session_state:
    st.session_state.file_details = None
if 'show_hr' not in st.session_state:
    st.session_state.show_hr = False
if 'show_technical' not in st.session_state:
    st.session_state.show_technical = False
if 'job_description' not in st.session_state:
    st.session_state.job_description = None
if 'user_questions' not in st.session_state:
    st.session_state.user_questions = None
if 'show_user' not in st.session_state:
    st.session_state.show_user = False



def show_hr_questions():
    st.session_state.show_hr = True
    st.session_state.show_technical = False
    st.session_state.show_user = False

def show_technical_questions():
    st.session_state.show_hr = False
    st.session_state.show_technical = True
    st.session_state.show_user = False

def show_user_questions():
    st.session_state.show_hr = False
    st.session_state.show_technical = False
    st.session_state.show_user = True

# Title
st.title("Interview Question Generator")

# File uploader
uploaded_file = st.file_uploader("Choose a Resume File")

#Job Description
job_description = st.text_area("Job Description", height=300)
st.session_state.job_description = job_description

#user questions
user_questions = st.text_area("User Questions", height=100)
st.session_state.user_questions = user_questions

if uploaded_file is not None:
    if st.session_state.uploaded_file != uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        with st.spinner('Uploading Resume...'):
            st.session_state.file_details = get_file_details(uploaded_file, uploaded_file.name)
        st.session_state.show_hr = False
        st.session_state.show_technical = False

if st.session_state.uploaded_file is not None:
    st.write("Resume uploaded:", st.session_state.uploaded_file.name)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button('HR Questions', on_click=show_hr_questions)
    with col2:
        st.button('Technical Questions', on_click=show_technical_questions)
    with col3:
        st.button('User Question', on_click=show_user_questions)

    if st.session_state.show_hr:
        #st.write("HR Interview Questions:-")
        # Add your HR questions logic here
        input_question = "Provide me HR questions on this resume in relation with job description."
        with st.spinner('Generating HR questions...'):
            hr_questions = get_hr_questions(st.session_state.file_details, st.session_state.job_description, input_question)
            st.write(hr_questions)
        
    if st.session_state.show_technical:
        #st.write("Technical Interview Questions")
        # Add your technical questions logic here
        input_question = "Provide me Technical questions on this resume in relation with job description."
        with st.spinner('Generating Technical questions...'):
            technical_questions = get_technical_questions(st.session_state.file_details, st.session_state.job_description, input_question)
            st.write(technical_questions)

    if st.session_state.show_user:
        st.write(st.session_state.user_questions)
        with st.spinner('Generating User questions...'):
            answer = get_user_questions(st.session_state.file_details, st.session_state.job_description, st.session_state.user_questions)
            st.write(answer)