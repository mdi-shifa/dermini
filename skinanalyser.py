# Importing All the modules
import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
def skinanalyser():
     
    # Load environment variables and configure the API key
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    # Function to load Gemini Vision Model and get response
    def get_gemini_response(image, prompt):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([image[0], prompt])
        return response.text

    # Function to extract data from uploaded image
    def input_image_setup(uploaded_file):
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            return [{"mime_type": uploaded_file.type, "data": bytes_data}]
        else:
            raise FileNotFoundError("No file uploaded")

    # Streamlit UI setup
    st.title("AI-Powered Skin Health Analyzer")
    st.write(
        """
        Welcome to DERMINI's Skin Health Analyzer! Our cutting-edge AI scans your skin images to detect potential issues,
        offering personalized insights and care suggestions. Upload a photo of your skin, and let DERMINI guide you on the path to healthier skin!
        """
    )

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose a skin image for analysis...", type=["jpg", "jpeg", "png", "webp", "jfif", "afif"])
    image = None

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        # Defining a System Prompt
        input_prompt = f"""Image: (content of the uploaded image)
        Who are you? : You are an expert dermatologist AI with the ability to accurately analyze skin conditions.
        Text: Analyze the image and provide the following information:

        * Skin Condition: Identify the skin condition (e.g., acne, eczema, psoriasis, etc.) present in the image. If no condition is detected, provide a disclaimer.
        * Disease Detection: If a skin defect or disease is detected, identify the specific condition and provide a disclaimer.
        Only if a disease is detected, proceed with the following:
        * Severity: Assess the severity of the skin condition (mild, moderate, severe).
        * Symptoms: Describe the common symptoms associated with the detected skin condition.
        * Treatment Suggestions: Provide potential treatment recommendations or skincare tips based on the analysis.
        * Precautions: Suggest preventative measures to avoid worsening of the condition.

        Give the response with headings.
        Inform the user if the image is not related to skin defects or analysis.
        """

        submit = st.button("Analyze Image")
        st.warning("Skin conditions and severity will be identified only if the image contains the necessary information.")
        
        Disclaimer = (
            "**Disclaimer:** This application uses AI-based image analysis to provide potential information about skin conditions. "
            "The results are for informational purposes only and should not be considered a substitute for professional medical advice. "
            "For any concerns about your skin health, please consult a licensed dermatologist. They can provide a comprehensive diagnosis and tailored treatment plan."
        )

        if submit:
            if image:
                with st.spinner("Analyzing Image..."):
                    image_data = input_image_setup(uploaded_file)  # Step-1 --> image is converted into data
                    response = get_gemini_response(image_data, input_prompt)  # Step-2 --> Using gemini model to get desired response
                st.subheader("Analysis Result:")
                st.write(response)
                st.warning(Disclaimer)
                st.balloons()
            else:
                st.error("Please upload an image to proceed.")
    else:
        st.info("Upload an image of your skin to get started!")
        st.write(
            """
            To analyze your skin image, click on the 'Choose a skin image for analysis...' button above and select an image file from your device. 
            Once the image is uploaded, click on 'Analyze Image' to receive detailed insights into potential skin conditions and recommendations.
            """
        )
        st.balloons()

if __name__ == "__main__":
    skinanalyser()
