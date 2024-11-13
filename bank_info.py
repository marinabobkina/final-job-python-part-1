import validation as val


"""Функции для работы с банковской информацией."""
def bank_info_user(id_owner_parameter,
                   id_taxpayer_parameter,
                   account_number_parameter,
                   bank_name_parameter,
                   id_bank_parameter,
                   cor_account_parameter):
    """Вывод банковских данных."""

    print('\nИнформация о предпринимателе')
    print('ОГРНИП:', id_owner_parameter)
    print('ИНН:', id_taxpayer_parameter)
    print('Банковские реквизиты')
    print('Р/с:', account_number_parameter)
    print('Банк:', bank_name_parameter)
    print('БИК:', id_bank_parameter)
    print('К/с:', cor_account_parameter)

def bank_info_input():
    """Ввод банковских данных."""

    id_owner_input = val.ciphers_quantity_check('Введите ОГРНИП: ', 'ОГРНИП', 15)
    id_taxpayer_input = int(input('Введите ИНН: '))
    account_number_input = val.ciphers_quantity_check('Введите расчётный счёт: ', 'Расчетный счёт', 20)
    bank_name_input = input('Введите название банка: ')
    id_bank_input = int(input('Введите БИК: '))
    cor_account_input = int(input('Введите корреспондентский счёт: '))
    return (id_owner_input, id_taxpayer_input, account_number_input, bank_name_input, id_bank_input, cor_account_input)