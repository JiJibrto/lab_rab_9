# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения (список из трех чисел). Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту; вывод на экран информации о людях, чьи
# дни рождения приходятся на месяц, значение которого введено с клавиатуры; если таких
# нет, выдать на дисплей соответствующее сообщение.

if __name__ == '__main__':
    workers = []
    while True:
        command = input("Enter command> ").lower()

        if command == "exit":
            break

        elif command == "add":
            las_name = str(input("Enter last name>  "))
            name = str(input("Enter first name> "))
            tel = int(input("Enter phone> +"))
            date = list(map(int, input("Enter birthdate separated by space> ").split(" ")))

            temp = {
                'las_name': las_name,
                'name': name,
                'tel': tel,
                'date': date
            }
            workers.append(temp)
            # Отсортировать список в случае необходимости.
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('las_name', ''))

        elif command == "list":
            line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
                '-' * 4,
                '-' * 15,
                '-' * 15,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Телефон",
                    "Дата рождения"
                )
            )
            print(line)
            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                        idx,
                        worker.get('las_name', ''),
                        worker.get('name', ''),
                        worker.get('tel', 0),
                        ".".join(map(str, worker.get('date')))
                    )
                )
            print(line)

        elif command == "task":
            check = list(map(int, input("Enter birthdate separated by space> ").split(" ")))
            task_list = []
            iz = 0
            for worker in workers:
                if ''.join(map(str, worker.get('date'))) == ''.join(map(str, check)):
                    task_list.append(worker)
                    iz += 1

            if iz == 0:
                print("Workers not found")
            else:
                line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
                    '-' * 4,
                    '-' * 15,
                    '-' * 15,
                    '-' * 20,
                    '-' * 20
                )
                print(line)
                print(
                    "| {:^4} | {:^15} | {:^15} | {:^20} | {:^20} |".format(
                        "№",
                        "Фамилия",
                        "Имя",
                        "Телефон",
                        "Дата рождения"
                    )
                )
                print(line)
                for idx, worker in enumerate(task_list, 1):
                    print(
                        '| {:>4} | {:<15} | {:<15} | {:>20} | {:^20} |'.format(
                            idx,
                            worker.get('las_name', ''),
                            worker.get('name', ''),
                            worker.get('tel', 0),
                            ".".join(map(str, worker.get('date')))
                        )
                    )
                print(line)

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                workers = json.load(f)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(workers, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("task - вывести сотрудников определенной даты рождения")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - выход из программы;")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)