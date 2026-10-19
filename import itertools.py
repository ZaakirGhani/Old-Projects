import itertools


question_7 = [('Evaluate the effectiveness of top down design when developing this program.(9 marks)',
                   ['always broken down into smaller units', 'the designer can define the requirements of what the program needs to do',
                    'subunits gets less complex as you progress',
                    'tasks and code can be reused again',
                    'saves time','units can be updatable'],
                    ['inflexible decisions','time consuming','testing stubs','testing requires stubs',
                      'modules are very specific','existing components','existing components cannot be used again',
                      'dependent on the bigger picture'],
                      ['breaking down the bigger picture into smaller problems','time consuming and inflexible decisions can slow down progress','use of studs can make the process more complex'])]

question, positives, negatives, conclusions = question_7[0]

# Limit sizes for practicality (e.g. choose 2 to 4 positives/negatives for realistic arguments)
min_args, max_args = 2, 4

# Get all combinations of positives and negatives within those bounds
positive_combos = []
for r in range(min_args, max_args + 1):
    positive_combos.extend(itertools.combinations(positives, r))

negative_combos = []
for r in range(min_args, max_args + 1):
    negative_combos.extend(itertools.combinations(negatives, r))

# Now combine them with each conclusion
full_combinations = []
for pos in positive_combos:
    for neg in negative_combos:
        for concl in conclusions:
            full_combinations.append({
                "positives": pos,
                "negatives": neg,
                "conclusion": concl
            })

# Print a few examples
for i, combo in enumerate(full_combinations[:5]):  # Just showing first 5 to avoid overload
    print(f"\n--- Combination {i+1} ---")
    print("Positives:")
    for p in combo['positives']:
        print(f" - {p}")
    print("Negatives:")
    for n in combo['negatives']:
        print(f" - {n}")
    print("Conclusion:")
    print(f" => {combo['conclusion']}")
