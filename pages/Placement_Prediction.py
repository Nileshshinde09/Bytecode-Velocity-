from utils import processing,st

class main_(processing):
    def __init__(self) -> None:
        st.title("Will you get placed ?")
        st.error("The prediction made by this app is based on machine learning.")
        st.markdown("[You can see source code here ](https://github.com/Nileshshinde09/student-placement-prediction)")
           # User input to select age
        age = st.slider("Choose age ",14,30)
        
        # User input to select stream
        Stream = st.selectbox("Choose Stream",['Electronics And Communication', 'Computer Science','Information Technology', 'Mechanical', 'Electrical', 'Civil'])
        
        # User input to select number of internships
        Internships = st.slider("Choose Internships",0,3)
        
        # User input to select CGPA
        cgpa = st.slider("Choose CGPA ",5,10)
        
        # User input to select number of Backlogs
        HistoryOfBacklogs = st.select_slider("History Of Backlogs", ['0','1'])
    
        # List of available streams
        streams =['Civil','Computer Science','Electrical','Electronics And Communication','Information Technology','Mechanical']
        
        # calling processing function to process the data and predict placement
        processing(Stream,streams,cgpa,Internships,age,HistoryOfBacklogs)
    

        
