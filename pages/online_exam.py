import streamlit as st
import mysql.connector

# Title
st.title("Exam Questions")

# Input for student's name
student_name = st.text_input("Enter Your Name")

# Input for selecting the exam name to display questions
exam_name_to_display = st.selectbox("Select the Exam Name to Display Questions", ["Exam 1", "Exam 2", "kt", "Exam 3"])  # Provide options based on your data

# Establish a connection to the MySQL database (replace with your own credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sabita@1234",
    database="google_form"
)

# Create a cursor
cursor = conn.cursor()

# Check if a submission for the same student and exam already exists
cursor.execute("SELECT * FROM student_result WHERE student_name = %s AND exam_name = %s", (student_name, exam_name_to_display))
existing_submission = cursor.fetchone()

if existing_submission:
    st.warning("You have already submitted this exam. Your submission has been recorded.")
else:
    # Fetch all questions for the selected exam
    cursor.execute("SELECT * FROM exam_data WHERE exam_name = %s", (exam_name_to_display,))
    exam_data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Initialize a variable to keep track of the user's total marks
    total_marks = 0

    # Initialize a list to store whether each question is correct or not
    correct_answers = []

    # Initialize a dictionary to store the selected options
    selected_options = {}

    # Display questions and options with radio buttons for selection
    for question_index, row in enumerate(exam_data):
        question_number = question_index + 1  # Convert to 1-based indexing

        st.write(f"Question {question_number}: {row[3]}")

        # Create radio buttons for options
        selected_option = st.radio(f"Select an option for Question {question_number}", [row[4], row[5], row[6], row[7]])

        # Store the selected option in the dictionary
        selected_options[question_number] = selected_option

    # Submit button to calculate total marks
    if st.button("Submit"):
        for question_number, row in enumerate(exam_data, start=1):
            # Check if the selected option is correct
            if selected_options[question_number] == row[7]:
                total_marks += 4
                correct_answers.append(True)
            else:
                correct_answers.append(False)

        # # Display the total marks after the user clicks the submit button
        # st.write(f"Total Marks: {total_marks} out of {4 * len(exam_data)}")

        # # Display a list of correct/incorrect answers
        # st.write("Correct Answers:")
        # for i, is_correct in enumerate(correct_answers, start=1):
        #     st.write(f"Question {i}: {'Correct' if is_correct else 'Incorrect'}")

        # Establish a new connection to store student results in the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sabita@1234",
            database="google_form"
        )

        # Create a cursor
        cursor = conn.cursor()

        # Check if a submission for the same student and exam already exists again (to handle concurrent submissions)
        cursor.execute("SELECT * FROM student_result WHERE student_name = %s AND exam_name = %s", (student_name, exam_name_to_display))
        existing_submission = cursor.fetchone()

        if not existing_submission:
            # Insert student results into the student_result table
            cursor.execute("INSERT INTO student_result (student_name, exam_name, total_marks) VALUES (%s, %s, %s)",
                           (student_name, exam_name_to_display, total_marks))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
