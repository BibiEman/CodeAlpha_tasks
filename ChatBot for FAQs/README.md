# FAQ Chatbot

A modern chatbot that can answer frequently asked questions using Natural Language Processing (NLTK). Available in both command-line and graphical user interface versions.

## Features
- Natural language understanding using NLTK
- Cosine similarity for finding the best matching responses
- Easy to customize FAQ database
- Modern graphical user interface with clean design
- Command-line interface option
- Real-time response generation
- Message history with scroll support

## Setup Instructions
1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
   - For GUI version:
   ```bash
   python gui_chatbot.py
   ```
   - For command-line version:
   ```bash
   python chatbot.py
   ```

## GUI Features
- Clean, modern interface using the Arc theme
- Scrollable chat history
- Message input with Enter key support
- Send button for submitting questions
- Automatic scrolling to latest messages
- Visual separation between user and bot messages
- Resizable window

## Customizing FAQs
You can modify the FAQs by editing the `faq_data.py` file. Each FAQ entry should contain:
- Question: The frequently asked question
- Answer: The corresponding answer

## Usage
### GUI Version
1. Launch the application using `python gui_chatbot.py`
2. Type your question in the input field
3. Press Enter or click the Send button
4. View the bot's response in the chat display

### Command-line Version
- Type your question when prompted
- Type 'quit' to exit the chatbot
- The chatbot will find the most relevant answer from its FAQ database 