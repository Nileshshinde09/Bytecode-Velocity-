import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
'''
admin_list(c): This function takes a cursor object c as input and returns
 a list of all the users in the database who have the value "Yes" for the 
 "admin" column. The query is executed using the cursor object c and the 
 results are fetched using fetchall().

members_list(c): This function is similar to the admin_list(c) function, 
but it returns a list of all the users in the database who have the value 
"Yes" for the "member" column and "No" for the "admin" column.

streamlit_list(): This function creates an option menu using the option_menu
 function from the streamlit_option_menu library. 
 The menu has two options: "Members List" and "Admin List", 
 and it returns the selected option.

ml(): This function creates the web page with the lists
 of members and admin. It first imports the required libraries
 
  and connects to the database. Then it calls the streamlit_list()
   function to get the selected option. If the selected option is 
   "Admin List", it calls the admin_list(c) function to get the list 
   of admin and displays it in a table using streamlit's st.table() function. 
   If the selected option is "Members List", it calls the members_list(c) 
   function to get the list of members and displays it in a table using 
   streamlit's st.table() function.

This script is used to display the lists of members and admins
 on a web page, it uses a database to get the list of members and
  admins, it uses the streamlit library to display the data on the web page. 
  The script uses the option_menu function from the streamlit_option_menu library
   to create a dropdown menu to switch between the two lists. It also uses the pandas 
   library to create a dataframe to store the data from the database. The script also 
   uses the sqlite3 library to connect to the database.
'''
def admin_list(c):
    admin = "Yes"
    c.execute('SELECT * FROM userstable WHERE admin =?',(admin,))
    data = c.fetchall()
    return data
def members_list(c):
    admin = "No"
    member = 'Yes'
    c.execute('SELECT * FROM userstable WHERE admin =? AND member =?',(admin,member))
    data = c.fetchall()
    return data


def streamlit_list():
    selected = option_menu(
	menu_title=None,  # required
	options=["Members List","Admin List"],  # required
	icons=["member","admin"],  # optional
	menu_icon="cast",  # optional
	default_index=0,
	)
    return selected
def ml():
    import sqlite3 
    conn = sqlite3.connect("data.db", check_same_thread=False)
    c = conn.cursor()
    selected =streamlit_list()
    if selected =="Admin List":
        st.title("Admin List")
        table = admin_list(c)
        df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
        df = df.drop(columns=["member","admin","password"],axis = 1)
        for index,i in enumerate(df['mobile_no']):
            i = str(i)
            df.iloc[index,3] =i[:4]+'XXXXXX'

        st.table(df)

    if selected == "Members List":
        st.title("Members List")
        table = members_list(c)
        members_df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
        members_df = members_df.drop(columns=["member","password"],axis = 1)
        for index,i in enumerate(members_df['mobile_no']):
            i = str(i)
            members_df.iloc[index,3] =i[:4]+'XXXXXX'
        st.table(members_df)

