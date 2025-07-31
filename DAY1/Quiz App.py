# Simple Python Quiz App

# List of quiz questions (each with a question, options, and correct answer)
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Paris", "c) Rome", "d) Madrid"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"],
        "answer": "c"
    },        
    {
        "question": "What is the output of 3 * 2 + 1?",
        "options": ["a) 7", "b) 9", "c) 5", "d) 6"],
        "answer": "a"
    }
]

score = 0  # To track user score

print("Welcome to the Python Quiz App!\n")

# Loop through each question
for i, q in enumerate(quiz, 1):
    print(f"Q{i}: {q['question']}")
    for option in q['options']:
        print(option)
    
    user_answer = input("Your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. The correct answer is '{q['answer']}'\n")

# Show final score
print(f"Quiz Completed! You scored {score} out of {len(quiz)}.")