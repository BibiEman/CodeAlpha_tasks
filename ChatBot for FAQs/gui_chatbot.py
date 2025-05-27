import tkinter as tk
from tkinter import ttk, scrolledtext
from ttkthemes import ThemedTk
import time
from chatbot import FAQChatbot

class ChatbotGUI:
    def __init__(self):
        self.chatbot = FAQChatbot()
        
        # Create themed root window
        self.root = ThemedTk(theme="arc")
        self.root.title("FAQ Chatbot Assistant")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set color scheme
        self.colors = {
            'bg': '#E8EAF6',  # Light blue-grey background
            'user_bubble': '#2196F3',  # Material Blue
            'bot_bubble': '#673AB7',   # Material Deep Purple
            'input_bg': '#FFFFFF',     # White
            'button': '#FF4081',       # Pink accent
            'text_light': '#FFFFFF',   # White text
            'text_dark': '#424242'     # Dark grey text
        }
        
        # Configure grid weight
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        self.setup_styles()
        
    def setup_styles(self):
        """Configure custom styles for widgets"""
        style = ttk.Style()
        
        # Configure main frame
        style.configure("Main.TFrame", background=self.colors['bg'])
        
        # Configure input frame
        style.configure("Input.TFrame", background=self.colors['bg'])
        
        # Configure send button
        style.configure("Send.TButton",
                       padding=8,
                       font=("Helvetica", 10, "bold"),
                       background=self.colors['button'])
        
    def create_widgets(self):
        """Create and setup all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, style="Main.TFrame", padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Chat display area with custom background
        self.chat_display = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            font=("Helvetica", 11),
            background=self.colors['bg'],
            borderwidth=0,
            relief="flat"
        )
        self.chat_display.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.chat_display.config(state=tk.DISABLED)
        
        # Configure tags for message bubbles
        self.chat_display.tag_configure(
            "user_message",
            justify="right",
            lmargin1=50,
            lmargin2=50,
            rmargin=10,
            spacing1=10,
            spacing3=10
        )
        self.chat_display.tag_configure(
            "bot_message",
            justify="left",
            lmargin1=10,
            lmargin2=10,
            rmargin=50,
            spacing1=10,
            spacing3=10
        )
        
        # Input frame with rounded corners
        input_frame = ttk.Frame(main_frame, style="Input.TFrame", padding="10")
        input_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
        input_frame.grid_columnconfigure(0, weight=1)
        
        # Question input with custom styling
        self.question_input = ttk.Entry(
            input_frame,
            font=("Helvetica", 12),
            style="Custom.TEntry"
        )
        self.question_input.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.question_input.bind("<Return>", self.send_message)
        
        # Send button with custom styling
        send_button = ttk.Button(
            input_frame,
            text="Send",
            style="Send.TButton",
            command=self.send_message
        )
        send_button.grid(row=0, column=1)
        
        # Welcome message
        self.display_bot_message("👋 Hello! I'm your FAQ Assistant. How can I help you today?")
        
    def create_message_bubble(self, message, is_user=False):
        """Create a visually appealing message bubble"""
        tag = "user_message" if is_user else "bot_message"
        bubble_color = self.colors['user_bubble'] if is_user else self.colors['bot_bubble']
        prefix = "You: " if is_user else "🤖 Bot: "
        
        # Create bubble-like message
        bubble = f"\n{prefix}{message}\n"
        
        return bubble, tag
        
    def display_bot_message(self, message):
        """Display a message from the chatbot"""
        self.chat_display.config(state=tk.NORMAL)
        bubble, tag = self.create_message_bubble(message, is_user=False)
        self.chat_display.insert(tk.END, bubble, tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
    def display_user_message(self, message):
        """Display a message from the user"""
        self.chat_display.config(state=tk.NORMAL)
        bubble, tag = self.create_message_bubble(message, is_user=True)
        self.chat_display.insert(tk.END, bubble, tag)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
    def send_message(self, event=None):
        """Process and send user message"""
        message = self.question_input.get().strip()
        if not message:
            return
            
        # Clear input field
        self.question_input.delete(0, tk.END)
        
        # Display user message
        self.display_user_message(message)
        
        # Get and display bot response with typing simulation
        self.root.after(500, lambda: self.simulate_typing())
        response = self.chatbot.get_response(message)
        self.root.after(1500, lambda: self.display_bot_message(response))
        
    def simulate_typing(self):
        """Simulate bot typing effect"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "\n🤖 Bot is typing...\n", "bot_message")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
    def run(self):
        """Start the GUI application"""
        # Set window background
        self.root.configure(bg=self.colors['bg'])
        self.root.mainloop()

if __name__ == "__main__":
    gui = ChatbotGUI()
    gui.run() 