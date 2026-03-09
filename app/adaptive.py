def update_ability(current_ability, difficulty, correct):

    if correct:
        current_ability += 0.1
    else:
        current_ability -= 0.1

    # keep ability between 0.1 and 1.0
    current_ability = max(0.1, min(1.0, current_ability))

    return round(current_ability, 2)