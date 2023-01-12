'''
This code defines several functions that interact with a SQLite 
database to manage user data.

The view_all_users function retrieves all data from the 
'userstable' table.

The view_all_user_names function retrieves all usernames
 from the 'userstable' table.

The remove_users function deletes a user with a given 
username from the 'userstable' table.

The admin_list and members_list functions retrieve data for admin and 
member users respectively.
The signup_list function retrieves data for users who have not
 yet been made members.
 
The getdata function retrieves data for a user with a given username.

The showtable function displays the data retrieved by the 
view_all_users function in a table.

The loadtable function retrieves data from the 'userstable' 
table and returns it as a DataFrame.

The streamlit_list function creates a dropdown menu to allow 
the user to select between different types of lists.

The mlist and mdelist functions toggle the 'member' status of a 
user with a given username.

The table_main function controls the display of different lists of 
users based on the user's status and selection from the dropdown menu.

'''
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import csv
import sqlite3 
conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

def view_all_users(c):
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_all_user_names():
    c.execute('SELECT username FROM userstable')
    data = c.fetchall()
    return data

def remove_users(username):
    c.execute("DELETE FROM userstable WHERE username=?",(username,))
    conn.commit()
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

def signup_list(c):
    admin = "No"
    member = 'No'
    c.execute('SELECT * FROM userstable WHERE admin =? AND member =?',(admin,member))
    data = c.fetchall()
    return data

def getdata(username):
    c.execute('SELECT * FROM userstable WHERE username =?',(username,))
    data = c.fetchall()
    return data

def showtable():
    table = view_all_users(c)
    df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
    df = df.iloc[:,:-1]
    st.table(df)
    if ('table_len' not in st.session_state):
	    st.session_state['table_len'] = len(df)-1

def loadtable():
    table = view_all_users(c)
    df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
    return df

def streamlit_list():
    selected = option_menu(
	menu_title=None,  # required
	options=["Logged in Students","Members List","Admin List"],  # required
	icons=["","member","admin"],  # optional
	menu_icon="cast",  # optional
	default_index=0,
	)
    return selected

def mlist(username):
    member = "Yes"
    c.execute("UPDATE userstable SET member =?  WHERE username=?",(member,username))
    conn.commit()

def mdelist(username):
    member = "No"
    c.execute("UPDATE userstable SET member =?  WHERE username=?",(member,username))
    conn.commit()


def table_main():

    try:
        if  0==st.session_state['loggedin_name']: 
            st.info("For get access the page do sign up / log in first")
        else:
            username=st.session_state['loggedin_name']
            data = list(getdata(username)[0])
            if "Yes" ==data[4]:
                st.session_state['isitadmin'] = 1
                selected =streamlit_list()
                if selected =="Logged in Students":
                    
                    st.title("Logged in Students")
                    table = signup_list(c)
                    Logged_df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
                    Logged_df = Logged_df.drop(columns=["member","password"],axis = 1)
                    if st.button("Update"):
                        st.table(Logged_df)
                    else:
                        st.table(Logged_df)
                if selected =="Admin List":
                    st.title("Admin List")
                    table = admin_list(c)
                    df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
                    df = df.drop(columns=["member","admin","password"],axis = 1)
                    if st.button("Update"):
                        st.table(df)
                    else:
                        st.table(df)

                if selected == "Members List":
                    st.title("Members List")
                    table = members_list(c)
                    members_df = pd.DataFrame(table,columns=["name","username","semester","mobile_no","admin","member","email","password"])
                    members_df = members_df.drop(columns=["member","password"],axis = 1)
                    if st.button("Update"):
                        st.table(members_df)
                    else:
                        st.table(members_df)


            
                username_i=st.text_input("Enter the index of the username you wish to remove from list:")
                if st.button('Remove'):
                    try:
                        usernames = []
                        for user in view_all_user_names():
                            usernames.append(user[0])
                        if username_i in usernames or username_i !="nilesh":
                            remove_users(username_i)
                            st.info("Member successfully removed")
                        else:
                            st.error("UserName is Not in list")
                    except Exception:
                        pass
                st.header("Add Member")
                if st.button("Add Member"):
                    username = st.text_input("Enter the username you wish to add in the list:")
                    if username in usernames or username !="nilesh":
                        mlist(username)
                        st.info("Member successfully added")
                    else:
                        st.error("UserName is Not in list")

                username = st.text_input("Enter the username you wish to delist from members list:")
                if st.button("delist"):
                    if username in usernames or username !="nilesh":
                        mdelist(username)
                        st.info("Member successfully delisted")
                    else:
                        st.error("UserName is Not in list")
                    
                st.header('Download Member List')
                df =loadtable()
                csvfile = df.to_csv()
                st.download_button('Download', csvfile)

            else:
                st.info(
            """
            You can't access this page, Login As Admin
            """)
    except Exception as e:
        st.error(e)




