quiz = {
    "1. What does 'CPU' stand for?": "Central Processing Unit",
    "2. What does 'RAM' stand for in computing?": "Random Access Memory",
    "3. What is the value of 2 to the power of 5?": "32",
    "4. Which language is primarily used for web page structure?": "HTML",
    "5. What does 'IP' stand for in networking?": "Internet Protocol",
    "6. What is the output of: 3 * 3 + 1?": "10",
    "7. What port does HTTP use by default?": "80",
    "8. What does the 'try' keyword do in Python?": "Handles exceptions",
    "9. Which data structure uses FIFO (First In First Out)?": "Queue",
    "10. What is the full form of 'SQL'?": "Structured Query Language"
}

score = 0

print("Welcome to the Technical Quiz! \n Answer the following questions:\n")

for question in quiz:
    print(question)
    answer = input("Your answer: ")
    
    if answer.strip().lower() == quiz[question].lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! The correct answer is:", quiz[question], "\n")

print("Quiz Over!")
print("Your final score is:", score, "/ 10")
