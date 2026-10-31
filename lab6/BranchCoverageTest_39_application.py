import pytest
from password_policy import check_password, strength, suggest_fix


# Check password validation

def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


def test_password_too_short():
    assert "too short" in check_password("Ab1!")


def test_password_too_long():
    assert "too long" in check_password("A" * 65)


def test_common_password():
    assert "common" in check_password("PASSWORD")


def test_no_uppercase():
    assert "no uppercase" in check_password("abcdef1!")


def test_no_lowercase():
    assert "no lowercase" in check_password("ABCDEF1!")


def test_no_digit():
    assert "no digit" in check_password("Abcdefgh!")


def test_no_special():
    assert "no special" in check_password("Abcdefg1")


def test_multiple_issues():
    issues = check_password("abc")
    assert len(issues) >= 3


# Strength tests

def test_strong_password():
    assert strength("Abcdefgh12345!") == "strong"


def test_weak_password():
    assert strength("abcdefg!") == "weak"


def test_very_weak_password():
    assert strength("abc") == "very weak"


# Suggestion tests

def test_suggest_none():
    assert suggest_fix([]) == "none needed"


def test_suggest_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_uppercase():
    assert suggest_fix(["no uppercase"]) == "add uppercase"


def test_suggest_shortening():
    assert suggest_fix(["too long"]) == "shorten it"