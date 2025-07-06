from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import google.generativeai as genai
import re
import webbrowser
from urllib.parse import urlparse

app = Flask(__name__)

# Gemini Setup
GEMINI_API_KEY = "AIzaSyDinNdVUUZNGqNaWITNwIE7UhK4VbBgOE0"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def extract_urls(text):
    """Extract URLs from text"""
    url_pattern = r'https?://[^\s<>"]{2,}'
    urls = re.findall(url_pattern, text)
    return urls

def is_valid_url(url):
    """Check if URL is valid"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def open_url(url):
    """Open URL in default browser"""
    try:
        webbrowser.open(url)
        return True
    except:
        return False

def get_gemini_response(prompt, context=""):
    """Get response from Gemini API"""
    full_prompt = f"""
    You are JARVIS, an intelligent AI assistant. When users ask for videos, music, or any media content, provide helpful responses and include relevant YouTube links or other media links when possible.

    For video/music requests, you can suggest links like:
    - YouTube videos
    - Music videos or songs
    - Educational content
    - Entertainment content

    Always be helpful and provide the best possible response along with relevant links when appropriate.

    Context: {context}
    User input: {prompt}

    Respond helpfully and include relevant links when possible:
    """
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error getting response: {e}"

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Get response from Gemini
    response = get_gemini_response(user_message)
    
    # Extract URLs from response
    urls = extract_urls(response)
    valid_urls = [url for url in urls if is_valid_url(url)]
    
    # Auto-open first valid URL if found
    opened_url = None
    if valid_urls:
        first_url = valid_urls[0]
        if open_url(first_url):
            opened_url = first_url
    
    return jsonify({
        'response': response,
        'urls': valid_urls,
        'opened_url': opened_url
    })

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    """Convert speech to text"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
            
        text = r.recognize_google(audio)
        return jsonify({'text': text})
        
    except sr.WaitTimeoutError:
        return jsonify({'error': 'Timeout. No speech detected.'}), 400
    except sr.UnknownValueError:
        return jsonify({'error': 'Sorry, I didn\'t catch that.'}), 400
    except sr.RequestError as e:
        return jsonify({'error': f'Network error: {e}'}), 500
    except Exception as e:
        return jsonify({'error': f'Error: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
