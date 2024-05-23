import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 11
Questions = {
    "What's my Full Name": 
        ["Antonio Legrier", "Anthony Legrier", "Anton Lagrier", "Antonio Lagraer"],
    "What's my Favorite color": 
        ["Gray", "Blue", "Green", "Red"],
    "What's my Favorite book series":
        ["Overlord", "Mistborn", "Dungeon Born", "Solo Leveling"],
    "What's my Favorite Song":
        ["Location", "Halo", "Touchy Feely Fool", "Happy if you're happy"],
    "What's my Favorite Tv Show":
        ["Yu-gi-oh! GX", "Overlord", "Pokemon", "Yu-gi-oh!"],
    "What did I always want to be when I grew up":
        ["Lawyer", "Doctor", "Teacher", "Your Husband"],
    "What's my least favorite food":
        ["Pancakes", "Stir fry", "Lasagna", "Tuna"],
    "What game do I always play with Ivan":
        ["Tft", "Yu-gi-oh", "Overwatch", "Pokemon'"],
    "What makes me cry":
        ["Thinking about my sister", "Sad movies", "My life", "Depression"],
    "What do I like to doing the most":
        ["Bothering Russ", "Reading", "Criticizing people", "Sleeping"],
    "Who's my favorite person":
        ["Russ", "Myself", "Anyone rich", "AJR"],
}

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternatives in labeled_alternatives.items():
        print(f" {label} {alternatives}")
        
    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
    
    return labeled_alternatives[answer_label]

def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐You got it! ⭐ Thats 1 point")
        print("You do know me ")
        return 1
    else:
        print(f"You should know me better than that ☹️, the answer is {correct_answer!r}, not {answer!r}")
        print("No point for you this time")
        return 0
    
def run_quiz():
    questions = prepare_questions(
        Questions, num_questions=NUM_QUESTIONS_PER_QUIZ
    )
    
    num_correct = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question, alternatives)        
    
    print(f"\nYou got {num_correct} correct out of {len(questions)} questions")

if __name__== "__main__":
    run_quiz()         