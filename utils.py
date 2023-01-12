import joblib
import streamlit as st
from learn_control import learn_control 
class utils(learn_control):
    def __init__(self,age:int,streams:int,Internships:int,cgpa:int
                ,HistoryOfBacklogs:int) -> None:
           
        def prediction(x_data) -> bool:
            model = joblib.load("model.joblib")
            if x_data:
                print(x_data)
                y_pred = model.predict_one(x_data) 
                print(learn_control.learn_control_processing(x_data))  
                if 1 == learn_control.learn_control_processing(x_data):
                    model = model.learn_one(x_data, y_pred)
                else:
                    pass
                joblib.dump(model,"model.joblib")
            return y_pred

        def predict()->None:
            x = {'Age': age,'Stream': streams,'Internships': Internships,'CGPA': cgpa,'HistoryOfBacklogs': HistoryOfBacklogs}
            if int(prediction(x)): 
                st.success('Congratulations probably ,You will get placed :thumbsup:')
            else: 
                st.error('Sorry but, Probably you will not get placed :thumbsdown:') 

        if st.button('Predict'):
            if st.session_state['ans'] == 1:
                predict()
            else:
                st.info("For get access the page do sign up / log in first")

class processing(utils):
    def __init__(self,Stream:int,streams:int,cgpa:int,
                Internships:int,age:int,HistoryOfBacklogs:int) -> None:
        for i in streams:
            if Stream ==i:
                streams = streams.index(i)
        HistoryOfBacklogs =int(HistoryOfBacklogs)
        age = int(age)
        Internships = int(Internships)
        cgpa = int(cgpa)
        utils(age,streams,Internships,cgpa,HistoryOfBacklogs)
    

        
