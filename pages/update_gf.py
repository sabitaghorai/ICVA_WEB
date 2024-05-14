import streamlit as st
import mysql.connector

# Title and form description
st.title("Update Exam Questions")
st.write("This form is for updating exam-related information.")

# Input for selecting the exam name to update
exam_name_to_update = st.selectbox("Select the Exam Name to Update", ["Exam 1", "Exam 2","kt", "hou"])  # Provide options based on your data

# Establish a connection to the MySQL database (replace with your own credentials)
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sabita@1234",
        database="google_form"
)

# Create a cursor
cursor = conn.cursor()

# Fetch all questions for the selected exam
cursor.execute("SELECT * FROM exam_data WHERE exam_name = %s", (exam_name_to_update,))
exam_data = cursor.fetchall()

# Initialize lists to store question, options, and correct options
questions = []
options = []
correct_options = []

# Populate the lists with fetched data
for row in exam_data:
    questions.append(row[3])
    options.append([row[4], row[5], row[6], row[7]])
    correct_options.append(row[8])

# Close the connection
conn.close()

# Display all questions for editing
for question_index, question_text in enumerate(questions):
    st.write(f"Editing Question {question_index + 1}:")
    edited_question = st.text_input(f"Edit Question {question_index + 1}", value=question_text)

    st.write("Options:")
    edited_option1 = st.text_input("Edit Option 1", value=options[question_index][0])
    edited_option2 = st.text_input("Edit Option 2", value=options[question_index][1])
    edited_option3 = st.text_input("Edit Option 3", value=options[question_index][2])
    edited_option4 = st.text_input("Edit Option 4", value=options[question_index][3])

    edited_correct_option = st.selectbox(f"Select the correct option for edited Question {question_index + 1}",
                                        ["Option 1", "Option 2", "Option 3", "Option 4"],
                                        index=["Option 1", "Option 2", "Option 3", "Option 4"].index(correct_options[question_index]))

    # Button to save the edited question
    if st.button(f"Save Edited Question {question_index + 1}"):
        # Establish a connection to the MySQL database again
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sabita@1234",
        database="google_form"
        )

        # Create a cursor
        cursor = conn.cursor()

        # Update the corresponding record in the database
        cursor.execute("UPDATE exam_data SET question_text = %s, option1 = %s, option2 = %s, option3 = %s, option4 = %s, correct_option = %s WHERE exam_name = %s AND question_text = %s",
                       (edited_question, edited_option1, edited_option2, edited_option3, edited_option4, edited_correct_option, exam_name_to_update, question_text))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Update the lists with the edited question details
        questions[question_index] = edited_question
        options[question_index] = [edited_option1, edited_option2, edited_option3, edited_option4]
        correct_options[question_index] = edited_correct_option

        # Display a success message
        st.success(f"Question {question_index + 1} has been successfully edited.")
