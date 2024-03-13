def find_runner_up_score(n, scores):
    scores_set = set(scores)  # Convert scores to a set to remove duplicates
    if len(scores_set) < 2:
        return "No runner-up score exists."
    else:
        scores_set.remove(max(scores_set))  # Remove the maximum score
        return max(scores_set)  # Return the maximum score from the remaining set


def main():
    n = int(input("Enter the number of participants: "))
    scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

    runner_up_score = find_runner_up_score(n, scores)
    print("Runner-Up Score:")
    print(runner_up_score)


if __name__ == "__main__":
    main()
