import streamlit as st
import os
import time
from dotenv import load_dotenv
from PIL import Image
from google import genai

# --------------------------------------
# Page Config
# --------------------------------------
st.set_page_config(
    page_title="Civil Engineering Insight Studio",
    page_icon="🏗️",
    layout="wide"
)

# --------------------------------------
# FINAL CLEAN CSS (NO FILE PILL + NO ENTER HINT)
# --------------------------------------
st.markdown(
    """
    <style>
    /* ===== APP BACKGROUND ===== */
    .stApp {
        background: linear-gradient(135deg, #0b1220, #020617);
    }

    .block-container {
        background-color: rgba(15, 23, 42, 0.9);
        padding: 2.5rem;
        border-radius: 22px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.7);
    }

    h1 {
        text-align: center;
        font-weight: 900;
        color: #ffffff !important;
    }

    label {
        color: #f9fafb !important;
        font-weight: 700;
    }

    /* ===== TEXT INPUT ===== */
    .stTextInput input {
        background-color: #020617 !important;
        color: #ffffff !important;
        font-size: 16px;
        font-weight: 600;
        border-radius: 14px;
        border: 2px solid #6366f1;
        padding: 14px;
    }

    .stTextInput input::placeholder {
        color: #cbd5f5 !important;
    }

    /* 🚀 REMOVE "Press Enter to apply" */
    div[data-testid="InputInstructions"] {
        display: none !important;
    }

    /* ===== FILE UPLOADER ===== */
    section[data-testid="stFileUploader"] {
        background-color: #020617 !important;
        border-radius: 16px;
        padding: 18px;
        border: 2px dashed #6366f1;
    }

    /* 🚀 REMOVE ROUNDED FILE NAME PILL */
    div[data-testid="stFileUploaderFile"] {
        display: none !important;
    }

    /* ===== BUTTON ===== */
    .stButton button {
        background: linear-gradient(90deg, #6366f1, #22d3ee);
        color: #020617;
        border-radius: 16px;
        height: 3.2em;
        font-size: 17px;
        font-weight: 800;
        border: none;
    }

    /* ===== OUTPUT ===== */
    .analysis-box {
        background-color: rgba(2, 6, 23, 0.97);
        padding: 28px;
        border-radius: 20px;
        margin-top: 30px;
        border-left: 6px solid #6366f1;
        color: #ffffff;
    }

    /* ===== SPINNER ===== */
    div[data-testid="stSpinner"] {
        background: rgba(240, 249, 255, 0.95) !important;
        border-radius: 20px;
        padding: 16px 26px;
        border: 2px solid #6366f1;
    }

    div[data-testid="stSpinner"] span {
        color: #020617 !important;
        font-weight: 900;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------
# Load API Key
# --------------------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in .env file")
    st.stop()

# --------------------------------------
# Gemini Client
# --------------------------------------
client = genai.Client(api_key=API_KEY)

# --------------------------------------
# Gemini Function
# --------------------------------------
def get_gemini_response(user_text, image: Image.Image):
    prompt = f"""
You are a professional civil engineer.

Analyze the given image and explain:
1. Type of structure
2. Structural system
3. Materials used
4. Construction technique
5. Engineering purpose
6. Safety or design features

User notes: {user_text if user_text else "Not provided"}
"""
    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="models/gemini-flash-latest",
                contents=[prompt, image]
            )
            return response.text
        except Exception as e:
            if "503" in str(e):
                time.sleep(2)
            else:
                raise e

    return "⚠️ Model busy. Please try again later."

# --------------------------------------
# UI
# --------------------------------------
st.title("🏗️ Civil Engineering Insight Studio")

user_text = st.text_input(
    "✏️ Optional Description",
    placeholder="Example: Bridge, building, dam, road..."
)

uploaded_file = st.file_uploader(
    "📷 Upload an Image",
    type=["jpg", "jpeg", "png"]
)

image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=700)

# --------------------------------------
# Button Action
# --------------------------------------
if st.button("🚀 Describe Structure"):
    if image is None:
        st.warning("⚠️ Please upload an image first.")
    else:
        with st.spinner("🔍 Analyzing structure..."):
            result = get_gemini_response(user_text, image)

        st.markdown(
            f"""
            <div class="analysis-box">
                <h3>📊 Civil Engineering Analysis</h3>
                {result}
            </div>
            """,
            unsafe_allow_html=True
        )
