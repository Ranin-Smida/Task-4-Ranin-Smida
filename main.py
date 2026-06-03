import random

def normalize_answer(text: str) -> str:
    """Normalize user input for reliable comparisons."""
    # Trim, case-normalize, and collapse internal whitespace to stabilize matching.
    return " ".join(text.strip().casefold().split())


def ask_question(prompt: str, accepted_answers: list[str]) -> bool:
    # Loop until we get a non-blank answer to avoid accidental empty input.
    while True:
        raw = input(f"{prompt} ")
        if raw.strip():
            break
        print("Please enter a response (not blank).")

    # Normalize once so the comparison is deterministic.
    cleaned = normalize_answer(raw)
    if cleaned in accepted_answers:
        print("Correct! +1 point.\n")
        return True

    print("Incorrect.\n")
    return False


def main() -> None:
    # Central question bank; each entry defines a prompt and acceptable answers.
    questions = [
        {
            "prompt": "1) What is the capital of France?",
            "answers": ["paris"],
        },
        {
            "prompt": "2) What planet is known as the Red Planet?",
            "answers": ["mars"],
        },
        {
            "prompt": "3) Which ocean is the largest on Earth?",
            "answers": ["pacific", "pacific ocean"],
        },
        {
            "prompt": "4) Who wrote 'Romeo and Juliet'?",
            "answers": ["william shakespeare", "shakespeare"],
        },
        {
            "prompt": "5) What is the chemical symbol for water?",
            "answers": ["h2o"],
        },
        {
            "prompt": "6) How many continents are there on Earth?",
            "answers": ["7", "seven"],
        },
        {
            "prompt": "7) What gas do plants absorb from the atmosphere?",
            "answers": ["carbon dioxide", "co2"],
        },
        {
            "prompt": "8) What is the largest planet in our solar system?",
            "answers": ["jupiter"],
        },
    ]

    # Pre-normalize all answer keys to match the normalization pipeline.
    for q in questions:
        q["answers"] = [normalize_answer(a) for a in q["answers"]]

    # Shuffle to make the quiz feel fresh each run.
    random.shuffle(questions)

    print("Welcome to The General Knowledge Quiz!\n")
    # Score is integer state that increments on each correct answer.
    score = 0
    # Track missed prompts so we can recap at the end.
    incorrect = []

    for q in questions:
        if ask_question(q["prompt"], q["answers"]):
            score += 1
        else:
            incorrect.append(q["prompt"])

    # Calculate final percentage as a user-friendly summary.
    total = len(questions)
    percent = (score / total) * 100

    print("Final Results")
    print("-------------")
    print(f"Score: {score}/{total} ({percent:.0f}%)")
    if incorrect:
        print("Missed questions:")
        for item in incorrect:
            print(f"- {item}")
    else:
        print("Perfect score! Great job!")


if __name__ == "__main__":
    main()
