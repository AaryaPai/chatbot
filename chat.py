import random

# Define a function to generate responses based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase
    
    # Define some predefined patterns and responses
    greetings = ["hello", "hi", "hey", "howdy"]
    farewells = ["bye", "goodbye", "see you later"]
    questions = ["how are you?", "what's up?", "how's it going?"]
    
    # Responses based on patterns
    
    if user_input in greetings:
        return "Hello! How can I assist you today?"
    elif user_input.startswith("how are you"):
        return "I'm well, what about you!"
    elif user_input in farewells:
        return "Goodbye! Have a great day!"
    elif any(question in user_input for question in questions):
        return "I'm doing well, thank you! How about you?"
    elif user_input.endswith("?"):
        return "you can try asking google that"
    else:
        return "alright!"

# Example conversation loop
print("Welcome! Type 'exit' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        response = chatbot_response(user_input)
        print("Chatbot:", response)
