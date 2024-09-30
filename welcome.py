import streamlit as st

def welcome():
    # Load Google Fonts
    st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Lora:wght@700&display=swap" rel="stylesheet">""", unsafe_allow_html=True)

    # Logo and main heading with updated font style and size
    st.image(r"C:\Users\$ ASUS $\Desktop\projects.py\images\logo.png", width=200)  # Ensure the image path is correct
    st.markdown("""
        <h1 style="font-family: 'Lora', serif; font-size: 48px; color: #007a87; text-align: center;">
        Welcome to DERMINI 🥼
        </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <p style="font-family: 'Roboto', sans-serif; font-size: 24px; color: #555555; text-align: center;">
        Your AI-Powered Dermatology Assistant🌟
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")  # Horizontal line

    # Main layout with two columns
    col1, col2 = st.columns(2)

    # Key Features section centered (Column 1)
    with col1:
        st.markdown("""
        <div style="background-color:#e5f7fa; padding:20px; border-radius:10px; text-align:center; box-shadow: 0px 4px 8px rgba(0,0,0,0.2);">
        <h3 style="color:#007a87; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">Key Features 🌈</h3>
        <p style="color:#333333; font-size:16px; margin-bottom:15px; font-family: 'Roboto', sans-serif;">Explore the capabilities that DERMINI offers to assist with your skincare needs:</p>
        <ul style="text-align:left; color:#333333; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
        <li><strong>🧴 Skin Defect Analysis</strong><br>
        Upload images to analyze skin defects like acne, rashes, or other issues. Get detailed information on possible causes and treatments.</li><br>

        <li><strong>🤖 AI Chatbot for Dermatology Advice</strong><br>
        An interactive chatbot that provides answers to skincare-related queries. Get personalized advice on skin types, skincare routines, and more.</li><br>

        <li><strong>✨ Personalized Skincare Recommendations</strong><br>
        Receive tailored skincare recommendations based on your skin type and conditions. Enhance your skincare routine with expert advice.</li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Additional Key Features (Column 2)
    with col2:
        st.markdown("""
        <div style="background-color:#e5f7fa; padding:20px; border-radius:10px; box-shadow: 0px 4px 8px rgba(0,0,0,0.2);">
        <h3 style="color:#007a87; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">Additional Key Features 🌟</h3>
        <ul style="text-align:left; color:#333333; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
        <li><strong>📄 Prescription Analyzer</strong><br>
        Upload dermat prescriptions to manage your skincare products effectively. Get detailed insights into the prescribed treatments.</li><br>

        <li><strong>🛒 Skincare Shopping</strong><br>
        Explore recommended skincare products based on your skin condition. Shop products tailored to your skin needs.</li><br>

        <li><strong>📞 Contact and Feedback</strong><br>
        Contact form for inquiries and feedback collection. Reach out for any questions to enhance DERMINI.</li><br>

        <li><strong>🔮 Future Features</strong><br>
        Planned improvements to further assist users with their dermat needs. </li><br>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # How to Use section centered (Spanning both columns)
    st.markdown("""
    <div style="background-color:#f9f9f9; padding:20px; border-radius:10px; text-align:center; box-shadow: 0px 4px 8px rgba(0,0,0,0.2);">
    <h3 style="color:#4d4d4d; font-size:24px; margin-bottom:10px; font-family: 'Lora', serif;">How to Use 🛠️</h3>
    <ul style="text-align:left; color:#333333; font-size:16px; line-height:1.6; font-family: 'Roboto', sans-serif;">
    <li>🖱️ Navigate through the app using the sidebar menu on the left.</li>
    <li>📷 Upload an image to analyze skin defects and receive detailed reports.</li>
    <li>💬 Interact with the AI chatbot to get personalized dermatology advice and skincare tips.</li>
    <li>📜 Use the Prescription Analyzer to input and analyze your skincare prescriptions.</li>
    <li>🛍️ Explore the Skincare Shopping section to find products recommended for your skin condition.</li>
    <li>📩 Provide feedback or contact support through the Contact and Feedback form.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    welcome()
