import streamlit as st
import mysql.connector

# Establish a connection to MySQL Server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sabita@1234",
    database="icvadatabase"
)
cursor = db.cursor()

# Function to add questions to the database
def add_questions(questions):
    sql = "INSERT INTO questionbank (class, subject, question_type, question) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, questions)
    db.commit()

# Streamlit UI
st.title("Question Database")

# Add Question Section
st.header("Add Questions")

class_options = ["6", "7", "8", "9", "10"]
class_name = st.selectbox("Class:", class_options)

subject_options = ["English", "Math", "Life Science", "Physics", "Chemistry"]
subject = st.selectbox("Subject:", subject_options)

question_type = st.selectbox("Question Type:", ["MCQ", "SAQ", "Descriptive"])

questions = []

# Allow user to add multiple questions under different question types
if question_type in ["MCQ", "SAQ", "Descriptive"]:
    st.header(f"Add {question_type} Questions")
    num_questions = st.number_input(f"Number of {question_type} Questions to Add:", min_value=1, value=1)

    for i in range(num_questions):
        st.subheader(f"{question_type} Question {i+1}")
        question_text = st.text_area(f"{question_type} Question Text {i+1} (Supports LaTeX)", height=100, help="You can include LaTeX code here.")
        questions.append((class_name, subject, question_type, question_text))

if st.button("Add Questions"):
    add_questions(questions)
    st.success("Questions added successfully!")
