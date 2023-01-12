'''
This is the main python script that runs the application. 
It starts by importing all the necessary modules and functions from 
different files. Then it uses the Streamlit library to create a user interface.

It first sets the page configuration using st.set_page_config() 
which sets the page title, icon, layout, initial sidebar state, 
and menu items. Then it uses st.markdown() to hide the menu and the sidebar.

It then initializes some variables in the session state using st.session_state,
 such as loggedin_name, username_login, isitadmin, ans, and year. 
 These variables will be used throughout the application to keep 
 track of the user's login status, username, admin status, and current year.

It then defines three functions streamlit_menu1(), streamlit_menu2() 
and streamlit_user() that create a Streamlit option menu. These functions
 return the selected option from the menu. streamlit_menu1() is used for 
 the initial menu and streamlit_menu2() and streamlit_user() is used for the sub-menus.

After that, it checks if the user is logged in or not. If the user is logged in,
 it displays a welcome message with the user's name. If the user is not
  logged in, it does nothing.

Finally, it uses a try-except block to handle the selected option from the 
menu and call the corresponding function. For example, if the user selects
 "Sign Up" or "Log in/Log out" from the menu, it calls the main() function 
 which handles the user authentication. If the user selects "Home", 
 it calls the main_method() function which is the main page of the 
 application. Similarly, if the user selects "About", it calls the about() 
 function, and so on.
'''
from question import question
from snippet import snippet
import streamlit as st
from streamlit_option_menu import option_menu
from pages.About import about
from pages.Members_List import ml
from pages.Table_Operations import table_main
from pages.main_page import main_method
from pages.user_authenticaton import main
import pages.Placement_Prediction
from pages.ai import ai
if __name__=="__main__":

    st.set_page_config(
        page_title="Bytecode Velocity",
        page_icon="📚",
            layout="wide",
            initial_sidebar_state="collapsed",
            menu_items={
                'Get Help': 'https://www.extremelycoolapp.com/help',
                'Report a bug': "https://www.extremelycoolapp.com/bug",
                'About': "# This is a header. This is an *extremely* cool app!"}
    )
    hide_menu_style ="""
            <style>
             #MainMenu {visibility: hidden;}
             </style>
             """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
    no_sidebar_style = """
    <style>
        div[data-testid="collapsedControl"] {display: none;}
    </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)
    if ('loggedin_name' not in st.session_state):
        st.session_state['loggedin_name'] = 0
    def streamlit_menu1():
        selected = option_menu(
        menu_title=None,  # required
        options=["Log in/Log out","Sign Up","Home", "Members List","Table Operations","Placement Prediction","ai","About","Exit"],  # required
        icons=["login","sign up","house", "list", "table operations","prediction","ai", "about","exit"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        )
        return selected
    def streamlit_menu2():
        selected = option_menu(
        menu_title=None,  # required
        options=["Sign Up","Login/Logout","Home", "Members List","ai","About","Exit"],  # required
        icons=["sign up","login","house", "list","ai", "about","exit"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
        )
        return selected

    def streamlit_user():
        selected = option_menu(
		menu_title=None,  # required
		options=["Sign Up","Login"],  # required
		icons=["sign up","login"],  # optional
		menu_icon="cast",  # optional
		default_index=0,  # optional
		orientation="horizontal",
		)
        return selected
    if ('username_login' not in st.session_state):
        st.session_state['username_login'] = 0
    if ('isitadmin' not in st.session_state):
        st.session_state['isitadmin'] = 0
    if ('ans' not in st.session_state):
        st.session_state['ans'] = 0
    if st.session_state['loggedin_name'] != 0:

        if st.session_state['isitadmin'] == 1:
            st.header(f"Admin :")
        st.header(f"Welcome {st.session_state['loggedin_name']}")

    else:
        pass

    if ('year' not in st.session_state):
        st.session_state['year'] = 'I'
    selected =streamlit_menu1()
    try:
        if selected == "Sign Up" or selected == "Log in/Log out":
            try:
                main(selected)           
            except Exception :
                pass

        if selected == "Home":
            try:
                
                main_method()
            except Exception :
                pass
        if selected == "About":
            about()
        if selected == "Members List":
            ml()
            pass
        if selected =="Placement Prediction":
            a = pages.Placement_Prediction.main_()
            pass
        if selected == "Table Operations":
            try:
                table_main()
                pass
            except Exception :
                pass  
        if selected =='ai':
            ai()  
        if selected =="Exit":
            # st.markdown("""
            #     <meta http-equiv="refresh" content="0; url='https://www.google.com'" />
            #     """, unsafe_allow_html=True
            # )
            st.info("Function will coming soon")
    except Exception:
        pass



