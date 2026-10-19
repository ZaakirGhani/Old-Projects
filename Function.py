def grade_question(questions):
    divider = "-------------------------------"
    score = 0  # Initialize score
    
    for question in questions:
        print(question[0])
        user_input = input(f"{divider}\nEnter your answer: ").strip().lower()
        
        # Check for keyword matches
        answer1_match = any(word in user_input for word in question[1])
        answer2_match = any(word in user_input for word in question[2])
        answer3_match = any(word in user_input for word in question[3])
        answer4_match = any(word in user_input for word in question[4])
        
        # Count how many answers matched
        match_count = sum([answer1_match, answer2_match, answer3_match, answer4_match])
        
        if match_count == 4:
            print(f"{divider}\nCorrect\n")
            score += 4
        elif match_count == 3:
            print(f"{divider}\nGood job, 3 marks\n")
            score += 3
        elif match_count == 2:
            print(f"{divider}\nGood job, 2 marks\n")
            score += 2
        elif match_count == 1:
            print(f"{divider}\nAlmost, you got 1 mark\n")
            score += 1
        else:
            print(f"{divider}\nIncorrect\n")
    
    return score

# Example questions list where:
# question[0] is the question text,
# question[1] to question[4] are lists of keywords for each answer possibility.
questions = [
    ('What is the color of the sky on a clear day?', ['blue'], ['azure'], ['cerulean'], ['sky-blue'])
]

# Call the function and capture the final score outside the function
final_score = grade_question(questions)
print(f"Final Score: {final_score}")
