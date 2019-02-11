#!/usr/bin/env python3
# coding=UTF8
import sqlite3


class DataBase:
    """ Класс работы с базой
        init - создает коннектор и курсор
    """
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

    def create_db(self):

        # Создание таблицы client
        self.cursor.execute("""CREATE TABLE client
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                name text NOT NULL,
                                phone_number INTEGER NOT NULL,
                                pin_code integer NOT NULL)
                            """)

        # Созданине таблицы account
        self.cursor.execute("""CREATE TABLE account
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                client_id INTEGER NOT NULL,
                                account_number INTEGER NOT NULL,
                                balance REAL NOT NULL DEFAULT 0                                
                                )
                            """)

    # функция добавления тестовых данных
    def insert_test_data(self, table, data):
        if table == 'account':
            columns = 'client_id,account_number,balance'
        elif table == 'client':
            columns = 'name,phone_number,pin_code'
        val = '?'
        for i in data[0][:-1]:
            val = val + ',?'
        val = '?,?,?'
        self.cursor.executemany("INSERT INTO " + str(table) + "("+columns+") VALUES (" + val + ")", data)
        self.conn.commit()

    # функция проверки баланса по номеру счета
    def select_balance(self, account_number):
        self.cursor.execute("select balance from account where account_number = '" + str(account_number) + "'")
        result = self.cursor.fetchall()
        if result:
            return result[0][0]
        else:
            return []

    # обновление данных бд при переводе
    def update_balance(self, from_ , to_, count):
        self.cursor.execute("update account set balance = (balance-" + count +\
                            ") WHERE account_number = '" + str(from_) + "'")
        self.cursor.execute("update account set balance = (balance+" + count + \
                            ") WHERE account_number = '" + str(to_) + "'")

    # вывод тестовых данных при запуске
    def select_join(self):
        self.cursor.execute("""select * 
                                from account left join client 
                                    on account.client_id = client.id""")
        return self.cursor.fetchall()
