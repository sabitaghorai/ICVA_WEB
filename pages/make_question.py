import streamlit as st
import mysql.connector


# Title and form description
st.title("Exam Question Collection and Correct Option Selection Form")
st.write("This form is for collecting exam-related information.")

# Input for the exam name
exam_name = st.text_input("Enter the Exam Name")

# Input for the number of questions
num_questions = st.number_input("How many questions do you want to add?", min_value=1, value=1)

# Initialize lists to store question, options, and correct options
questions = []
options = []
correct_options = []

# Loop to collect information for each question
for i in range(num_questions):
    st.write(f"Question {i + 1}:")
    question = st.text_input(f"Enter Question {i + 1}", key=f"question_{i}")
    questions.append(question)

    st.write("Options:")
    option1 = st.text_input("Option 1", key=f"option1_{i}")
    option2 = st.text_input("Option 2", key=f"option2_{i}")
    option3 = st.text_input("Option 3", key=f"option3_{i}")
    option4 = st.text_input("Option 4", key=f"option4_{i}")
    options.append([option1, option2, option3, option4])

    correct_option = st.selectbox(f"Select the correct option for Question {i + 1}", ["Option 1", "Option 2", "Option 3", "Option 4"], key=f"correct_option_{i}")
    correct_options.append(correct_option)

# Submit button
if st.button("Submit"):
    # Establish a connection to the MySQL database (replace with your own credentials)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sabita@1234",
        database="google_form"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Insert data into the database
    for i in range(num_questions):
        cursor.execute("INSERT INTO exam_data (exam_name, question_number, question_text, option1, option2, option3, option4, correct_option) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (exam_name, i+1, questions[i], options[i][0], options[i][1], options[i][2], options[i][3], correct_options[i]))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Display a success message
    st.success("Data has been successfully stored in the database.")
