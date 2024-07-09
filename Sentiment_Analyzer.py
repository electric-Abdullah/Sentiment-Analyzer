# Import the Python SDK
import google.generativeai as genai
import streamlit as st
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import streamlit.components.v1 as components
import os 

# Add Api key
genai.configure(api_key=os.getenv("Google_Gemini_Api"))

# Title with colors and relevant emojis
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>😊 Best Sentiment Analyzer 😢</h1>", unsafe_allow_html=True)

model = genai.GenerativeModel('gemini-pro')

# Text input field with label
st.markdown("<h3 style='color: #2196F3;'>Write Your Sentiment:</h3>", unsafe_allow_html=True)
Prompt = st.text_input("")

# Button to trigger text transfer
get_response = st.button("➡➡", key='translate_button')

# Empty container to hold the transferred text
response_field = st.empty()

# Function to return styled sentiment
def styled_sentiment(sentiment):
    if sentiment.lower() in ['positive', 'happy']:
        return f'<p style="color:green; font-size:20px;">😊 Positive</p>'
    elif sentiment.lower() in ['negative', 'sad']:
        return f'<p style="color:red; font-size:20px;">😢 Negative</p>'
    elif sentiment.lower() == 'neutral':
        return f'<p style="color:gray; font-size:20px;">😐 Neutral</p>'
    else:
        return f'<p style="color:blue; font-size:20px;">🤔 {sentiment.capitalize()}</p>'

# Logic to transfer text on button click
if get_response:
    response = model.generate_content(
        [f"What is the sentiment of this sentence? Tell me in one word '{Prompt}'"], 
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }
    )
    sentiment = response.text.strip().lower()
    styled_response = styled_sentiment(sentiment)
    response_field.markdown(styled_response, unsafe_allow_html=True)

# JavaScript code to detect Enter key press and trigger the button click
components.html("""
<script>
document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        // Change the selector to find the button
        const buttons = window.parent.document.querySelectorAll('button');
        buttons.forEach(button => {
            if (button.innerText === '➡➡') {
                button.click();
            }
        });
    }
});
</script>
""")



made_by_container = st.empty()

made_by_container.markdown("<p style='position: fixed;bottom: 10;right:10;background-color:rgba(55,40,55); color: #ffffff;padding: 10px;border-radius: 10px;box-shadow: 0px 0px 10px rgba(255, 105, 180, 0.5);animation: pulse 5s infinite; @keyframes pulse {10% {box-shadow: 0px 0px 10px rgba(255, 105, 180, 0.5);}50% {box-shadow: 0px 0px 20px rgba(255, 105, 180, 1);}100% {box-shadow: 0px 0px 10px rgba(255, 105, 180, 0.5);}'>Made By Abdullah</p>", unsafe_allow_html=True)


