import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
from faq_data import faqs

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class FAQChatbot:
    def __init__(self):
        self.faqs = faqs
        self.vectorizer = TfidfVectorizer(stop_words='english')
        # Prepare the questions for vectorization
        questions = [faq['question'] for faq in self.faqs]
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def preprocess_text(self, text):
        """Preprocess the input text by removing punctuation and converting to lowercase."""
        # Remove punctuation and convert to lowercase
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.lower()

    def find_best_match(self, user_question):
        """Find the most similar question in the FAQ database."""
        # Preprocess and vectorize the user's question
        processed_question = self.preprocess_text(user_question)
        question_vector = self.vectorizer.transform([processed_question])

        # Calculate similarity with all FAQ questions
        similarities = cosine_similarity(question_vector, self.question_vectors)
        best_match_index = np.argmax(similarities)
        similarity_score = similarities[0][best_match_index]

        return best_match_index, similarity_score

    def get_response(self, user_question):
        """Get the most appropriate response for the user's question."""
        best_match_index, similarity_score = self.find_best_match(user_question)

        # If the similarity is too low, return a default response
        if similarity_score < 0.3:
            return ("I'm sorry, I don't have a specific answer for that question. "
                   "Please try rephrasing your question or contact customer support for more help.")

        return self.faqs[best_match_index]['answer']

    def run(self):
        """Run the chatbot interface."""
        print("FAQ Chatbot: Hello! I'm here to help answer your questions. Type 'quit' to exit.")
        print("What would you like to know?")

        while True:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nChatbot: Goodbye! Have a great day!")
                break

            if not user_input:
                print("Chatbot: Please ask a question!")
                continue

            response = self.get_response(user_input)
            print(f"\nChatbot: {response}")

if __name__ == "__main__":
    chatbot = FAQChatbot()
    chatbot.run() 