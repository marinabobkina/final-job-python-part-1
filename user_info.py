import main
import input_helpers as ih
import validation as val


"""Функции для работы с личной информацией пользователя."""
def personal_info_user(name_parameter,
                       age_parameter,
                       phone_parameter,
                       email_parameter,
                       postcode_parameter,
                       postaddress_parameter,
                       info_parameter):
    """Вывод личных данных."""

    print(main.separation())
    print('Имя:    ', name_parameter)

    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс:', postcode_parameter)
    print('Адрес:', postaddress_parameter)
    if info_parameter:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


def personal_info_input():
    """Ввод личных данных."""

    name_input = input('Введите имя: ')
    age_input = val.age_check('Введите возраст: ')
    phone_input = val.phone_check('Введите номер телефона (+7ХХХХХХХХХХ): ')
    email_input = input('Введите адрес электронной почты: ')
    postcode_input = val.postcode_check('Введите почтовый индекс: ')
    post_address_input = input('Введите почтовый адрес (без индекса): ')
    info_input = input('Введите дополнительную информацию: ')
    print('')
    return (name_input, age_input, phone_input, email_input, postcode_input, post_address_input, info_input)
