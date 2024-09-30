import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from mypharmacy import search_medicine_skincare
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def presc_analyze():
    # Load environment variables (API key)
    load_dotenv()

    # Load environment variables and configure the API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Function to interact with Google Generative AI (Gemini) model
    def get_gemini_response(input_prompt, image_data, user_prompt):
        # Define the model and safety settings
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
        model = genai.GenerativeModel("gemini-1.5-flash", safety_settings=safety_settings)
        
        # Get the response
        response = model.generate_content([input_prompt, image_data[0], user_prompt])
        return response.text

    # Function to handle image upload
    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            image_parts = [
                {
                    "mime_type": uploaded_file.type,
                    "data": bytes_data,
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("No file uploaded")

    # Heuristic method to extract medicine names from text
    def extract_medicine_names_heuristic(text):
        import re
        # Split text into potential medicine names based on delimiters
        potential_medicines = re.split(r'\d+\.\s*|\n|\r|,', text)
        # Clean up and filter non-medicine words
        potential_medicines = [med.strip() for med in potential_medicines if med.strip() and med.lower() not in ["the", "to", "of", "and", "is"]]
        return potential_medicines

    # Streamlit app setup
    st.title("AI-Powered Prescription Analyzer 🧴")
    st.write("Welcome to DERMINI's Prescription Analyzer! Our cutting-edge AI scans your prescription images to detect potential information, offering personalized insights,dosage and care suggestions. Upload a photo of your prescription, and let DERMINI guide you on the path to healthier skin!")
    
    # File upload for prescription image
    st.write("Choose a prescription image for analysis...")
    uploaded_file = st.file_uploader("Drag and drop file here", type=["jpg", "jpeg", "png", "webp", "jfif", "afif"], label_visibility="visible")
    image = ""
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    submit = st.button("Analyze Image")

    # Define the user prompt
    user_prompt = "Give me details about the entire prescription , focusing on medications and frequency."
    
    # Define system prompt for interpreting prescriptions
    info_prompt = """You are an expert in interpreting prescriptions.
    You will receive prescription images and answer questions based on them. Try your best to provide the medicine links .
    Please include information such as {user_prompt}."""

    # Define prompt for extracting medicine names
    medicine_prompt = "Please list all medications mentioned in the prescription."

    if submit:
        image_data = input_image_setup(uploaded_file)

        # Get extracted information from Google Generative AI
        info_response = get_gemini_response(info_prompt.format(user_prompt=user_prompt), image_data, "")
        st.subheader("Extracted Information:")
        st.write(info_response)

        # Get extracted medicine names
        medicine_response = get_gemini_response(medicine_prompt, image_data, "")
        medicine_names = extract_medicine_names_heuristic(medicine_response)

        if medicine_names:
            st.subheader("Medicine Names:")
            # Display medicine names
            medicine_list = ", ".join(medicine_names)
            st.write(medicine_list)

            # Provide shopping links for each medicine name
            st.subheader("Medicines with Links:")
            for medicine in medicine_names:
                st.markdown(f"### {medicine}")
                results_df = search_medicine_skincare(medicine)
                if results_df is not None and not results_df.empty:
                    for index, row in results_df.head(7).iterrows():
                        st.markdown(f"[{row['Product Name']}]({row['Link']}) - {row['Price']} ₹")
                else:
                    st.write(f"No results found for {medicine}")
        else:
            st.write("No medicine names found using the heuristic approach.")

    st.write("To analyze your prescription image, click on the 'Choose a prescription image for analysis...' button above and select an image file from your device. Once the image is uploaded, click on 'Analyze Image' to receive detailed insights into prescription and recommendations.")
    st.balloons()

if __name__ == '__main__':
    presc_analyze()
