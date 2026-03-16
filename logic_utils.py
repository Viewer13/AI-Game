#FIX: Refactored game logic functions to be more modular and added attempt limit functionality based on difficulty level. This allows for a more structured and maintainable codebase, making it easier to manage game mechanics and provide a better user experience. The functions now handle parsing guesses, checking outcomes, updating scores, and enforcing attempt limits effectively thanks to Copilot Agent mode.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 100
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 20
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score


def get_attempt_limit(difficulty: str) -> int:
    """Return the attempt limit for a given difficulty."""
    attempt_limit_map = {
        "Easy": 8,
        "Normal": 6,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 8)


def is_attempt_allowed(attempts: int, difficulty: str) -> bool:
    """Check if another attempt is allowed based on current attempts and difficulty."""
    limit = get_attempt_limit(difficulty)
    return attempts < limit
