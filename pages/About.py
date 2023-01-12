import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
import streamlit as st

def about():
    def load_lottiefile(filepath:str):
        with open(filepath,'r') as f:
            return json.load(f)

    s1,s2 = st.columns([1,3])
    with s1:
        lotti3 = load_lottiefile("./static/112023-p-cube-web.json")
        st_lottie(
            lotti3,
            speed = 1,
            reverse =False,
            loop =True,
            quality = "low",
            height = 400,
            width = 400,
            key = None
        )
        

        
        
    with s2:
        st.header('''

        Reason for creation of the club? Why?
        ''')
        st.markdown('''

            To create awareness about programming skills and coding trends amongst the students
        ''')
        st.header('''
            Objectives of the club? What?

        ''')
        st.markdown('''
            1️⃣ To develop logical and abstract thinking, analytical skills and communication skills
            
            2️⃣ To learn basics of coding and programming skills
            
            3️⃣ To learn about trending technologies and tools
            
            4️⃣ To conduct workshops/seminars on trending topics
            
            5️⃣ To develop apps, websites, games, tools etc
            
            6️⃣ To develop team skills through organising, learning and teaching


        ''')
        st.header('''
        Activities/Events? How?
        ''')
        lotti4 = load_lottiefile("./static/42930-objective-communication.json")
        st_lottie(
            lotti4,
            speed = 1,
            reverse =False,
            loop =True,
            quality = "low",
            height = 300,
            width = 300,
            key = None
        )
        st.markdown('''
            🔴Organise training sessions by expert resource persons

            🟡Presentations on trending topics

            🔴Workshops/Seminars on coding skills

            🟡Competitions on coding and analytical skills

            🔴Some domains/topic areas

            🟡Coding languages like Python, C, C++, Ruby on Rails

            🔴Open source movement and tools
        ''')
        lotti5 = load_lottiefile("./static/127673-expo-logic-budget-for-in-person-events-hero.json")
        st_lottie(
            lotti5,
            speed = 1,
            reverse =False,
            loop =True,
            quality = "low",
            height = 300,
            width = 300,
            key = None
        )
        st.markdown('''
            🟡Machine Learning

            🔴Artificial Intelligence

            🟡Internet of Things

            🔴CyberSecurity

            🟡Algorithms

            🔴System Design and Software Design
            
            🟡Approaches to Programming
        ''')