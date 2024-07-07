# Best Sentiment Analyzer 😊😢

This project utilizes Google's Generative AI and Streamlit to perform sentiment analysis on text input.

## Features

- **Sentiment Analysis**: Analyzes the sentiment (positive, negative, neutral) of user-provided text.
- **Styled Outputs**: Displays sentiment results with colored emojis based on sentiment categories.
- **Input Handling**: Accepts user input via a text field and triggers analysis upon button click.
- **Safety Settings**: Includes settings to block high levels of hate speech and harassment in generated responses.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/electric-Abdullah/Sentiment-Analyzer.git
   cd Sentiment-Analyzer
   
2. Install dependencies:
   `````
   pip install -r requirements.txt

## Usage
1. Set up your Google Generative AI API key in config.py:
   `````
   genai.configure(api_key="your-api-key")

3. Run the Streamlit app:
   `````
   streamlit run app.py

4. Enter text in the provided field and click the ➡➡ button to analyze sentiment.
   

