import streamlit as st
from streamlit_option_menu import option_menu
from welcome import welcome  # Import the welcome function
from skinanalyser import skinanalyser  # Import the skinanalyser function
from dermini_feedback import show_dermini_feedback  # Correct import for the feedback function
from chatbot import chatbot
from prescription import presc_analyze
from shop import shop

st.set_page_config(
    page_title="DERMINI", 
    page_icon="🩺", 
    layout="centered", 
    initial_sidebar_state="auto"
)

with st.sidebar:
    selected = option_menu(
        'DERMINI',
        ['Welcome', 'Scan DERMINI', 'Ask DERMINI', 'Medi DERMINI', 
         'Shop DERMINI', 'Contact & Feedback'],
        icons=['house', 'search', 'chat-dots', 'file-earmark-medical', 'box', 'envelope'],
        menu_icon="🩺",
        default_index=0
    )

if selected == 'Welcome':
    welcome()  # Call the welcome function directly

if selected == 'Scan DERMINI':
    skinanalyser()  # Call the skinanalyser function directly

if selected == 'Ask DERMINI':
    chatbot()  # Code to display the chatbot page

if selected == 'Medi DERMINI':
    presc_analyze()  # Code to display the prescription analysis page

if selected == 'Shop DERMINI':
    shop()  # Code to display the skincare shopping page
    
if selected == 'Contact & Feedback':
    show_dermini_feedback()  # Call the feedback function
