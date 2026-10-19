Q = ['1. What time is it?','2. Is it time?']
A = [['cat', 'fire'], ['mouse', 'trap']]
S = []

for i in range(len(Q)):
    print(Q[i])
    M = input(": ").strip().lower()
    S.append(M)
    if all(word in M for word in A[i]):
        print("Correct")
    else:
        print("Never")
