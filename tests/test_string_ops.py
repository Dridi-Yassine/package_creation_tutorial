from package_creation_tutorial.string_ops import (
    capitalize_words,
    count_vowels,
    reverse_string,
)


def test_reverse_string() -> None:
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"


def test_count_vowels() -> None:
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5


def test_capitalize_words() -> None:
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming") == "Python Programming"
