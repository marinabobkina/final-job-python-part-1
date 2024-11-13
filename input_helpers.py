import main
import user_info as ui
import bank_info as bi

"""Вспомогательные функции для ввода данных."""
def submenu_second(name,
                   age,
                   phone,
                   email,
                   postcode,
                   post_address,
                   info,
                   id_owner,
                   id_taxpayer,
                   account_number,
                   bank_name,
                   id_bank,
                   cor_account):
    """Реализация работы подменю 2: вывод информации."""

    while True:
        print(main.separation())
        print('ВЫВЕСТИ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Вся информация')
        print('0 - Назад')

        option2 = int(input('Введите номер пункта меню: '))

        if option2 == 0:
            print(main.separation())
            break

        if option2 == 1:
            ui.personal_info_user(name, age, phone, email, postcode, post_address, info)

        elif option2 == 2:
            ui.personal_info_user(name, age, phone, email, postcode, post_address, info)
            bi.bank_info_user(id_owner, id_taxpayer, account_number, bank_name, id_bank, cor_account)

        else:
            print('Введите корректный пункт меню')


def submenu_first(name,
                  age,
                  phone,
                  email,
                  postcode,
                  post_address,
                  info,
                  id_owner,
                  id_taxpayer,
                  account_number,
                  bank_name,
                  id_bank,
                  cor_account):
    """Реализация работы подменю 1: ввод и редактирование данных."""

    while True:
        print(main.separation())
        print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
        print('1 - Личная информация')
        print('2 - Информация о предпринимателе')
        print('0 - Назад')

        option2 = int(input('Введите номер пункта меню: '))

        if option2 == 1:
            name_filled, age_filled, phone_filled, email_filled, postcode_filled, post_address_filled, info_filled = ui.personal_info_input()
            name = name_filled
            age = age_filled
            phone = phone_filled
            email = email_filled
            postcode = postcode_filled
            post_address = post_address_filled
            info = info_filled

        elif option2 == 2:
            id_owner_filled, id_taxpayer_filled, account_number_filled, bank_name_filled, id_bank_filled, cor_account_filled = bi.bank_info_input()
            id_owner = id_owner_filled
            id_taxpayer = id_taxpayer_filled
            account_number = account_number_filled
            bank_name = bank_name_filled
            id_bank = id_bank_filled
            cor_account = cor_account_filled

        elif option2 == 0:
            print(main.separation())
            return (
            name, age, phone, email, postcode, post_address, info, id_owner, id_taxpayer, account_number, bank_name,
            id_bank, cor_account)
            break

        else:
            print('Введите корректный пункт меню')