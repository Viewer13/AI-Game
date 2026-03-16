#FIX: Added tests for game logic functions, including checking guesses and attempt limits for hard mode. These tests ensure that the core game mechanics are functioning correctly and provide feedback on whether guesses are correct, too high, or too low, as well as enforcing attempt limits based on difficulty level thanks to Copilot Agent mode.
from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hard_mode_attempt_limit():
    from logic_utils import is_attempt_allowed
    difficulty = "Hard"
    # For hard mode, limit is 5 attempts
    # After 4 attempts, should still allow the 5th
    assert is_attempt_allowed(4, difficulty) == True
    # After 5 attempts, should not allow the 6th
    assert is_attempt_allowed(5, difficulty) == False
