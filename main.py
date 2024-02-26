import json


class PhoneBook:
    """
    Класс, представляющий телефонную книгу.
    """

    def __init__(self, filename: str):
        """
        Инициализация объекта PhoneBook.
        """
        self.filename = filename
        self.data = self.load_data()

    def load_data(self) -> list:
        """
        Загрузка данных из файла.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    def save_data(self) -> None:
        """
        Сохранение данных в файл.

        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def display_data(self, page: int, page_size: int) -> None:
        """
        Вывод данных постранично.

        Parameters:
            page (int): Номер страницы.
            page_size (int): Размер страницы.

        """
        start = (page - 1) * page_size
        end = start + page_size
        for index, entry in enumerate(self.data[start:end], start=start+1):
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

    def add_entry(self) -> None:
        """
        Добавление новой записи.

        """
        entry = {}
        entry['last_name'] = input('Введите фамилию: ')
        entry['first_name'] = input('Введите имя: ')
        entry['middle_name'] = input('Введите отчество: ')
        entry['organization'] = input('Введите название организации: ')
        entry['work_phone'] = input('Введите рабочий телефон: ')
        entry['personal_phone'] = input('Введите личный (сотовый) телефон: ')
        self.data.append(entry)
        self.save_data()

    def edit_entry(self, index: int) -> None:
        """
        Редактирование записи.

        """
        entry = self.data[index]
        entry['last_name'] = input('Введите фамилию: ')
        entry['first_name'] = input('Введите имя: ')
        entry['middle_name'] = input('Введите отчество: ')
        entry['organization'] = input('Введите название организации: ')
        entry['work_phone'] = input('Введите рабочий телефон: ')
        entry['personal_phone'] = input('Введите личный (сотовый) телефон: ')
        self.data[index] = entry
        self.save_data()

    def search_entry(self, search_criteria: str) -> list:
        """
        Поиск записей.

        Parameters:
            search_criteria (str): Критерий поиска.

        Returns:
            list: Список найденных записей.

        """
        results = []
        for entry in self.data:
            if any(search_criteria.lower() in value.lower() for value in entry.values()):
                results.append(entry)
        return results

    def main(self) -> None:
        """
        Основное меню справочника и его логика работы.

        """

        page_size = 5
        page = 1

        while True:
            print('1. Отобразить записи')
            print('2. Добавить записи')
            print('3. Редактировать записи')
            print('4. Поиск записей')
            choice = input('Введите цифру действия: ')

            match choice:
                case "1":
                    self.display_data(page, page_size)
                    action = input(
                        'Следующая страница (n) или Предыдущая (p) или Выход (q): '
                    )
                    match action.lower():
                        case "n":
                            if (page * page_size) < len(self.data):
                                page += 1
                            else:
                                print('ВЫ НА ПОСЛЕДНЕЙ СТРАНИЦЕ!!!')
                        case "p":
                            page -= 1
                            if page < 1:
                                page = 1
                        case "q":
                            break
                        case _:
                            print('#############################################')
                            print('#!!!Некорректный ввод, попробуйте ещё раз!!!#')
                            print('#############################################')
                            continue
                    self.display_data(page, page_size)
                case "2":
                    self.add_entry()
                case "3":
                    index = int(input('Введите номер записи для редактирования: '))
                    index -= 1
                    if index < 0 or index >= len(self.data):
                        print('Некорректный номер записи!')
                        continue
                    self.edit_entry(index)
                case "4":
                    search_criteria = input('Введите данные для поиска: ')
                    results = self.search_entry(search_criteria)
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
                case _:
                    print('#############################################')
                    print('#!!!Некорректный ввод, попробуйте ещё раз!!!#')
                    print('#############################################')


if __name__ == '__main__':
    phonebook = PhoneBook('phone_book.json')
    phonebook.main()
