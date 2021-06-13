
def validate(guess, word):
    correct = 0
    misplaced = 0
    valid = True
    match = False
    if len(guess) != 4 or len(set(guess)) != 4:
        response = {
            "valid": False,
            "guess": guess
        }
        return response
    guess = guess.lower()
    for x in guess:
        if x not in "qwertyuioplkjhgfdsazxcvbnm":
            response = {
                "valid": False,
                "guess": guess
            }
            return response  
    common = len(set(word).intersection(set(guess)))
    for x in range(4):
        if word[x] == guess[x]:
            correct += 1
    misplaced = common - correct
    if guess == word:
        match = True
    response = {
        "valid": True,
        "misplaced": misplaced,
        "correct": correct,
        "match": match,
        "guess": guess
    }
    return response

