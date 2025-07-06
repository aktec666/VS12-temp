import string
from password.new_password import generate_password
import pytest  # нужен для теста с исключением

def test_password_has_valid_characters():
    """Пароль содержит только допустимые символы"""
    password = generate_password(20)
    allowed = string.ascii_letters + string.digits + string.punctuation
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что при генерации используются только допустимые символы"""
    length = 100
    password = generate_password(length)  # Генерируем длинный пароль для более надежной проверки
    assert len(password) == length

def test_password_dif():
    """Тест, что при генерации используются только допустимые символы"""
    length = 100
    password1 = generate_password(length)  # Генерируем длинный пароль для более надежной проверки
    password2 = generate_password(length)
    assert password1 != password2
"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданнойa
Тест, что два сгенерированных подряд пароля различаются
"""

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



