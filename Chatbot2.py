# -*- coding: utf-8 -*-
# Chatbot - Chats with the user and loops through three questions 

import random 

# Make a list of questions and comments
questions = ["What are your top 3 favourite books?", "What 3 movies do you think are the best?", "If you could only have 3 foods for the rest of your life, what would they be?"]
comments = ["Wow? Really?", "That's interesting...", "Strange...", "I agree!", "That's nice"]

# Ask for your name
print("Hello! What's your name?") 

# Get name
name = input().strip("!?").capitalize() 

# Reply its very nice to meet you
print("It's very nice to meet you," , name+ ".")

# Loop through the questions 
for question in questions: 
  
    print(question)
  
    # Get first, second and third input
    first = input("First:")
    second = input("Second:")
    third = input("Third:")
    
    # Reply with a random comment
    random_comment = random.choice(comments) 
     
    print(random_comment) 
    
print("Goodbye!")
    
