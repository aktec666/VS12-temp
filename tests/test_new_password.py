import string
from password.new_password import generate_password
import pytest  # нужен для теста с исключением

def test_password_has_valid_characters():
    """Пароль содержит только допустимые символы"""
    password = generate_password(20)
    allowed = string.ascii_letters + string.digits + string.punctuation
    for char in password:
        assert char in allowed

def test_password_correct_length():
    """Пароль имеет правильную длину"""
    password = generate_password(20)
    assert len(password) == 20

def test_passwords_are_different():
    """Два пароля не совпадают"""
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2

def test_empty_password():
    """Пароль длиной 0 — пустая строка"""
    assert generate_password(0) == ""



