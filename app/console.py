#!/usr/bin/env python3
# coding=UTF8
import sys
from app.function.check import check_balance
from app.function.transfer import transfer_money
from app.sample.test_data import insert_test_data
import logging

commands = {'help': 'to print help information',
            'check': 'check account balance',
            'transfer': 'transfer money',
            'quit': 'Exit program',
            'exit': 'Exit program',
            }


# напрасление в нужную функцию обработки команд
def routing(command, value):
    if command == 'help':
        for key in commands.keys():
            answer(key + ' - ' + commands[key])
        return
    elif command in ['quit', 'exit']:
        sys.exit(0)
    elif command == 'check':
        answer(check_balance(value))
        return
    elif command == 'transfer':
        answer(transfer_money(value))
    return


# проверка на соответствие доступным командам
def check_command(c):
    if c.lower() in commands:
        return c.lower()
    else:
        return False


# парсинг введенных данных
def parse_input(t):
    # обрезаем начальные и конечные пробелы
    t = t.strip()
    # разбиваем строку на кортеж слов
    t = t.split(' ')
    # проверяем первый элемент на пренодлежность к команде
    command = check_command(t[0])

    if not command:
        return False, []
    else:
        return command, t[1:]


# функция ответа пользователю. в данном случае просто принт,
# но могло быть взаимодействие с GUI или API
def answer(t):
    print(t)
    logging.info(str(t))


# основной цикл программы
def start():
    try:
        insert_test_data()
        answer('please input the command or input "help"' )
    except Exception as Ex:
        logging.error(Ex)
    try:
        while True:
            text = input()
            answer('input: ' + str(text))
            command, value = parse_input(text)
            answer('parse: ' + str(command) + str(value) + '\n\nresult:')
            if command:
                routing(command, value)
            else:
                answer('unknown command')
    except Exception as Ex:
        logging.error(Ex)


if __name__ == "__main__":
    while True:
        try:
            text = input()
            command, value = parse_input(text)
            answer('input: ' + str(text))
            answer('parse: ' + command + value)
            if command:
                routing(command, value)
            else:
                answer('unknown command')
        except Exception as Ex:
            logging.error(Ex)

