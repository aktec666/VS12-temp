import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
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
