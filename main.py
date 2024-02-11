import json


# Функция для загрузки данных из файла
def load_data(filename: str) -> list:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


# Функция для сохранения данных в файл
def save_data(data: list, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(data, file)


# Функция для вывода данных постранично
def display_data(data: list, page: int, page_size: int) -> None:
    start = (page - 1) * page_size
    end = start + page_size
    for index, entry in enumerate(data[start:end], start=start+1):
        output_text = (
            f"***************************************\n"
            f"Страница: {page}\n"
            f"Номер записи: {index}\n"
            f"Фамилия: {entry['last_name']}\n"
            f"Имя: { entry['first_name']}\n"
            f"Отчество: {entry['middle_name']}\n"
            f"Организация: {entry['organization']}\n"
            f"Рабочий телефон: {entry['work_phone']}\n"
            f"Личный (сотовый) телефон: {entry['personal_phone']}"
            )
        print(output_text)


# Функция для добавления новой записи
def add_entry(data: list) -> list:
    entry = {}
    entry['last_name'] = input('Введите фамилию: ')
    entry['first_name'] = input('Введите  имя: ')
    entry['middle_name'] = input('Введите отчество: ')
    entry['organization'] = input('Введите название организации: ')
    entry['work_phone'] = input('Введите рабочий телефон: ')
    entry['personal_phone'] = input('Введите личный (сотовый) телефон: ')
    data.append(entry)
    return data


# Функция для редактирования записей
def edit_entry(data: list, index: int) -> list:
    entry = data[index]
    entry['last_name'] = input('Введите фамилию: ')
    entry['first_name'] = input('Введите  имя: ')
    entry['middle_name'] = input('Введите отчество: ')
    entry['organization'] = input('Введите название организации: ')
    entry['work_phone'] = input('Введите рабочий телефон: ')
    entry['personal_phone'] = input('Введите личный (сотовый) телефон: ')
    data[index] = entry
    return data


# Функция для поиска записей
def search_entry(data: list, search_criteria: str) -> list:
    results = []
    for entry in data:
        if any(search_criteria.lower() in value.lower() for value in entry.values()):
            results.append(entry)
    return results


def main() -> None:
    filename = 'phone_book.json'
    data = load_data(filename)
    page_size = 5
    page = 1

    while True:  # Основное меню справочника и его логика работы
        print('1. Отобразить записи')
        print('2. Добавить записи')
        print('3. Редактировать записи')
        print('4. Поиск записей')
        choice = input('Введите цифру действия: ')

        if choice == '1':
            display_data(data, page, page_size)
            action = input(
                'Следующая страница (n) или Предыдущая (p) или Выход (q): '
                )
            if action.lower() == 'n':
                if (page - 1 * page_size) < len(data):
                    page += 1
                else:
                    print('ВЫ НА ПОСЛЕДНЕЙ СТРАНИЦЕ!!!')
            elif action.lower() == 'p':
                page -= 1
                if page < 1:
                    page = 1
            elif action.lower() == 'q':
                break
            else:
                print('#############################################')
                print('#!!!Некорректный ввод, попробуйте ещё раз!!!#')
                print('#############################################')
            display_data(data, page, page_size)
        elif choice == '2':
            data = add_entry(data)
            save_data(data, filename)
        elif choice == '3':
            index = int(input('Введите номер записи для редактирования: '))
            index -= 1  # Выравниваем чтобы была корректная обработка при работе со списком
            data = edit_entry(data, index)
            save_data(data, filename)
        elif choice == '4':
            search_criteria = input('Ведите данные для поиска: ')
            results = search_entry(data, search_criteria)
            for entry in results:
                output_text = (
                    f"***************************************\n"
                    f"Фамилия: {entry['last_name']}\n"
                    f"Имя: { entry['first_name']}\n"
                    f"Отчество: {entry['middle_name']}\n"
                    f"Организация: {entry['organization']}\n"
                    f"Рабочий телефон: {entry['work_phone']}\n"
                    f"Личный (сотовый) телефон: {entry['personal_phone']}"
                    )
                print(output_text)
        else:
            print('#############################################')
            print('#!!!Некорректный ввод, попробуйте ещё раз!!!#')
            print('#############################################')


if __name__ == "__main__":
    main()
