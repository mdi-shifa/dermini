# dermini_feedback.py
import streamlit as st
import pandas as pd
import os
import re

def show_dermini_feedback():  
    st.title("Feedback Form")
    
    # Initialize form
    with st.form(key='feedback_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        rating = st.selectbox("Rate your experience (1-5)", [1, 2, 3, 4, 5])
        comments = st.text_area("Additional Comments")

        # Submit button
        submit_button = st.form_submit_button(label='Submit')

    # Validate form submission
    if submit_button:
        # Check if all fields are filled
        if not name.strip() or not email.strip() or not rating or not comments.strip():
            st.error("Please fill in all fields before submitting.")
        # Validate email format using regular expression
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Please enter a valid email address.")
        else:
            st.success("Thank you for your feedback!")

            # Save feedback to a CSV file
            feedback_data = {
                'Name': [name],
                'Email': [email],
                'Rating': [rating],
                'Comments': [comments]
            }

            feedback_df = pd.DataFrame(feedback_data)
            if os.path.exists('feedback.csv'):
                feedback_df.to_csv('feedback.csv', mode='a', header=False, index=False)
            else:
                feedback_df.to_csv('feedback.csv', index=False)

            st.write("Your feedback has been recorded.")

# Run the feedback form if this script is executed directly
if __name__ == "__main__":
    show_dermini_feedback()
