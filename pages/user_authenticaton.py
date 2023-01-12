'''
The above code is a part of a Streamlit application that 
handles user registration and login functionality. 
It makes use of the streamlit library for creating UI elements
 and the sqlite3 library for managing a SQLite database to store user data.

The main() function is the main entry point for the registration 
and login feature. It first creates a layout with two columns,
 one for displaying an animation using the st_lottie library and 
 another for the registration and login forms.

The first conditional block inside the function checks if the 
user has already logged in. If not, it displays the login form
 with fields for the username and password. The entered password 
 is hashed using the make_hashes function and the hashed password 
 is used to query the database for a match. If a match is found, 
 the user is considered logged in and the session variables are updated accordingly.

The second conditional block handles user registration. 
The form has fields for the user's name, username, semester,
 mobile number, email and password. The entered username is checked 
 against the existing usernames in the database to ensure it is unique.
  If the passwords entered in the two password fields do not match, 
  an error message is displayed. If the checkbox for "Club Admin" is checked,
   the user is prompted to enter an admin password. If the entered admin password
    matches the one stored in the secrets variable, the user is made an admin.

The last conditional block handles the logout functionality.
 It resets the session variables when the logout button is clicked.

Throughout the code, comments are provided to explain the functionality
 of each section of the code.
'''


import streamlit as st
import pandas as pd
import hashlib
from streamlit_lottie import st_lottie
import json
import requests
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

# DB  Functions


def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(name TEXT,username TEXT,semester TEXT,mobile_no TEXT,admin TEXT,member TEXT,email TEXT,password TEXT)')
# def match():
# 	c.execute('WHERE EXISTS (SELECT username FROM userstable WHERE  username==)')
def add_userdata(name,username,semester,mobile_no,admin,member,email,password):
	c.execute('INSERT INTO userstable(name,username,semester,mobile_no,admin,member,email,password) VALUES (?,?,?,?,?,?,?,?)',(name,username,semester,mobile_no,admin,member,email,password))
	conn.commit()
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def view_all_user_names():
	c.execute('SELECT username FROM userstable')
	data = c.fetchall()
	return data
def view_all_pass():
	c.execute('SELECT password FROM userstable')
	data = c.fetchall()
	return data
def view_all_name():
	c.execute('SELECT name FROM userstable')
	data = c.fetchall()
	return data
def load_lottiefile(filepath:str):
	with open(filepath,'r') as f:
		return json.load(f)
def main(selected):
	if ('password_ad' not in st.session_state):
		st.session_state['password_ad'] = 0

	s1,s2 = st.columns([3,5])
	with s1:
		lotti2 = load_lottiefile("./static/singing-contract.json")
		st_lottie(
		    lotti2,
		    speed = 1,
		    reverse =False,
		    loop =True,
		    quality = "low",
		    height = 400,
		    width = 400,
		    key = None
		)
	
	if selected == "Log in/Log out":
		with s2:
			if st.session_state['ans'] != 1:
				st.subheader("Login Section")
				
				username = st.text_input("User Name")
				password = st.text_input("Password",type='password')
				

				if st.button("Login"):
					create_usertable()
					hashed_pswd = make_hashes(password)

					result = login_user(username,check_hashes(password,hashed_pswd))
					if result:
						

						st.session_state['ans'] = 1

						st.success("Logged In as {}".format(username))
						st.session_state['loggedin_name'] = username

					else:
						st.warning("Incorrect Username/Password Or You are not sign up yet, if yes then do that first")
			
			else:
				st.subheader("Logout Section")
				if st.button("Logout"):
					st.session_state['ans'] = 0
					st.session_state['loggedin_name']=0
					st.session_state["isitadmin"] = 0
					st.info("You are successfully logged out")
				
	
	if selected =="Sign Up":
		with s2:
			if st.session_state['ans'] ==1:
				st.info("You are successfully logged in")
			else:
				st.subheader("Create New Account")
				name = st.text_input("Name")
				new_user = st.text_input("Username")
				semester =st.selectbox("Choose Semester",['I','II' ,'III','IV' ,'V' ,'VI' ])
				mobile_no = st.text_input("Enter Mobile No. ",value="91",max_chars=12)
				new_password = st.text_input("Password",type='password')
				new_password2 = st.text_input("Confirm Password",type='password')
				email = st.text_input("Enter email ")
				Admin = 'No'
				member = 'No'
				if st.checkbox("Club Admin"):
					st.session_state['password_ad'] = st.text_input("Admin Password",type='password')
					if st.secrets['password'] ==st.session_state['password_ad']:
						Admin = 'Yes'
						
				if st.button("Signup"):
					usernames = []
					for user in view_all_user_names():
						usernames.append(user[0])
					if new_user in usernames:
						st.error("Occupied Username,Try with another Username")
					elif new_password != new_password2:
						st.error("Password Not Match")
					elif 4>len(new_password):
						st.error("Weak Password,Try with strong password")
					elif name == None or mobile_no ==None or name == '' or mobile_no =='':
						st.error('Please fill the information')
					
					elif not mobile_no.isdigit() or " " == mobile_no:
						st.error('Invalid mobile number') 
					elif "@gmail.com" not in email or email ==" ":
						st.error('Invalid email id')

					else:
						create_usertable()
						add_userdata(name,new_user,semester,mobile_no,Admin,member,email,make_hashes(new_password))
						st.success(
		"""
		You have successfully created a valid Account,
		Do Login
		""")

