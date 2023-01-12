'''
This is a Python script that uses the Streamlit library to create a web 
application that allows users to solve coding questions and submit them 
for evaluation. The script also uses the Streamlit_ace library to create a 
code editor and display the output of the user's code. The script connects to 
a SQLite database "data.db" to fetch user's information and update the information 
in the database.

The script defines a class "main_method" that has a constructor and several
 methods. The constructor sets up the initial state of the application, 
 such as fetching user data from the database and setting the year of the user.

The "run(code,year)" method takes the user's code and the year of the user
 as input, and evaluates the code. It redirects the output of the code 
 to a text file, depending on the year of the user. The "submit(year,code)" method compares the output of the code to the expected output, and returns 1 if they match.

The script also has a method "mlist(username)" which sets the user as a 
member of the coders club if the user solves the question correctly.

The script uses Streamlit's st.session_state to store the state of the 
application, such as whether the user is logged in or not, the name of the 
logged-in user, and the year of the user. The script also uses Streamlit's st.header, st.columns, st.markdown, st.error, and st.success functions to display the question, code editor, output, and messages to the user.
'''

from question import question
from snippet import snippet
import streamlit as st
from streamlit_ace import st_ace
import sys
from csv import writer
import sqlite3 

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

def getdata(username):
    c.execute('SELECT * FROM userstable WHERE username =?',(username,))
    data = c.fetchall()
    return data
def mlist(username):
    member = "Yes"
    c.execute("UPDATE userstable SET member =?  WHERE username=?",(member,username))
    conn.commit()
class main_method:
    def __init__(self) -> None:
        
        def run(code,year):
            code_part = code
            try:
                if year =='1':
                    inputfile = './static/file_first.txt'
                elif year =='2':
                    inputfile = './static/file_second.txt'
                else :
                    inputfile = './static/file_third.txt'
                orig_stdout = sys.stdout
                sys.stdout = open(inputfile, 'w')
                exec(code_part)
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = open(inputfile, 'r').read()
            except Exception as e:
                sys.stdout.close()
                sys.stdout=orig_stdout
                output = e
            return output
        def submit(year,code):

            if year =='1':
                inputfile = './static/file_first_temp.txt'
            elif year =='2':
                inputfile = './static/file_second_temp.txt'
            else :
                inputfile = './static/file_third_temp.txt'
            output = open(inputfile, 'r').read()
            if output ==run(code,year):
                return 1
        
        
        if st.session_state['ans'] ==0:
            data = ["non","I","I"]
        else:
            data = list(getdata(username=st.session_state['loggedin_name'])[0])
            st.session_state['year'] = data[2]

        if 'I' ==st.session_state['year'] or 'II' ==st.session_state['year']:
            year = '1'
        elif 'III' ==st.session_state['year'] or 'IV' ==st.session_state['year']:
            year = '2'
        else:
            year = '3'
        st.header("Solve question and submit, if the answer is right then you will be the part of coders club.")
        st.header('Question :')
        question(year)
        first,second= st.columns([6, 2])
        with first:
            st.markdown("## Code Editor")
            code = st_ace(value=(snippet(year)),
            language = 'python',
            theme='xcode')

        if st.button('run'):
            if 1 !=st.session_state['ans']:
                st.error('Please do Sign up/log in first')
    
            else:
                with second:
                    st.markdown("## Output")
                    st_ace(value =run(code,year) ,
                    language = 'python',
                    theme = 'pastel_on_dark',
                    readonly  = True)
        else:
            with second:
                st.markdown("## Output")
                st_ace(value ='' ,
                language = 'python',
                theme = 'pastel_on_dark',
                readonly  = True)
        if st.button('Submit'):
            if 1 !=st.session_state['ans']:
                st.error('Please do Sign up/log in first')
            elif submit(year):
                
                st.success('Congratulations you did it 🏆🥇')
            else:
                st.error('Better luck next time :thumbsdown:') 

'''
This script is defining a class main_method which has several 
methods to display a question, a code editor, and a submit button 
in a Streamlit app. The __init__ method of the class is being called 
when the class is created, and it sets up the layout and functionality of the app.

The run method takes in two parameters, code and year, and runs the code
 with the help of sys library to redirect the output to a file. Then it 
 reads the output from the file and returns it.

The submit method takes in two parameters, year and code, and compares the
 output generated by the run method with the output stored in a file. 
 If they match, it returns 1, otherwise, it returns nothing.

The __init__ method first checks if the user is logged in and gets the
 data of the user from the database. Then it sets the year based on the
  user's data and displays the question using the question method. 
  It also creates a code editor using the st_ace method and a submit button.

If the user clicks the "run" button, the code is run and the output is
 displayed in a separate column. If the user clicks the "Submit" button,
  the output of the code is compared with the output stored in the file and
   if they match, the user is congratulated, otherwise, the user is asked to 
   try again next time.


'''
