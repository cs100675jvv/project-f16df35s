from _function.format_table import format_table

def print_help():
    """
    Prints the help menu with a list of available commands and their descriptions.
    """
    headers = ["Command", "Arguments", "Command description"]

    commands = [
        ["help", "-", "Вивід допомоги по командам бота."],
        ["hello", "-", "Надіслати привітання від бота."],
        ["save", "-", "Збереження даних в нешифрованому вигляді."],
        ["save_secure", "-", "Збереження даних в зашифрованому вигляді. Потребує введення пароля."],
        ["load", "-", "Завантаження даних, збережених в нешифрованому вигляді."],
        ["load_secure", "-", "Завантаження даних, збережених в зашифрованому вигляді. Потребує введення пароля."],
        ["add", "[name] [phone]", "Додати новий контакт з іменем та номером телефону або номер телефону до існуючого контакту. Можна додати кілька номерів."],
        ["change", "[name] [old phone] [new phone]", "Змінити номер телефону для вказаного контакту."],
        ["delete", "[name]", "Видалення вказаного контакту."],
        ["show-phone", "[name]", "Показати номери телефонів для вказаного контакту."],
        ["all", "-", "Показати всі контакти в адресній книзі."],
        ["add-birthday", "[name] [date of birth]", "Додати дату народження для вказаного контакту."],
        ["change-birthday", "[name]", "Змінити день народження для контакта."],
        ["show-birthday", "[name]", "Показати дату народження для вказаного контакту."],
        ["birthdays", "-", "Показати дні народження, які наближаються протягом наступного тижня."],
        ["add-email", "[name] [email]", "Додати email до контакту. Може бути кілька емейлів."],
        ["change-email", "[name] [old-email] [new-email]", "Змінити email для вказаного контакту."],
        ["add-address", "[name] [address]", "Додати адресу до контакту."],
        ["change-address", "[name] [address]", "Змінити адресу для вказаного контакту."],
        ["search", "[string]", "Пошук в контактах по строці"],
        ["add-note", "[name]", "Відкрити редактор для тексту нотатки. Введіть :end для завершення редагування. Після цього нотатка буде додана."],
        ["find_note", "[string]",  "Знайти нотаток по строці."],
        ["delete_note", "[ID]", "Видалити нототок."],
        ["show_note", "[ID]", "Показати нотаток."],
        ["edit_note", "[ID]", "Редагувати нотаток."],
        ["list-notes", "-", "Показати список всіх нотаток [ID and DATE]."],
        ["close або exit", "-", "Закрити програму."]
    ]

    col_widths = [15, 30, 70]
    return print(format_table(headers, commands, col_widths))
