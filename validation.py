"""Функции для валидации данных (проверка возраста, почтового индекса, номера телефона и т.д.)."""
def count_symbols(text):
    """Postcode and phone input check: symbols accumulation and summing of their quantity"""

    checked_text = ''
    count_character = 0
    for character in text:
        if '0' <= character <= '9':
            checked_text += character
            count_character += 1
    return (count_character, checked_text)


def postcode_check(request_postcode):
    """Postcode validation"""

    user_postcode = input(request_postcode)
    count, postcode_checked = count_symbols(user_postcode)
    while count != 6:
        print('Ошибка ввода. В почтовом индексе должно быть шесть цифр.')
        user_postcode = input(request_postcode)
        count, postcode_checked = count_symbols(user_postcode)
    return postcode_checked


def phone_check(request_phone):
    """Phone validation"""

    user_phone = input(request_phone)
    count, phone_checked = count_symbols(user_phone)
    while True:
        if count != 11 or int(phone_checked) // 10 ** 10 != 7:
            print('Ошибка ввода. В номере телефона должно быть 11 цифр.')
            print('Первая цифра должна быть "7".')
            user_phone = input(request_phone)
            count, phone_checked = count_symbols(user_phone)
        else:
            return (f'+{phone_checked}')


def age_check(request_age):
    """Age validation"""

    user_age = int(input(request_age))
    while user_age <= 0:
            print('Возраст должен быть положительным')
            user_age = int(input(request_age))
    return user_age


def count_ciphers(number):
    """Counting of digits in a number"""

    count = 0
    while number:
        number //= 10
        count += 1
    return count


def ciphers_quantity_check(info_request, name, ciphers_quantity):
    """Check the number of digits"""

    user_info = int(input(info_request))
    count = count_ciphers(user_info)
    if count != ciphers_quantity:
        print(f'Ошибка ввода. В поле {name} должно быть {ciphers_quantity} цифр.')
        user_info = int(input(info_request))
        count = count_ciphers(user_info)
    return user_info