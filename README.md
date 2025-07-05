# jarvis-assistant


Your Intelligent Voice + Web-Based Gemini-Powered Personal Assistant
Built using Flask, Gemini AI, Text-to-Speech, Speech Recognition, and more.

Your Intelligent Voice + Web-Based Gemini-Powered Personal Assistant
Built using Flask, Gemini AI, Text-to-Speech, Speech Recognition, and more.

🧠 Features
🎤 Voice & Text Interaction
Accepts input via text or microphone
Uses speech_recognition for real-time voice input
Displays user messages in an animated, styled chat UI

🗣️ Text-to-Speech (TTS)
Replies are spoken aloud using pyttsx3
Can toggle speech on/off in the UI

🤖 Gemini AI Integration
Uses Google Gemini (generativeai) for natural, intelligent conversations
Handles queries about music, videos, education, entertainment, and general knowledge

🔗 Smart Link Detection & Autoplay
Automatically detects YouTube or media links in Gemini’s response
Opens the first valid link automatically in the user's browser

🌐 Web UI with Responsive Design
Stylish frontend built in HTML, CSS, and vanilla JS

Responsive design for desktops and mobiles

Includes buttons for:
Sending messages
Using microphone
Toggling speech
Clearing chat


💡 Tech Stack
Component	Library
AI Model	google-generativeai (Gemini)
Web Server	Flask
Speech-to-Text	speech_recognition
Text-to-Speech	pyttsx3
Frontend UI	HTML + CSS + JS

🛠️ Customization
🔑 Replace the GEMINI_API_KEY in app.py with your own key

🎨 Style the UI in index.html to suit your design

🎵 To handle local music or app launching, add Python commands to Gemini’s get_gemini_response() context
