import webbrowser
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize General Knowledge dictionary
general_knowledge = {
    "prime minister": "The Prime Minister of India is Narendra Modi.",
    "capital of india": "The capital of India is New Delhi.",
    "number of states in india": "There are 28 states in India.",
}

# Dictionary of Indian states and their Chief Ministers
chief_ministers = {
    "andhra pradesh": "Y. S. Jagan Mohan Reddy",
    "arunachal pradesh": "Pema Khandu",
    "assam": "Himanta Biswa Sarma",
    "bihar": "Nitish Kumar",
    "chhattisgarh": "Bhupesh Baghel",
    "goa": "Pramod Sawant",
    "gujarat": "Bhupendra Patel",
    "haryana": "Manohar Lal Khattar",
    "himachal pradesh": "Sukhvinder Singh Sukhu",
    "jharkhand": "Hemant Soren",
    "karnataka": "Siddaramaiah",
    "kerala": "Pinarayi Vijayan",
    "madhya pradesh": "Shivraj Singh Chouhan",
    "maharashtra": "Eknath Shinde",
    "manipur": "N. Biren Singh",
    "meghalaya": "Conrad Sangma",
    "mizoram": "Zoramthanga",
    "nagaland": "Neiphiu Rio",
    "odisha": "Mohan charan Majhi ",
    "punjab": "Bhagwant Mann",
    "rajasthan": "Ashok Gehlot",
    "sikkim": "Prem Singh Tamang",
    "tamil nadu": "M. K. Stalin",
    "telangana": "K. Chandrashekar Rao",
    "tripura": "Manik Saha",
    "uttar pradesh": "Yogi Adityanath",
    "uttarakhand": "Pushkar Singh Dhami",
    "west bengal": "Mamata Banerjee",
    "delhi": "Arvind Kejriwal"  
}

# Dictionary of Indian states and their capitals
state_capitals = {
    "andhra pradesh": "Amaravati",
    "arunachal pradesh": "Itanagar",
    "assam": "Dispur",
    "bihar": "Patna",
    "chhattisgarh": "Raipur",
    "goa": "Panaji",
    "gujarat": "Gandhinagar",
    "haryana": "Chandigarh",
    "himachal pradesh": "Shimla",
    "jharkhand": "Ranchi",
    "karnataka": "Bengaluru",
    "kerala": "Thiruvananthapuram",
    "madhya pradesh": "Bhopal",
    "maharashtra": "Mumbai",
    "manipur": "Imphal",
    "meghalaya": "Shillong",
    "mizoram": "Aizawl",
    "nagaland": "Kohima",
    "odisha": "Bhubaneswar",
    "punjab": "Chandigarh",
    "rajasthan": "Jaipur",
    "sikkim": "Gangtok",
    "tamil nadu": "Chennai",
    "telangana": "Hyderabad",
    "tripura": "Agartala",
    "uttar pradesh": "Lucknow",
    "uttarakhand": "Dehradun",
    "west bengal": "Kolkata",
    "delhi": "New Delhi"  
}

# URLs for popular social media websites
social_media_urls = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "whatsapp": "https://web.whatsapp.com",
    "chatgpt": "https://chat.openai.com",
    "reddit": "https://www.reddit.com",
    "snapchat": "https://www.snapchat.com",
    "pinterest": "https://www.pinterest.com",
    "tumblr": "https://www.tumblr.com",
    "tiktok": "https://www.tiktok.com",
    "spotify": "https://www.spotify.com",
    "quora": "https://www.quora.com",
    "vimeo": "https://www.vimeo.com",
    "discord": "https://discord.com",
    "flickr": "https://www.flickr.com"
    
}

# Function to perform mathematical operations
def perform_math(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    elif operation == "modulo":
        if num2 == 0:
            return "Cannot perform modulo by zero."
        return num1 % num2
    else:
        return "Unknown operation."

# Function to open social media sites
def open_social_media(site):
    if site in social_media_urls:
        speak(f"Opening {site}...")
        webbrowser.open(social_media_urls[site])
    else:
        speak(f"Sorry, I don't have {site} configured.")

# Function to answer general knowledge questions
def answer_gk(question):
    question = question.lower()
    if "prime minister" in question:
        return general_knowledge["prime minister"]
    elif "capital of india" in question:
        return general_knowledge["capital of india"]
    elif "number of states" in question:
        return general_knowledge["number of states in india"]
    elif "capital of odisha" in question:
        return state_capitals["odisha"]
    elif "capital of delhi" in question:
        return state_capitals["delhi"]
    elif "capital of punjab" in question:
        return state_capitals["punjab"]
    elif "capital of" in question:
        for state in state_capitals:
            if state in question:
                return f"The capital of {state.title()} is {state_capitals[state]}."
        return "State not found in the list."
    elif "chief minister" in question:
        for state in chief_ministers:
            if state in question:
                return f"The Chief Minister of {state.title()} is {chief_ministers[state]}."
        return "State not found in the list."
    else:
        return "I'm sorry, I don't know the answer to that question."

# Main function
def run_virtual_assistant():
    speak("Welcome to your virtual assistant. What can I do for you  !")
    while True:
        print("\nOptions:")
        print("1. Perform a mathematical operation (add, subtract, multiply, divide, modulo)")
        print("2. Open social media website")
        print("3. Answer general knowledge question")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Perform a mathematical operation
            operation = input("Enter the operation (add, subtract, multiply, divide, modulo): ").strip().lower()
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = perform_math(operation, num1, num2)
                speak(f"The result is {result}")
                print(f"The result is: {result}")
            except ValueError:
                speak("Invalid input. Please enter numeric values.")
                print("Invalid input. Please enter numeric values.")

        elif choice == '2':
            # Open a social media site
            site = input("Enter the name of the social media site to open (e.g., youtube, google, instagram): ").strip().lower()
            open_social_media(site)

        elif choice == '3':
            # Answer a general knowledge question
            question = input("Ask your general knowledge question (e.g., What is the capital of Odisha, or Who is the Chief Minister of Punjab?): ").strip().lower()
            answer = answer_gk(question)
            speak(answer)
            print(answer)

        elif choice == '4':
            # Exit
            speak("Goodbye!")
            print("Goodbye!")
            break

        else:
            speak("Invalid choice. Please choose an option between 1 and 4.")
            print("Invalid choice. Please choose an option between 1 and 4.")

# Run the assistant
if __name__ == "__main__":
    run_virtual_assistant()
