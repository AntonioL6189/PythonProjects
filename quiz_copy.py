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
    "What's my Tv Show":
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
    "Bonus Question, Who's my favorite person":
        ["Russ", "Myself", "Anyone rich", "AJR"],
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(Questions))
questions = random.sample(list(Questions.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
        )
    for label, alternative in labeled_alternatives.items():
        print(f" {label} {alternative}")
        
    while True:
        answer_label = input("\nChoice? ").lower()
        if answer_label in labeled_alternatives:
            break
        print(f"Please answer one of {', '.join(labeled_alternatives)}")
            
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        num_correct += 1
        print("⭐You got it! ⭐ Thats 1 point")
        print("You do know me ")
    else:
        print(f"You should know me better than that ☹️, the answer is {correct_answer!r}, not {answer!r}")
        print("No point for you this time")
print(f"\nYou got {num_correct} correct out of {num} questions")  