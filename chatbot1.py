dataset = {
    "hello": "Hello! Welcome to Tejas Mobile Shop.",
    "hi": "Hi! How can I help you?",
    "mobile": "We have Samsung, Vivo, Oppo, OnePlus and iPhone mobiles.",
    "price": "Mobile prices start from ₹7000.",
    "offer": "Today we have 10% discount on selected mobiles.",
    "location": "Our shop is located in Pune.",
    "contact": "Call us on 9876543210.",
    "timing": "Our shop opens from 10 AM to 9 PM.",
    "laptop": "We also sell HP, Dell and Lenovo laptops.",
    "accessories": "We have chargers, earphones, covers and smart watches.",
    "payment": "We accept Cash, UPI, Debit Card and Credit Card.",
    "emi": "EMI option is available on selected mobiles.",
    "repair": "Yes, mobile repair service is available.",
    "warranty": "All mobiles come with company warranty.",
    "delivery": "Home delivery is available in Pune city.",
    "exchange": "Old mobile exchange option is available.",
    "best": "Samsung and iPhone are our best-selling mobiles.",
    "discount": "Student discount is available on some products.",
    "5g": "Yes, we have latest 5G smartphones.",
    "thank you": "Welcome! Visit again.",
    "bye": "Thank you for visiting our shop."
}

print("===== MOBILE SHOP CHATBOT =====")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    words = user.split()

    found = False

    for key in dataset:

        if key in words or key == user:

            print("Bot:", dataset[key])
            found = True
            break

    if found == False:
        print("Bot: Sorry, I don't understand.")

    if user == "bye":
        break




"""""Title
Simple Mobile Shop Chatbot Using Python
Objective
To create a simple chatbot program in Python that automatically responds to customer queries related to a mobile shop using predefined questions and answers.
Theory
A chatbot is a software application that communicates with users like a human conversation. In this program, a simple rule-based chatbot is created using Python. The chatbot works by checking user input and matching it with predefined keywords stored in a dictionary. When the user enters a message, the chatbot searches for related keywords and gives the corresponding response. This type of chatbot does not use Artificial Intelligence or Machine Learning; instead, it works using simple keyword matching logic.
The program uses a Python dictionary called dataset to store questions and responses. Each keyword acts as a key, and its reply acts as a value. The chatbot continuously accepts user input using an infinite loop (while True). The input is converted into lowercase using .lower() so that comparison becomes easier and case-insensitive. Then the input sentence is divided into words using .split().
After splitting the sentence, the chatbot checks whether any keyword from the dataset exists in the user message. If a keyword matches, the chatbot prints the corresponding response. If no keyword is found, it displays a default message saying it does not understand the query. The chatbot continues running until the user types "bye", after which the loop stops using the break statement.
Important Points


Dictionary


Stores chatbot questions and answers.


Works as chatbot knowledge base.




Input Function


Takes message from user.




Lowercase Conversion


.lower() converts text into lowercase.


Helps in easy matching.




Split Function


.split() divides sentence into words.




Loop


while True keeps chatbot running continuously.




Keyword Matching


Searches keywords in user input.




Conditional Statements


if condition checks whether keyword exists.




Break Statement


Stops chatbot when user enters "bye".




Rule-Based Chatbot


Gives replies only from predefined dataset.




Simple AI Concept




Demonstrates basic human-computer interaction.


Algorithm


Create a dictionary containing chatbot questions and answers.


Display welcome message.


Take user input.


Convert input into lowercase.


Split the sentence into words.


Check every keyword in dataset.


If keyword matches:


Display corresponding response.




Otherwise:


Display default error message.




If user enters "bye":


Stop program using break.




End program.


Conclusion
This program demonstrates a simple rule-based chatbot using Python. It uses dictionary data, loops, and keyword matching to provide automatic responses to users. The project helps beginners understand the basic working of chatbots and simple Artificial Intelligence concepts."""