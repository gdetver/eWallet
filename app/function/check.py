from app.db import db


# функция проверки баланса
def check_balance(value):
    if not value:
        return 'please input command "check xxxxxxxxx"'
    if not value[0].isdigit():
        answer = 'your account must be digits'
        return answer
    balance = db.select_balance(value[0])
    if balance:
        answer = 'your balance is equal ' + str(balance)
    else:
        answer = 'account ' + value[0] + ' does not exist'
    return answer
