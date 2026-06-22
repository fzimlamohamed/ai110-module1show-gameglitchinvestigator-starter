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

def test_string_vs_int_comparison_single_digit_vs_double():
    # Bug fix: string comparison would say "9" > "10" (lexicographic)
    # but numeric comparison correctly says 9 < 10
    outcome, message = check_guess(9, "10")
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"

def test_string_vs_int_comparison_double_vs_single():
    # Bug fix: string comparison would say "100" < "2" (lexicographic)
    # but numeric comparison correctly says 100 > 2
    outcome, message = check_guess(100, "2")
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"

def test_string_vs_int_comparison_equal():
    # When passed as different types but equal values
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"
