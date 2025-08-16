import random

quiz = {
    "1. What does 'CPU' stand for?": {
        "answer": "Central Processing Unit",
        "options": ["Central Processing Unit", "Computer Primary Unit", "Central Peripheral Unit", "Control Program Unit"]
    },
    "2. What does 'RAM' stand for in computing?": {
        "answer": "Random Access Memory",
        "options": ["Readily Accessible Memory", "Random Access Memory", "Rapid Allocation Memory", "Run Access Module"]
    },
    "3. What is the value of 2 to the power of 5?": {
        "answer": "32",
        "options": ["16", "32", "64", "25"]
    },
    "4. Which language is primarily used for web page structure?": {
        "answer": "HTML",
        "options": ["HTML", "CSS", "JavaScript", "Python"]
    },
    "5. What does 'IP' stand for in networking?": {
        "answer": "Internet Protocol",
        "options": ["Internet Protocol", "Internal Process", "Internet Procedure", "Input Protocol"]
    },
    "6. What is the output of: 3 * 3 + 1?": {
        "answer": "10",
        "options": ["9", "10", "12", "8"]
    },
    "7. What port does HTTP use by default?": {
        "answer": "80",
        "options": ["443", "21", "80", "8080"]
    },
    "8. What does the 'try' keyword do in Python?": {
        "answer": "Handles exceptions",
        "options": ["Starts a loop", "Handles exceptions", "Defines a function", "Creates a class"]
    },
    "9. Which data structure uses FIFO (First In First Out)?": {
        "answer": "Queue",
        "options": ["Stack", "Queue", "Array", "Dictionary"]
    },
    "10. What is the full form of 'SQL'?": {
        "answer": "Structured Query Language",
        "options": ["Structured Quick Logic", "Strong Query Language", "Structured Query Language", "Sequential Query Layer"]
    }
}

score = 0

print("Welcome to the Technical Quiz!")
print("Answer the following questions by typing A, B, C, or D.")
print("You can also type 'skip' to move to the next question.\n")

for question, data in quiz.items():
    print(question)
    
    options = data["options"]
    random.shuffle(options)
    option_map = dict(zip(["A", "B", "C", "D"], options))
    
    for key in option_map:
        print(f"{key}. {option_map[key]}")

    while True:
        answer = input("Your answer (A/B/C/D or 'skip'): ").strip().upper()
        
        if answer == "SKIP":
            print("Question skipped.\n")
            break
        elif answer in option_map:
            if option_map[answer].lower() == data["answer"].lower():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong! The correct answer is:", data["answer"], "\n")
            break
        else:
            print("Invalid input. Please enter A, B, C, D or 'skip'.\n")

print("Quiz Over!")
print("Your final score is:", score, "/ 10")
