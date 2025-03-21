import random

# Define your updated details
user_details = {
    "name": "Arunachalam K",
    "age": "21",
    "interests": ["HTML", "CSS", "JavaScript", "Python", "Web Development", "Problem Solving"],
    "study_field": "Computer Science",
    "university": "XYZ University",
    "hobbies": ["Coding", "Reading", "Traveling"],
    "skills": ["Web Development", "Software Engineering", "Data Structures", "Python Programming"],
    "dream_job": "Software Developer",
    "internships": ["Web Development Internship Codebind Technologies", "Full Stack Developer Internship Itinfostar."],
    "projects": ["E-commerce website Using Front-end Development", "Portfolio website using HTML, CSS, JavaScript"],
    "mindset": "I have a strong problem-solving mindset, always focusing on breaking down problems into manageable steps."
}

def chatbot_response(user_input):
    responses = {
        "hi": f"Hello! I am {user_details['name']}. How can I assist you today?",
        "hello": f"Hi there! I'm {user_details['name']}. What can I do for you?",
        "bye": "Goodbye! Take care and feel free to return anytime!",
        "how are you": "I'm just an AI, but I'm here to help you with anything!",
        "thanks": "You're welcome! I'm always here to help.",
        "what's your name": f"My name is {user_details['name']}.",
        "how old are you": f"I am {user_details['age']} years old.",
        "what are your interests": f"I am interested in {', '.join(user_details['interests'])}.",
        "what's your field of study": f"I am studying {user_details['study_field']}.",
        "where do you study": f"I study at {user_details['university']}.",
        "what are your hobbies": f"My hobbies include {', '.join(user_details['hobbies'])}.",
        "what skills do you have": f"My skills include {', '.join(user_details['skills'])}.",
        "what's your dream job": f"My dream job is to be a {user_details['dream_job']}.",
        "tell me about your internships": f"I have completed two internships: {', '.join(user_details['internships'])}.",
        "what projects have you completed": f"I've worked on several projects, including: {', '.join(user_details['projects'])}.",
        "what's your mindset": f"{user_details['mindset']}",
        "help": "I can help with answering questions about my details, coding, or just general conversation!",
        "tell me something interesting": random.choice([
            "Did you know? The first computer programmer was Ada Lovelace!",
            "Did you know? Python was named after the comedy group Monty Python, not the snake!",
            "Did you know? The first website ever created is still online!"
        ])
    }

    user_input = user_input.lower().strip()
    if user_input == "exit":
        return "Goodbye! Hope to talk to you again soon!"

    return responses.get(user_input, "Sorry, I didn't quite understand that. Can you ask something else?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye! Take care!")
        break
    print("Bot:", chatbot_response(user_input))
