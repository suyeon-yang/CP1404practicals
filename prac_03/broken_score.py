def main():
    score = float(input("Enter score: "))
    print(determine_score_status(score))


def determine_score_status(score):
    """Determine score status, give comments."""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


main()


