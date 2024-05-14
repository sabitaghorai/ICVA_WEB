import mysql.connector
import streamlit as st
import pandas as pd

# Establish a connection to MySQL Server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sabita@1234",
    database="icvadatabase"
)

# Streamlit app


# # Function to fetch and display table data
# def view_table(table_name):
#     try:
#         query = f"SELECT * FROM {table_name};"
#         df = pd.read_sql(query, con=mydb)
#         st.write(f"Displaying data from the {table_name} table:")
#         st.dataframe(df)
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

# # List of tables in the database
# tables = ['Language', 'Subjects', 'Classes', 'Exams', 'Organizations', 'Experts',
#           'Questions', 'Answers', 'ExamPaper', 'MCQPaperSet', 'PaperSet', 'Country',
#           'State', 'District', 'Subdivision', 'Students', 'Courses']

# # Select a table to view
# selected_table = st.selectbox('Select a table to view:', tables)

# # View the selected table
# view_table(selected_table)






mycursor = mydb.cursor()


# Streamlit app title
st.title("Database Interaction App")

# # Select the table to interact with
# selected_table = st.selectbox("Select a table:", ("Language", "Subjects","Classes","Exams","Organizations",'Experts',
#           'Questions', 'Answers', 'ExamPaper', 'MCQPaperSet', 'PaperSet', 'Country',
#           'State', 'District', 'Subdivision', 'Students', 'Courses'))  # Add more table names if needed

# Function to insert data into the Language table
def insert_language_data():
    st.header("Insert Data into Language Table")
    name = st.selectbox("Name", ("ENGLISH", "BENGALI", "HINDI"), key="language_name_selectbox")
    short_name = st.selectbox("Short Name", ("ENG", "BEN", "HIN"), key="language_short_name_selectbox")

    if st.button("Insert"):
        insert_query = "INSERT INTO Language (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Language data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Language table
# def display_language_table():
#     st.header("Language Table")
#     mycursor.execute("SELECT * FROM Language")
#     data = mycursor.fetchall()
#     st.write(data)
    
    

# Function to insert data into the Subjects table
def insert_subject_data():
    st.header("Insert Data into Subjects Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Subjects (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Subject data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Subjects table
# def display_subjects_table():
#     st.header("Subjects Table")
#     mycursor.execute("SELECT * FROM Subjects")
#     data = mycursor.fetchall()
#     st.write(data)
    
    

# Function to insert data into the Classes table
def insert_class_data():
    st.header("Insert Data into Classes Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Classes (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Class data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Classes table
# def display_classes_table():
#     st.header("Classes Table")
#     mycursor.execute("SELECT * FROM Classes")
#     data = mycursor.fetchall()
#     st.write(data)
    
    
# Function to insert data into the Exams table
def insert_exam_data():
    st.header("Insert Data into Exams Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Exams (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Exam data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Exams table
# def display_exams_table():
#     st.header("Exams Table")
#     mycursor.execute("SELECT * FROM Exams")
#     data = mycursor.fetchall()
#     st.write(data)
    

# Function to insert data into the Organizations table
def insert_organization_data():
    st.header("Insert Data into Organizations Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")
    org_type = st.selectbox("Type", ("Govt", "Private", "Govt Aided", "NGO", "Govt Under Taken", "Public"))
    address = st.text_area("Address")

    if st.button("Insert"):
        insert_query = "INSERT INTO Organizations (Name, ShortName, Type, Address) VALUES (%s, %s, %s, %s)"
        values = (name, short_name, org_type, address)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Organization data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Organizations table
# def display_organizations_table():
#     st.header("Organizations Table")
#     mycursor.execute("SELECT * FROM Organizations")
#     data = mycursor.fetchall()
#     st.write(data)
    
# Function to insert data into the Experts table
def insert_expert_data():
    name = st.text_input("Name")
    col1, col2 = st.columns(2)

    # Define input fields
    with col1:
    
        communication_details = st.text_area("Communication Details")

    with col2:

        qualification = st.text_area("Qualification")
        
        
    #short_name = st.text_input("Short Name")
    #organization_id = st.number_input("Organization ID", min_value=1)
    permanent_address = st.text_area("Permanent Address")

    col1, col2, col3 = st.columns(3)

    # Define input fields
    with col1:
        designation = st.text_input("Designation", value="TEACHER")

    with col2:
        experience = st.text_area("Experience")

    with col3:
        joining_date = st.date_input("Joining Date")

    if st.button("Insert"):
        insert_query = "INSERT INTO Experts (Name,  ParmanentAddress, CommunicationAddress, Qualification, Designation, Experience, JoiningDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, permanent_address, communication_details, qualification, designation, experience, joining_date)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Expert data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Experts table
# def display_experts_table():
#     st.header("Experts Table")
#     mycursor.execute("SELECT * FROM Experts")
#     data = mycursor.fetchall()
#     st.write(data)
    
# Function to insert data into the Questions table
def insert_question_data():
    st.header("Insert Data into Questions Table")
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    que_beng_text = st.text_area("Bengali Text")
    que_eng_text = st.text_area("English Text")

    if st.button("Insert"):
        insert_query = "INSERT INTO Questions (ExprtID, QueBengText, QueEngText) VALUES (%s, %s, %s)"
        values = (expert_id, que_beng_text, que_eng_text)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Question data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Questions table
# def display_questions_table():
#     st.header("Questions Table")
#     mycursor.execute("SELECT * FROM Questions")
#     data = mycursor.fetchall()
#     st.write(data)


# Function to insert data into the Answers table
def insert_answer_data():
    st.header("Insert Data into Answers Table")
    ques_id = st.number_input("Question ID", min_value=1, step=1)
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    ans_beng_text = st.text_area("Bengali Text")
    ans_eng_text = st.text_area("English Text")

    if st.button("Insert"):
        insert_query = "INSERT INTO Answers (QuesID, ExprtID, AnsBengText, AnsEngText) VALUES (%s, %s, %s, %s)"
        values = (ques_id, expert_id, ans_beng_text, ans_eng_text)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Answer data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Answers table
# def display_answers_table():
#     st.header("Answers Table")
#     mycursor.execute("SELECT * FROM Answers")
#     data = mycursor.fetchall()
#     st.write(data)
    
# Function to insert data into the ExamPaper table
def insert_exam_paper_data():
    st.header("Insert Data into ExamPaper Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")
    exam_id = st.number_input("Exam ID", min_value=1, step=1)
    class_id = st.number_input("Class ID", min_value=1, step=1)
    subj_id = st.number_input("Subject ID", min_value=1, step=1)
    expert_id = st.number_input("Expert ID", min_value=1, step=1)
    full_marks = st.number_input("Full Marks", min_value=0, step=1)

    if st.button("Insert"):
        insert_query = "INSERT INTO ExamPaper (Name, ShortName, ExamID, ClassID, SubjID, ExprtID, FullMarks) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, short_name, exam_id, class_id, subj_id, expert_id, full_marks)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("ExamPaper data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the ExamPaper table
# def display_exam_paper_table():
#     st.header("ExamPaper Table")
#     mycursor.execute("SELECT * FROM ExamPaper")
#     data = mycursor.fetchall()
#     st.write(data)
    
# Function to insert data into the MCQPaperSet table
# # Function to display the MCQPaperSet table
# def display_mcq_table():
#     st.header("MCQPaperSet Table")
#     mycursor.execute("SELECT * FROM MCQPaperSet")
#     data = mycursor.fetchall()
#     st.write(data)
    

# Function to insert data into the PaperSet table
def insert_paper_set_data():
    st.header("Insert Data into PaperSet Table")
    ques_id = st.number_input("Question ID", min_value=1, step=1)
    exam_paper_id = st.number_input("Exam Paper ID", min_value=1, step=1)
    lang_id = st.number_input("Language ID", min_value=1, step=1)
    marks = st.number_input("Marks", min_value=0, step=1)
    harder_rank = st.number_input("Harder Rank", min_value=0, max_value=9, step=1)

    if st.button("Insert"):
        insert_query = "INSERT INTO PaperSet (QuesID, ExamPaperID, LangID, Marks, HarderRank) VALUES (%s, %s, %s, %s, %s)"
        values = (ques_id, exam_paper_id, lang_id, marks, harder_rank)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("PaperSet data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the PaperSet table
# def display_paper_set_table():
#     st.header("PaperSet Table")
#     mycursor.execute("SELECT * FROM PaperSet")
#     data = mycursor.fetchall()
#     st.write(data)        


# Function to insert data into the Country table
def insert_country_data():
    st.header("Insert Data into Country Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Country (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Country data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Country table
# def display_country_table():
#     st.header("Country Table")
#     mycursor.execute("SELECT * FROM Country")
#     data = mycursor.fetchall()
#     st.write(data)
        
# Function to insert data into the State table
def insert_state_data():
    st.header("Insert Data into State Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO State (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("State data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the State table
# def display_state_table():
#     st.header("State Table")
#     mycursor.execute("SELECT * FROM State")
#     data = mycursor.fetchall()
#     st.write(data)
            
# Function to insert data into the District table
def insert_district_data():
    st.header("Insert Data into District Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO District (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("District data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the District table
# def display_district_table():
#     st.header("District Table")
#     mycursor.execute("SELECT * FROM District")
#     data = mycursor.fetchall()
#     st.write(data)
    
    
# Function to insert data into the Subdivision table
def insert_subdivision_data():
    st.header("Insert Data into Subdivision Table")
    name = st.text_input("Name")
    short_name = st.text_input("Short Name")

    if st.button("Insert"):
        insert_query = "INSERT INTO Subdivision (Name, ShortName) VALUES (%s, %s)"
        values = (name, short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Subdivision data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Subdivision table
# def display_subdivision_table():
#     st.header("Subdivision Table")
#     mycursor.execute("SELECT * FROM Subdivision")
#     data = mycursor.fetchall()
#     st.write(data)
    
def insert_student_data():
 
    col1, col2,col3,col4 = st.columns(4)

    # Define input fields
    with col1:
        title = st.selectbox("Title", ("Mr.", "Mrs.", "Master", "Miss", "Sri", "Sk", "Dr."))
        
    with col2:
       fname = st.text_input("First Name")   
       
    with col3:
        mname = st.text_input("Middle Name")
    
    with col4:
       lname = st.text_input("Last Name")    
        
    icvaid = st.number_input("ICVA ID", min_value=1, key="ICVAId")   
    
    col1, col2, col3 = st.columns(3)

    # Define input fields
    with col1:
        father_name = st.text_input("Father Name")

    with col2:
        mother_name = st.text_input("Mother Name")

    with col3:
        class_id = st.selectbox("Class", ("001 - CLASS SEVEN", "002 - CLASS EIGHT"))
    # p_subdiv_id = st.selectbox("Permanent Subdivision", (1, 2, 3))
    # p_dist_id = st.selectbox("Permanent District", (1, 2, 3))
    # p_state_id = st.selectbox("Permanent State", (1, 2, 3))
    # p_country_id = st.selectbox("Permanent Country", (1, 2, 3))
    # p_pin_code = st.number_input("Permanent Pin Code", min_value=100000, max_value=9999999)
    # c_address = st.text_area("Communication Address")
    # c_subdiv_id = st.selectbox("Communication Subdivision", (1, 2, 3))
    # c_dist_id = st.selectbox("Communication District", (1, 2, 3))
    # c_state_id = st.selectbox("Communication State", (1, 2, 3))
    # c_country_id = st.selectbox("Communication Country", (1, 2, 3))
    #c_pin_code = st.number_input("Communication Pin Code", min_value=100000, max_value=9999999)
    
    permanent_address = st.text_area("Permanent Address", key="permanent_address")
    
    col1, col2 = st.columns(2)

    # Define input fields
    with col1:
        gender = st.selectbox("Gender", ("FEMALE", "MALE", "TRANSGENDER"))

    with col2:
        doa = st.date_input("Date of Admission")
        
    col1, col2, col3, col4 = st.columns(4)

    # Define input fields
    with col1:
        email_address = st.text_input("Email Address")

    with col2:
        alt_email_address = st.text_input("Alternate Email Address")

    with col3:
        mobile_no = st.number_input("Mobile No", min_value=1000000000, max_value=9999999999)

    with col4:
        alt_mobile_no = st.number_input("Alternate Mobile No", min_value=1000000000, max_value=9999999999)
        
     # Create two columns for input fields
    col1, col2 = st.columns(2)

    # Define input fields
    with col1:
        dob = st.date_input("Date of Birth", key="DoB")
        schoolname = st.text_input("School Name", key="SchoolName")
       

    with col2:
        schoolid = st.number_input("School ID", min_value=1, key="SchoolId")
    
        


    if st.button("Insert", key="insert_button"):
        insert_query = "INSERT INTO Students (FName, MName, LName, Title, FatherName, MotherName, ClassID, Gender, DoA, PAddress , EmailAddress, AltEmailAddress, MobileNo, AltMobileNo, ICVAId, DoB , SchoolName, SchoolId) " \
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            fname, mname, lname, title, father_name, mother_name, class_id.split(" - ")[0], gender, doa, permanent_address,
            email_address, alt_email_address, mobile_no, alt_mobile_no,icvaid, dob , schoolname, schoolid
        )

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Student data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")
# # Function to display the Students table
# def display_students_table():
#     st.header("Students Table")
#     mycursor.execute("SELECT * FROM Students")
#     data = mycursor.fetchall()
#     st.write(data)
    

# Function to insert data into the Courses table
def insert_course_data():
    st.header("Insert Data into Courses Table")
    course_name = st.text_input("Course Name")
    course_short_name = st.text_input("Course Short Name")
    
    if st.button("Insert"):
        insert_query = "INSERT INTO Courses (Name, ShortName) VALUES (%s, %s)"
        values = (course_name, course_short_name)

        try:
            mycursor.execute(insert_query, values)
            mydb.commit()
            st.success("Course data inserted successfully!")
        except mysql.connector.Error as err:
            st.error(f"An error occurred: {err}")

# # Function to display the Courses table
# def display_courses_table():
#     st.header("Courses Table")
#     mycursor.execute("SELECT * FROM Courses")
#     data = mycursor.fetchall()
#     st.write(data)
        
                
# # Check the selected table and perform actions accordingly
# if selected_table == "Language":
#     insert_language_data()
#     #display_language_table()
    
# elif selected_table == "Subjects":
#     insert_subject_data()
#     #display_subjects_table()
    
# elif selected_table == "Classes":
#     insert_class_data()
#    # display_classes_table()    

# elif selected_table == "Exams":
#     insert_exam_data()
#    # display_exams_table()
    
# elif selected_table == "Organizations":
#     insert_organization_data()
#     #display_organizations_table() 
    
# elif selected_table == "Experts":
#     insert_expert_data()
#     #display_experts_table()     
 
 
# elif selected_table == "Questions":   
#     insert_question_data()
#     #display_questions_table()  
    
# elif selected_table == "Answers":
#     insert_answer_data()
#     #display_answers_table()    
    
# elif selected_table == "ExamPaper":
#     insert_exam_paper_data()
#     #display_exam_paper_table()
    
# elif selected_table == "MCQPaperSet":
#     insert_mcq_data()
#     #display_mcq_table()        


# elif selected_table == "PaperSet":
#     insert_paper_set_data()
#     #display_paper_set_table()


# elif selected_table == "Country":
#     insert_country_data()
#     #display_country_table()    
    
# elif selected_table == "State":  
#     insert_state_data()
#     #display_state_table()    


# elif selected_table == "District":  # Add this condition for the District table
#     insert_district_data()
#    # display_district_table()


# elif selected_table == "Subdivision":  # Add this condition for the Subdivision table
#     insert_subdivision_data()
#    # display_subdivision_table()
    
# elif selected_table == "Students":  # Add this condition for the Students table
#     insert_student_data()
#    # display_students_table()    
    
# elif selected_table == "Courses":  # Add this condition for the Courses table
#     insert_course_data()
#  #   display_courses_table()    









# def insert_mcq_data():
#     st.header("Insert Data into MCQPaperSet Table")

#     # Initialize lists to store question data
#     ques_ids = []
#     exam_paper_ids = []
#     lang_ids = []
#     options1 = []
#     options2 = []
#     options3 = []
#     options4 = []
#     marks_list = []
#     harder_ranks = []

#     for i in range(num_questions):
#     st.subheader(f"Question {i + 1}")

#     ques_id = st.number_input("Question ID", min_value=1, step=1)
#     exam_paper_id = st.number_input("Exam Paper ID", min_value=1, step=1)

#     # Create four columns for input fields
#     col1, col2, col3, col4 = st.columns(4)

#     # Define input fields
#     with col1:
#         option1 = st.text_input("Option 1")

#     with col2:
#         option2 = st.text_input("Option 2")

#     with col3:
#         option3 = st.text_input("Option 3")

#     with col4:
#         option4 = st.text_input("Option 4")
#         marks = st.number_input("Marks", min_value=1, step=1)
#         harder_rank = st.number_input("Harder Rank", min_value=1, max_value=4, step=1)

#     # Append data to respective lists
#     ques_ids.append(ques_id)
#     exam_paper_ids.append(exam_paper_id)
#     lang_ids.append(lang_id)
#     options1.append(option1)
#     options2.append(option2)
#     options3.append(option3)
#     options4.append(option4)
#     marks_list.append(marks)
#     harder_ranks.append(harder_rank)

#     # Add a sign/button to add more questions
#     if i < num_questions - 1:
#         st.write("--------------")  # Separation line
#         add_question = st.button("Add Another Question", key=f"add_question_{i}")
#         if add_question:
#             continue  # Continue to the next iteration

             

#     if st.button("Insert", key="insert_button2"):
#         try:
#             # Insert all questions in one query using executemany
#             insert_query = "INSERT INTO MCQPaperSet (QuesID, ExamPaperID, LangID, Option1, Option2, Option3, Option4, Marks, HarderRank) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
#             values = list(zip(ques_ids, exam_paper_ids, lang_ids, options1, options2, options3, options4, marks_list, harder_ranks))

#             mycursor.executemany(insert_query, values)
#             mydb.commit()
#             st.success(f"{num_questions} MCQs inserted successfully!")
#         except mysql.connector.Error as err:
#             st.error(f"An error occurred: {err}")

tab1, tab2  = st.tabs(["Students","Experts"])

with tab1:
   st.header("Student Details")
   insert_student_data()

with tab2:
   st.header("Experts details")
   insert_expert_data()

# with tab3:
#    st.header("MCQPaperSet")
#    insert_mcq_data()
           
# Close database connection
mycursor.close()
mydb.close()
