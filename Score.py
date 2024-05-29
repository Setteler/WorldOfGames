def add_score(difficulty):
    points = difficulty*3+5
    try:
        with open('Scores.txt', 'r') as file:
            current_score = int(file.read())
    except :
            current_score = 0
    score = current_score + points
    with open('Scores.txt', 'w') as file:
         file.write(str(score))

