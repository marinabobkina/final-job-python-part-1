import input_helpers as ih


def separation():
    SEPARATOR = '------------------------------------------'
    return SEPARATOR


def main_menu():
    """Реализация работы главного меню: навигация."""

    # User data.
    name = name_filled = ''
    age = age_filled = 0
    phone = phone_filled = ''
    email = email_filled = ''
    postcode = postcode_filled = ''
    post_address = post_address_filled = ''
    info = info_filled = ''

    # Bank data.
    id_owner = id_owner_filled = 0
    id_taxpayer = id_taxpayer_filled = 0
    account_number = account_number_filled = 0
    bank_name = bank_name_filled = ''
    id_bank = id_bank_filled = 0
    cor_account = cor_account_filled = 0

    while True:
        separation()
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Ввести или обновить информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить работу')

        option = int(input('Введите номер пункта меню: '))

        if option == 0:
            print('РАБОТА ЗАВЕРШЕНА.')
            break

        if option == 1:
            (name_filled, age_filled, phone_filled, email_filled, postcode_filled, post_address_filled, info_filled,
             id_owner_filled, id_taxpayer_filled, account_number_filled, bank_name_filled, id_bank_filled,
             cor_account_filled) = ih.submenu_first(name, age, phone, email, postcode, post_address, info, id_owner,
                                                    id_taxpayer, account_number, bank_name, id_bank, cor_account)
            name = name_filled
            age = age_filled
            phone = phone_filled
            email = email_filled
            postcode = postcode_filled
            post_address = post_address_filled
            info = info_filled
            id_owner = id_owner_filled
            id_taxpayer = id_taxpayer_filled
            account_number = account_number_filled
            bank_name = bank_name_filled
            id_bank = id_bank_filled
            cor_account = cor_account_filled

        elif option == 2:
            ih.submenu_second(name, age, phone, email, postcode, post_address, info, id_owner, id_taxpayer,
                              account_number, bank_name, id_bank, cor_account)

        else:
            print('Введите корректный пункт меню')


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')
print(separation())
main_menu()