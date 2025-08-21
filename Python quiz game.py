print("Welcome to the Python Quiz Game! 🐍")
score = 0

questions = {
    "What is the capital of France? ": "paris",
    "What is 5 + 7? ": "12",
    "Who created Python? ": "guido van rossum",
    "What is the square root of 64? ": "8",
    "Which keyword is used to define a function in Python? ": "def"
}

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer is", answer)

print(f"\nYou got {score} out of {len(questions)} correct!")
