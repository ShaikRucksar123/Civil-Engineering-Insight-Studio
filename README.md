🏗️ Civil Engineering Insight Studio

An AI-powered web application that intelligently analyzes images of civil engineering structures and generates detailed, structured engineering insights using Google Gemini Vision (Gemini Flash).

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
📌 Project Overview

Civil Engineering Insight Studio enables users to upload images of civil engineering structures such as buildings, bridges, dams, and roads. The system processes the image using advanced AI vision capabilities and provides an automated structural analysis that includes:

🏢 Type of Structure
🧱 Structural System
🏗️ Materials Used
⚙️ Construction Techniques
🎯 Engineering Purpose
🛡️ Safety and Design Features

The application combines a modern Streamlit interface with Google Gemini Flash for intelligent image-based engineering interpretation.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
🧠 Technologies Used

Python
Streamlit – Interactive Web Interface
Google Gemini Generative AI API
Gemini Flash (Vision Model)
Pillow (PIL) – Image Processing
python-dotenv – Environment Variable Management

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
🔑 API Used

API Name: Google Gemini Generative AI API
Python SDK: google-genai
Model: models/gemini-flash-latest
Authentication: API Key

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
⚙️ System Architecture

User
↓
Streamlit Web Interface
↓
Python Backend (app.py)
↓
Google GenAI Client (google-genai)
↓
Gemini Flash Vision Model
↓
Generated Civil Engineering Insights

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
📁 Project Structure

civil-engineering-insight/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
📦 Requirements

Create a file named requirements.txt:

streamlit
python-dotenv
Pillow
google-genai

Install dependencies:

pip install -r requirements.txt

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
🔐 API Key Setup

Generate a Google Gemini API key from Google AI Studio

Create a .env file in the project root directory

Add your API key:

GOOGLE_API_KEY=your_api_key_here

⚠️ Important: Do not upload or share your .env file publicly.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
▶️ How to Run the Application

streamlit run app.py

The application will automatically open in your default web browser.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
🖼️ Application Workflow

Upload an image of a civil engineering structure
Optionally provide additional description
Image and text are processed by the Gemini Flash Vision model
AI analyzes structural characteristics
Structured engineering insights are displayed instantly

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
📊 Sample Output

Type of Structure: Reinforced Concrete Building
Structural System: RCC Frame Structure
Materials Used: Concrete, Steel Reinforcement
Construction Technique: Cast-in-place Concrete
Engineering Purpose: Residential or Commercial Usage
Safety Features: Columns, Beams, Load Distribution Systems

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - 
🚀 Future Enhancements

Automated PDF report generation
Confidence scoring for AI insights
Multi-image comparative analysis
Cloud deployment using Streamlit Cloud
Advanced structural defect and damage detection

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
🧑‍💻 Author

Rucksar Shaik
Internship Project – AI in Civil Engineering
