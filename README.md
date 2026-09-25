# Gemini AI Chatbot


A console-based AI chatbot built in Python, powered by Google's Gemini API. Type a message and get a real-time AI-generated response, right in your terminal.

## Features

- Real-time conversational responses using Google's Gemini AI model
- Secure API key handling using environment variables (`.env`), never hardcoded in source code
- Simple, continuous chat loop until the user types "exit"

## Concepts Used

- Python functions and modules (`chatbot.py` separated from the main app logic)
- Environment variables for secure API key management (`python-dotenv`)
- REST API integration (Google Generative AI SDK)
- Basic control flow: loops and conditionals for the chat interface

## Project Structure

```
├── chatbot.py         # Configures the Gemini client and defines get_response()
├── app_console.py     # Console chat loop that uses chatbot.py
├── requirements.txt   # Python dependencies
└── .gitignore         # Ensures .env (API key) is never committed
```

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project folder with your own Gemini API key:
   ```
   GEMINI_API_KEY=your_own_api_key_here
   ```
   Get a free key at [Google AI Studio](https://aistudio.google.com/apikey).
3. Run the chatbot:
   ```
   python app_console.py
   ```
4. Type your message and press Enter. Type `exit` to quit.

## Sample Usage

```
Gemini AI Chatbot (type 'exit' to quit)
You: hi
Bot: Hello! How can I help you today?
You: what is 2+2
Bot: 2 + 2 = 4
```

## Security Note

The `.env` file containing the API key is intentionally excluded from this repository via `.gitignore`. Anyone running this project needs to supply their own API key.
