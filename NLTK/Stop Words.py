import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Your Stopwords function (modified to return the filtered list)
def Stopwords(user_input):
    Stop_Words = set(stopwords.words('english'))
    words = word_tokenize(user_input)
    word_list = []
    for w in words:
        if w.lower() not in Stop_Words:  # compare lowercase for consistency
            word_list.append(w)
    print("Filtered tokens:", word_list)  # For debugging
    return word_list

# Helper function to check if all tokens of an expected phrase are in the user's filtered tokens.
def phrase_in_tokens(phrase, tokens):
    # Tokenize the expected phrase.
    phrase_tokens = word_tokenize(phrase.lower())
    # Convert tokens from user's answer to lower-case.
    tokens_lower = [token.lower() for token in tokens]
    # Return True only if every word from the phrase is present in the filtered tokens.
    return all(pt in tokens_lower for pt in phrase_tokens)

# Questions and their expected answers
question_1c_and_1d = [
    (
        "1c. Describe how accepted style conventions have been used to make the code in \nFigure 1 more readable. (3 Marks)",
        ['sensible naming styles', 'sensible naming style', 'pep 8', 'pep8', 'conventions'],
        ['camelcase', 'snakecase', 'pascalcase', 'camel case', 'snake case', 'pascal case', 'meaningful identifiers', 'spacing'],
        ['convey the purpose of each variable', 'variable', 'clarify code structure', 'start and end of words']
    ),
    (
        "1d. Explain why line 4 in Figure 1 is needed. (3 Marks)",
        ['input is a string'],
        ['converted into an integer', 'changed into an int'],
        ['used in calculations', 'avoid runtime errors', 'avoid errors']
    )
]

marks = 0  # Initialize the marks

# Evaluate each question
for Q in question_1c_and_1d:
    print(Q[0])
    user_input = input("\nEnter your answer: ")
    
    # Obtain the filtered tokens by removing stop words
    filtered_tokens = Stopwords(user_input)
    
    # Check each expected answer part using our helper function
    answer1_match = any(phrase_in_tokens(phrase, filtered_tokens) for phrase in Q[1])
    answer2_match = any(phrase_in_tokens(phrase, filtered_tokens) for phrase in Q[2])
    answer3_match = any(phrase_in_tokens(phrase, filtered_tokens) for phrase in Q[3])
    
    # Award marks based on matches
    if answer1_match and answer2_match and answer3_match:
        print("\nCorrect")
        marks += 3
        print("Validated tokens:", filtered_tokens)
    elif (answer1_match and answer2_match) or (answer2_match and answer3_match):
        print("\nGood job, 2 marks")
        marks += 2
    elif answer1_match or answer2_match or answer3_match:
        print("\nAlmost, you got 1 mark")
        marks += 1
    else:
        print("\nIncorrect")

print("Total marks:", marks)
